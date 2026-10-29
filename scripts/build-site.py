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
def page(tpl, title, body, base, navigation):
    for key, value in {'title':html.escape(title),'body':body,'base':base,'navigation':navigation,'lang':'es'}.items():
        tpl = tpl.replace('{{'+key+'}}',value)
    return tpl
def build(profile, out):
    config = yaml.safe_load((profile/'.trayector/settings/site.yaml').read_text()) or {}
    if not config.get('enabled', False):
        return
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
    for section, folder in [('experience','experience'),('articles','content')]:
        if not options[section]: continue
        target=out/section
        target.mkdir()
        entries=[]
        for n, path in enumerate(sorted((profile/folder).rglob('*.md')) if (profile/folder).is_dir() else []):
            meta, body=parse(path.read_text())
            if section=='articles' and str(meta.get('status','published')).lower() in ('draft','private'): continue
            slug=re.sub('[^a-z0-9]+','-',path.relative_to(profile/folder).with_suffix('').as_posix().lower()).strip('-') or str(n)
            title=str(meta.get('title') or next((x[2:] for x in body.splitlines() if x.startswith('# ')),path.stem))
            (target/(slug+'.html')).write_text(page(tpl,title,convert(body),'../',nav.replace('href="','href="../')))
            entries.append('<li><a href="'+html.escape(slug)+'.html">'+html.escape(title)+'</a></li>')
        (target/'index.html').write_text(page(tpl,section.title(),'<h1>'+section.title()+'</h1><ul>'+''.join(entries)+'</ul>','../',nav.replace('href="','href="../')))
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
