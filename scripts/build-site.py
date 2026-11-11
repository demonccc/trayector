import argparse, html, re, shutil
from pathlib import Path
import markdown, yaml, bleach
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import simpleSplit

root = Path(__file__).resolve().parent.parent / 'site'
tags = set(bleach.sanitizer.ALLOWED_TAGS) | {'p','h1','h2','h3','h4','pre','code','hr','br','img','table','thead','tbody','tr','td','th'}
attrs = {'a':['href','title'], 'img':['src','alt','title']}
def convert(src):
    return bleach.clean(markdown.markdown(src, extensions=['extra']), tags=tags, attributes=attrs, protocols=['http','https','mailto'], strip=True)
def parse(src):
    if src.startswith('---\n'):
        _, meta, text = src.split('---\n', 2)
        return yaml.safe_load(meta) or {}, text
    return {}, src
def page(tpl, title, body, base, navigation, lang='es'):
    for key, value in {'title':html.escape(title),'body':body,'base':base,'navigation':navigation,'lang':html.escape(lang)}.items():
        tpl = tpl.replace('{{'+key+'}}',value)
    return tpl
def build(profile, out):
    config = yaml.safe_load((profile/'.trayector/settings/site.yaml').read_text()) or {}
    if not config.get('enabled', False):
        return
    languages = config.get('languages', ['es'])
    if not isinstance(languages, list) or not languages or any(not isinstance(v, str) or not re.fullmatch(r'[a-z]{2,3}(?:-[A-Za-z0-9]+)*', v) for v in languages):
        raise ValueError('site.languages must be a non-empty list of language codes')
    if len(languages) != len(set(languages)):
        raise ValueError('site.languages contains duplicate languages')
    if out == profile or profile in out.parents:
        raise ValueError('Output may not overwrite career source')
    if out.exists(): shutil.rmtree(out)
    out.mkdir(parents=True)
    shutil.copytree(root/'assets',out/'assets')
    tpl=(root/'templates/base.html').read_text()
    options = {key:bool(config.get(key,{}).get('enabled',False)) for key in ('articles','experience','cv')}
    nav=''.join('<a href="'+route+'">'+title+'</a> ' for key,route,title in (('experience','experience/index.html','Experiencia'),('articles','articles/index.html','Artículos'),('cv','cv/index.html','CV')) if options[key])
    profile_md=profile/'PROFILE.md'
    if not profile_md.is_file(): raise FileNotFoundError('Missing PROFILE.md')
    (out/'index.html').write_text(page(tpl,'Perfil',convert(parse(profile_md.read_text())[1]),'',nav))
    # Experience retains its existing record renderer.
    if options['experience']:
        target = out/'experience'
        target.mkdir()
        entries = []
        for n, path in enumerate(sorted((profile/'experience').rglob('*.md')) if (profile/'experience').is_dir() else []):
            meta, body = parse(path.read_text(encoding='utf-8'))
            slug = re.sub('[^a-z0-9]+', '-', path.relative_to(profile/'experience').with_suffix('').as_posix().lower()).strip('-') or str(n)
            title = str(meta.get('title') or next((x[2:] for x in body.splitlines() if x.startswith('# ')), path.stem))
            (target/(slug+'.html')).write_text(page(tpl,title,convert(body),'../',nav.replace('href="','href="../')),encoding='utf-8')
            entries.append('<li><a href="'+html.escape(slug)+'.html">'+html.escape(title)+'</a></li>')
        (target/'index.html').write_text(page(tpl,'Experiencia','<h1>Experiencia</h1><ul>'+''.join(entries)+'</ul>','../',nav.replace('href="','href="../')),encoding='utf-8')

    # Articles are opt-in and indexed by a readable README, not front matter.
    if options['articles']:
        target = out/'articles'
        target.mkdir()
        entries = []
        allowed = config.get('articles',{}).get('include',[])
        if not isinstance(allowed,list):
            raise ValueError('articles.include must be a list of approved article directory names')
        for slug in allowed:
            if not isinstance(slug,str) or not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_-]*',slug):
                raise ValueError('Invalid article directory name in articles.include')
            article = profile/'articles'/slug
            readme = article/'README.md'
            if not readme.is_file():
                raise FileNotFoundError('Approved article has no README.md: '+slug)
            source = readme.read_text(encoding='utf-8')
            title = next((line[2:].strip() for line in source.splitlines() if line.startswith('# ')),slug)
            section = re.search(r'^## Content\s*\n(.*?)(?=^## |\Z)', source, re.M|re.S)
            if not section:
                raise ValueError('Article README is missing ## Content: '+slug)
            translations = re.findall(r'^\s*[-*]\s*([^:\n]+):\s*\[([^\]]+)\]\(([^)]+)\)\s*$',section.group(1),re.M)
            if not translations:
                raise ValueError('Article has no linked language files: '+slug)
            available = [(label, caption, filename) for label, caption, filename in translations if filename.endswith('.md') and filename[:-3] in languages]
            if not available:
                continue
            destination = target/slug
            destination.mkdir()
            assets = article/'assets'
            if assets.is_dir():
                shutil.copytree(assets,destination/'assets')
            language_links = []
            for label,_,filename in available:
                if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_-]*\.md',filename):
                    raise ValueError('Unsafe article language file name: '+filename)
                lang = filename[:-3]
                body_path = article/filename
                if not body_path.is_file():
                    raise FileNotFoundError('Missing article language file: '+str(body_path))
                body = body_path.read_text(encoding='utf-8')
                page_title = next((line[2:].strip() for line in body.splitlines() if line.startswith('# ')),title)
                links = '<nav aria-label="Languages">'+''.join('<a href="'+html.escape(f[:-3])+'.html">'+html.escape(l)+'</a> ' for l,_,f in available)+'</nav>'
                rendered = convert(body)
                (destination/(lang+'.html')).write_text(page(tpl,page_title,links+rendered,'../../',nav.replace('href="','href="../../'),lang),encoding='utf-8')
                language_links.append('<a href="'+html.escape(slug)+'/'+html.escape(lang)+'.html">'+html.escape(label.strip())+'</a>')
            summary = re.search(r'^## Summary\s*\n(.*?)(?=^## |\Z)', source,re.M|re.S)
            excerpt = convert(summary.group(1).strip()) if summary else ''
            entries.append('<li><strong>'+html.escape(title)+'</strong>'+excerpt+'<p>'+' · '.join(language_links)+'</p></li>')
        (target/'index.html').write_text(page(tpl,'Artículos','<h1>Artículos</h1><ul>'+''.join(entries)+'</ul>','../',nav.replace('href="','href="../')),encoding='utf-8')
    if options['cv']:
        slug=str(config['cv'].get('selected','general'))
        if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_-]*',slug):
            raise ValueError('CV selected must be a simple filename without directories')
        source=profile/'cv'/(slug+'.md')
        if not source.is_file(): raise FileNotFoundError('Selected CV does not exist: '+str(source))
        meta, resume=parse(source.read_text(encoding='utf-8'))
        (out/'cv').mkdir()
        (out/'cv/index.html').write_text(page(tpl,str(meta.get('title') or 'CV'),'<p><a href="resume.pdf">Descargar PDF</a></p>'+convert(resume),'../',nav.replace('href="','href="../')),encoding='utf-8')
        # Generate a text-based PDF deterministically from the *same* reviewed Markdown.
        pdf=canvas.Canvas(str(out/'cv/resume.pdf'),pagesize=A4)
        width,height=A4
        left,top,bottom=48,height-54,48
        y=top
        for raw in resume.splitlines():
            line=raw.strip()
            if not line:
                y-=10
                continue
            heading=line.startswith('#')
            line=re.sub(r'^#{1,6}\s*','',line)
            line=re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',line)
            line=re.sub(r'[*_`]+','',line)
            font='Helvetica-Bold' if heading else 'Helvetica'
            size=13 if heading else 10
            pdf.setFont(font,size)
            for wrapped in simpleSplit(line,font,size,width-96):
                if y<bottom:
                    pdf.showPage()
                    y=top
                    pdf.setFont(font,size)
                pdf.drawString(left,y,wrapped)
                y-=size*1.45
        pdf.save()
    (out/'.nojekyll').touch()
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--profile',required=True,type=Path)
    p.add_argument('--output',required=True,type=Path)
    args=p.parse_args()
    build(args.profile.resolve(),args.output.resolve())
