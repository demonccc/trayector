import argparse, html, re, shutil
from pathlib import Path
import markdown, yaml, bleach

root = Path(__file__).resolve().parent
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
    nav=''.join('<a href="'+route+'">'+title+'</a> ' for key,route,title in (('experience','experience/index.html','Experiencia'),('articles','articles/index.html','Artículos'),('cv','cv/general.pdf','CV')) if options[key])
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
        if config['cv'].get('profile')!='general': raise ValueError('Only the general CV is supported by the default site')
        source=profile/'generated/cv/general.pdf'
        if not source.is_file(): raise FileNotFoundError('CV enabled but generated/cv/general.pdf does not exist')
        (out/'cv').mkdir()
        shutil.copy2(source,out/'cv/general.pdf')
    (out/'.nojekyll').touch()
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--profile',required=True,type=Path)
    p.add_argument('--output',required=True,type=Path)
    args=p.parse_args()
    build(args.profile.resolve(),args.output.resolve())
