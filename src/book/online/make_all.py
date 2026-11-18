import base64, re, subprocess, shutil
subprocess.run(['python3','build_book.py'],check=True)
h=open('Rihlati_online.html').read()
f=lambda p: base64.b64encode(open(p,'rb').read()).decode()
css=('<style>@font-face{font-family:"Amiri Quran";src:url(data:font/ttf;base64,'+f('../fonts/AmiriQuran-Regular.ttf')+')}'
     '@font-face{font-family:"Nunito";font-weight:200 1000;src:url(data:font/ttf;base64,'+f('../fonts/Nunito.ttf')+')}</style>')
h=h.replace('<link rel="preconnect" href="https://fonts.googleapis.com">\n','')
h=re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>', lambda m: css, h)
h=h.replace('<meta name="claude:viewport-fit-sides" content="cover">','<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">')
off='<!doctype html>\n<html lang="ru"><head>'+h+'</html>'
open('/home/claude/book/Rihlati_onlain_kniga.html','w').write(off)

import hashlib, base64 as _b64, json as _json
USED = {}
EXTERNAL_AUDIO = True   # True — звуки отдельными файлами (облегчение сайта, ждёт согласия)
def urlmap(path, prefix, out):
    if not EXTERNAL_AUDIO: return open(path).read()
    root = os.path.dirname(out) if prefix == '' else os.path.dirname(os.path.dirname(out))
    d = _json.load(open(path)); os.makedirs(root + '/audio/v', exist_ok=True)
    for k, v in d.items():
        if isinstance(v, str) and v.startswith('data:'):
            b = _b64.b64decode(v.split(',', 1)[1]); name = hashlib.md5(b).hexdigest()[:12] + '.mp3'
            fp = root + '/audio/v/' + name
            if not os.path.exists(fp): open(fp, 'wb').write(b)
            USED.setdefault(root, set()).add(name); d[k] = prefix + 'audio/v/' + name
    return _json.dumps(d, ensure_ascii=False)
def app(src, prefix, out, sw_link):
    h=open(src).read()
    h=h.replace('<link rel="preconnect" href="https://fonts.googleapis.com">\n','')
    h=re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>', lambda m: css, h)
    h=h.replace('<meta name="claude:viewport-fit-sides" content="cover">','<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">')
    h='<!doctype html>\n<html lang="ru"><head>'+h+'</html>'
    head=f"""<meta name="theme-color" content="#E4EEF6">
<link rel="manifest" href="{prefix}manifest.webmanifest">
<link rel="icon" type="image/png" href="{prefix}favicon.png">
<link rel="apple-touch-icon" href="{prefix}apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Рихляти">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
"""
    a=h.replace('<html lang="ru"><head>','<html lang="ru"><head>'+head,1).replace('<title>Моё путешествие к Корану</title>','<title>Рихляти — путешествие к Корану</title>')
    a=a.replace('<div class="app">', '<div class="app">\n  ' + sw_link, 1)
    a=a.replace('<button class="tocover" id="toCover">', sw_link.replace('class="lang-sw"','class="lang-sw sm"') + '<button class="tocover" id="toCover">', 1) if False else a
    js=f"""<script>
if('serviceWorker' in navigator){{ addEventListener('load',()=>navigator.serviceWorker.register('{prefix}sw.js',{{scope:'{prefix}'}}).catch(()=>{{}})); }}
</script>
</html>"""
    a=a.replace('</head>', LSW_CSS + '</head>', 1) if '</head>' in a else a.replace('<style>', LSW_CSS + '<style>', 1)
    a=a.replace('<head>','<head><script>window.SONGS='+urlmap('/home/claude/book/online/songs.json', prefix, out)+';</script>',1)
    a=a.replace('<head>','<head><script>window.VOICE='+urlmap('/home/claude/book/online/voice.json', prefix, out)+';</script>',1)
    _vn = 'voice_names.json' if ('/qt/' in out or '/tr/' in out) else 'voice_names_ru.json'
    a=a.replace('<head>','<head><script>window.VOICE_N='+urlmap('/home/claude/book/online/'+_vn, prefix, out)+';</script>',1)
    a=a[:-7]+LSW_JS+GC_JS+js
    if '/tr/' in out: a=a.replace('<html lang="ru">','<html lang="tr">',1).replace('content="Рихляти"','content="Rihleti"',1)
    open(out,'w').write(a)
import os
LSW_CSS = """<style>
.lsw{position:absolute;z-index:30;top:6px;left:50%;transform:translateX(-50%);display:flex;background:var(--paper);border:2px solid var(--line);border-radius:999px;padding:3px;gap:2px;box-shadow:0 3px 10px rgba(0,0,0,.06)}
.lsw a{font:inherit;font-weight:800;font-size:13px;color:var(--ink-soft);text-decoration:none;padding:.4em 1em;border-radius:999px;white-space:nowrap}
.lsw a.on{background:var(--indigo);color:#fff}
.lsw a:focus-visible{outline:3px solid var(--gold);outline-offset:2px}
.app.oncover{padding-top:52px!important}
.app:not(.oncover)>.lsw{display:none}
.lsw.mini{position:static;transform:none;box-shadow:none;padding:2px}
.lsw.mini a{font-size:11px;padding:.35em .7em}
@media (max-width:560px){.lsw.mini{order:5;margin:0 auto}.lsw.mini a{font-size:11px;padding:.3em .7em}}
</style>"""
def SW(cur, up):
    L = [('ct', 'qt/', 'Къырымтатарджа'), ('ru', '', 'Русский'), ('tr', 'tr/', 'Türkçe')]
    return ('<nav class="lsw" aria-label="Til / Язык / Dil">' + ''.join(
        f'<a href="{up}{p or "./"}" data-lang="{k}" class="{"on" if k==cur else ""}">{t}</a>' if up=='' else
        f'<a href="{up}{p}" data-lang="{k}" class="{"on" if k==cur else ""}">{t}</a>' for k, p, t in L) + '</nav>')
GC_JS = """<script>
// статистика посещений (GoatCounter, без cookie и личных данных)
window.goatcounter = {no_onload: true};
function gcCount(){ try { if(window.goatcounter && window.goatcounter.count) window.goatcounter.count({path: location.pathname + (location.hash || '#cover')}); } catch(e){} }
addEventListener('hashchange', gcCount);
</script>
<script data-goatcounter="https://rihlati.goatcounter.com/count" async src="https://gc.zgo.at/count.js" onload="gcCount()"></script>
"""
LSW_JS = """<script>
document.querySelectorAll('.lsw a').forEach(a => a.addEventListener('click', e => { if(a.classList.contains('on')){ e.preventDefault(); return; } e.preventDefault(); location.href = a.getAttribute('href') + location.hash; }));
(function(){ const app = document.querySelector('.app'), les = document.getElementById('lesson');
  const cov = document.getElementById('cover');
  const upd = () => app.classList.toggle('oncover', !cov.hidden); upd(); new MutationObserver(upd).observe(cov, {attributes:true, attributeFilter:['hidden']}); })();
</script>"""
SW_RU = SW('ru', '')
SW_CT = SW('ct', '../')
SW_TR = SW('tr', '../')
for out_dir in ['/home/claude/ruhlar-', '/home/claude/book/app/rihlati']:
    os.makedirs(out_dir+'/qt', exist_ok=True); os.makedirs(out_dir+'/tr', exist_ok=True)
    app('Rihlati_online.html', '', out_dir+'/index.html', SW_RU)
    app('Rihlati_online_ct.html', '../', out_dir+'/qt/index.html', SW_CT)
    app('Rihlati_online_tr.html', '../', out_dir+'/tr/index.html', SW_TR)
for root, names in (USED.items() if EXTERNAL_AUDIO else []):
    for fn in os.listdir(root + '/audio/v'):
        if fn not in names: os.remove(root + '/audio/v/' + fn)
print('ok')
