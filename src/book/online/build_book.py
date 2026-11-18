import sys, re, json; sys.path.insert(0,'/home/claude/book')
import chars, chars4, data, icons_ru as I
def mk(pal):
    A = lambda **k: re.sub(r' width="150"', '', chars4.adam(pal=pal, **k), count=1)
    M = lambda **k: re.sub(r' width="150"', '', chars4.maryam(pal=pal, **k), count=1)
    return {'a_wave': A(right='wave'), 'm_wave': M(left='wave'), 'a_point': A(right='point', mood='open'), 'm_point': M(left='point', mood='open'),
            'a_book': A(book=True), 'm_book': M(book=True), 'a_open': A(right='wave', mood='open'), 'm_wink': M(left='wave', mood='wink'),
            'a_wink': A(right='wave', mood='wink'), 'm_open': M(left='wave', mood='open')}
def c(fn, **k):
    return re.sub(r' width="100"', '', getattr(chars, fn)(w=100, **k), count=1)
CH = {'a_wave': c('adam', right='wave'), 'm_wave': c('maryam', left='wave'),
      'a_point': c('adam', right='point', mood='open'), 'm_point': c('maryam', left='point', mood='open'),
      'a_book': c('adam', book=True), 'm_book': c('maryam', book=True),
      'a_open': c('adam', right='wave', mood='open'), 'm_wink': c('maryam', left='wave', mood='wink'),
      'a_wink': c('adam', right='wave', mood='wink'), 'm_open': c('maryam', left='wave', mood='open')}
BASE = dict(zip("بتثجخذزشضظغفقني", "ٮٮٮححدرسصطعڡٯںى"))
DOTS = {"ب":"одну точку","ت":"две точки","ث":"три точки","ج":"точку","خ":"точку","ذ":"точку","ز":"точку","ش":"три точки","ض":"точку","ظ":"точку","غ":"точку","ف":"точку","ق":"две точки","ن":"точку","ي":"две точки"}
SIM = {"ا":"لد","ب":"تث","ت":"بث","ث":"تب","ج":"حخ","ح":"جخ","خ":"حج","د":"ذر","ذ":"دز","ر":"زو","ز":"رذ","س":"شص","ش":"سص","ص":"ضس","ض":"صط","ط":"ظص","ظ":"طض","ع":"غح","غ":"عف","ف":"قو","ق":"فك","ك":"لق","ل":"اك","م":"وه","ن":"بت","ه":"مو","و":"رم","ي":"نب"}
def clean(s):
    s = re.sub(r'[\U0001F300-\U0001FAFF☀-➿️]', '', s).strip()
    return re.sub(r'\{(.+?)\}', r'<span class="arin">\1</span>', s)
L = []
for (ch, ar, ru, snd, shape, con), r in zip(data.LETTERS, I.RU):
    assert r[0] == ch
    L.append(dict(ch=ch, ar=ar, ru=ru, snd=clean(snd), shape=clean(shape), word=r[1], special=r[4],
                  hint=r[3] or "", ico=I.icon(r[2]), base=BASE.get(ch, ""), dots=DOTS.get(ch, ""), sim=list(SIM[ch])))
NEWMN = json.load(open('newmn.json'))
SOFT = {"ث": "Тихое «с»: кончик языка чуть-чуть выглядывает между зубками, без голоса.",
        "ذ": "Звонкое «з»: кончик языка чуть-чуть выглядывает между зубками.",
        "ظ": "Толстое, твёрдое «з»: кончик языка чуть-чуть выглядывает между зубками."}
for l in L:
    if l['ch'] in NEWMN:
        l['word'], l['ico'] = NEWMN[l['ch']]; l['special'] = False; l['hint'] = ''; l['snd'] = SOFT[l['ch']]
html = open('book_template.html').read()
html = html.replace('/*GT*/', '')
LR = list(L)
# (Лям-Алиф убрана по просьбе автора) LR.insert(len(LR) - 1, dict(ch='لا', ar='لَامْ أَلِفْ', ru='Лям-Алиф', snd='', shape='Лям и Алиф держатся за руки', word='لَا «ля» — Лям и Алиф, два друга', special=True, hint='Так пишутся вместе Лям и Алиф. Читается «ля».',
#                             ico=I.icon('يَدٌ'), base='', dots='', sim=['ل', 'ا']))
html = html.replace('/*DATA*/', 'const LET=' + json.dumps(LR, ensure_ascii=False) + ';\nconst SH=' + open('shift.json').read() + ';\nconst CH=' + json.dumps(mk('ru'), ensure_ascii=False) + ';')
html = html.replace('/*HAR*/', open('har.js').read()).replace('/*SK*/', open('sk.js').read()).replace('/*P*/', 'const PL=' + open('pl.json').read() + ';\n' + open('p.js').read())
open('Rihlati_online.html', 'w').write(html)
print(len(html))

# ======================================================= крымскотатарская версия (черновик перевода)
import ct, chars3
def c3(fn, **k):
    s = getattr(chars3, fn)(w=100, **k)
    return re.sub(r' width="100"', '', s, count=1)
CH3 = {'a_wave': c3('adam', right='wave'), 'm_wave': c3('maryam', left='wave'),
       'a_point': c3('adam', right='point', mood='open'), 'm_point': c3('maryam', left='point', mood='open'),
       'a_book': c3('adam', left='hold', right='hold'), 'm_book': c3('maryam', left='hold', right='hold'),
       'a_open': c3('adam', right='wave', mood='open'), 'm_wink': c3('maryam', left='wave'),
       'a_wink': c3('adam', right='wave'), 'm_open': c3('maryam', left='wave', mood='open')}
LC = []
for l in L:
    n, shape, word, ico, special = ct.LETTERS_CT[l['ch']]
    kind, key = ico.split(':', 1)
    icon = NEWMN[key][1] if kind == 'new' else I.icon(key)
    LC.append(dict(l, ru=n, shape=shape, word=word, ico=icon, special=special, hint='', snd='', dots=ct.DOTS_CT.get(l['dots'], '')))
LAMALIF = dict(ch='لا', ar='لَامْ أَلِفْ', ru='Лям-Элиф', snd='', shape='Лям ве Элиф къол-къола тутушалар', word='لَا «ля» — Лям ве Элиф эки дост', special=True, hint='',
               ico=I.icon('يَدٌ'), base='', dots='', sim=['ل', 'ا'])
# (Лям-Алиф убрана по просьбе автора) LC.insert(len(LC) - 1, LAMALIF)
RED, BLUE, GOLD = "#B8603F", "#3F6B5A", "#C79A4E"
def tulip(x, y, s=1, col=RED):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 18 V36" stroke="#3F7A4A" stroke-width="2"/>'
            f'<path d="M0 30 Q-10 24 -12 14 Q-4 18 0 26Z M0 30 Q10 24 12 14 Q4 18 0 26Z" fill="#5E9E4E"/>'
            f'<path d="M-9 4 Q-10 18 0 20 Q10 18 9 4 L5 9 L0 0 L-5 9Z" fill="{col}"/><path d="M0 2 V16" stroke="#fff" stroke-width="1" opacity=".5"/></g>')
def band(w=620):
    out = ""
    for i, x in enumerate(range(30, w - 10, 62)):
        out += tulip(x, 4, .9, RED if i % 2 == 0 else BLUE)
        out += f'<circle cx="{x + 31}" cy="22" r="3.2" fill="{GOLD}"/><path d="M{x+20} 22 h22" stroke="{GOLD}" stroke-width="1.2"/>'
    return f'<svg class="ornek" viewBox="0 0 {w} 44" preserveAspectRatio="xMidYMid meet" aria-hidden="true">{out}</svg>'
CT_CSS = '''<style>
:root{--sky1:#E4EDE3;--sky2:#F8F1E4;--paper:#FFFCF6;--ink:#4A3A30;--ink-soft:#7D6A5C;--indigo:#3F6B5A;--rose:#B8603F;--rose-l:#F3E0D6;--sage:#7C9A6A;--sage-l:#E4EDDC;--gold:#C79A4E;--gold-l:#F3E6C8;--line:#E5D4B8;--red:#B8603F}
.btn{box-shadow:0 5px 0 #2E5042}.btn:active{box-shadow:0 2px 0 #2E5042}
.btn.rose{box-shadow:0 5px 0 #8E4529}.btn.sage,.navbtn.next{box-shadow:0 4px 0 #5C7A4C}
.ornek{display:block;width:min(100%,520px);height:auto;margin:0 auto}
.cv-card .ornek{width:min(92%,460px)}
.cv-card::before{border-color:#C79A4E;border-width:2px}
.section-t{border-color:#D9BE8A}
.lang-sw{font:inherit;font-weight:800;font-size:13px;color:var(--indigo);background:var(--paper);border:2px solid var(--line);border-radius:999px;padding:.35em 1em;text-decoration:none}
.ct-soon{background:rgba(255,253,248,.7);border:2px dashed var(--line);border-radius:18px;padding:10px 16px;color:var(--ink-soft);font-size:14px;max-width:520px;text-align:center}
</style>'''
h = open('book_template.html').read()
for a, b in ct.SRC:
    assert h.count(a) >= 1, ('нет фрагмента', a[:80])
    h = h.replace(a, b)
h = h.replace('<html', '<html', 1)
# орнамент на обложке и над картой
h = h.replace('<div class="cv-ar"', band() + '\n      <div class="cv-ar"', 1)
h = h.replace('<div class="cv-author">2026</div>', '<div class="cv-author">2026</div>\n      ' + band(), 1)
h = h.replace('<div class="section-t"><span class="dot"></span>Болюк 1.', band() + '\n    <div class="section-t"><span class="dot"></span>Болюк 1.', 1)
# пока только раздел 1: остальные разделы скрываем
for a, b in [('Раздел 2. Волшебные огласовки', 'Болюк 2. Тылсымлы харекелер'), ('Раздел 3. Сукун и шадда', 'Болюк 3. Сукун ве шедде'),
             ('Раздел 4. Танвин', 'Болюк 4. Тенвин'), ('Раздел 5. Мадд — длинные звуки', 'Болюк 5. Медд — узун сеслер')]:
    assert a in h, a; h = h.replace(a, b)
h = h.replace('/*DATA*/', 'const LET=' + json.dumps(LC, ensure_ascii=False) + ';\nconst SH=' + open('shift.json').read() + ';\nconst CH=' + json.dumps(mk('ct'), ensure_ascii=False) + ';')
import ct2
h = h.replace('/*GT*/', ct2.GT_JS)
h = h.replace('/*HAR*/', ct2.apply_js(open('har.js').read())).replace('/*SK*/', ct2.apply_js(open('sk.js').read()) + ct2.SETS_JS).replace('/*P*/', 'const PL=' + open('pl_ct.json').read() + ';\n' + ct2.apply_js(open('p.js').read()))
i = h.index('</style>') + len('</style>'); h = h[:i] + '\n' + CT_CSS + h[i:]
open('Rihlati_online_ct.html', 'w').write(h)
print('ct', len(h))

# ======================================================= турецкая версия
import tr_vals, tr2
LT = []
for l in L:
    n, shape, word, ico, special = tr_vals.LETTERS_TR[l['ch']]
    kind, key = ico.split(':', 1)
    icon = NEWMN[key][1] if kind == 'new' else I.icon(key)
    LT.append(dict(l, ru=n, shape=shape, word=word, ico=icon, special=special, hint='', snd='', dots=tr_vals.DOTS_TR.get(l['dots'], '')))
# (Лям-Алиф убрана по просьбе автора) LT.insert(len(LT) - 1, dict(ch='لا', ar='لَامْ أَلِفْ', ru='Lam-Elif', snd='', shape='Lam ile Elif el ele tutuşuyor', word='لَا «lâ» — Lam ile Elif iki dost', special=True, hint='',
#                ico=I.icon('يَدٌ'), base='', dots='', sim=['ل', 'ا']))
TR_CSS = '''<style>
:root{--sky1:#E2EEF2;--sky2:#FBF4EA;--paper:#FFFDF8;--ink:#3A3F4A;--ink-soft:#6B7280;--indigo:#245E86;--rose:#C2563F;--rose-l:#F6E1DA;--sage:#3E978B;--sage-l:#DDEFEC;--gold:#CF9F45;--gold-l:#F5E8C9;--line:#DCE3E6;--red:#C2563F}
.btn{box-shadow:0 5px 0 #18476A}.btn:active{box-shadow:0 2px 0 #18476A}
.btn.rose{box-shadow:0 5px 0 #943E2B}.btn.sage,.navbtn.next{box-shadow:0 4px 0 #2C7268}
.ornek{display:block;width:min(100%,520px);height:auto;margin:0 auto}
.cv-card .ornek{width:min(92%,460px)}
</style>'''
RED, BLUE, GOLD = "#C2563F", "#245E86", "#CF9F45"
h = open('book_template.html').read()
for (a, _), b in zip(ct.SRC, tr_vals.V):
    assert h.count(a) >= 1, ('нет фрагмента', a[:80])
    h = h.replace(a, b)
h = h.replace('<div class="cv-ar"', band() + '\n      <div class="cv-ar"', 1)
h = h.replace('<div class="cv-author">2026</div>', '<div class="cv-author">2026</div>\n      ' + band(), 1)
for a, b in [('Раздел 2. Волшебные огласовки', 'Bölüm 2. Sihirli harekeler'), ('Раздел 3. Сукун и шадда', 'Bölüm 3. Cezm ve şedde'),
             ('Раздел 4. Танвин', 'Bölüm 4. Tenvin'), ('Раздел 5. Мадд — длинные звуки', 'Bölüm 5. Med — uzun sesler'),
             ('Эльмаза Темиркалиева · 2026', 'Elmaza Temirkaliyeva · 2026')]:
    assert a in h, a; h = h.replace(a, b)
h = h.replace('/*DATA*/', 'const LET=' + json.dumps(LT, ensure_ascii=False) + ';\nconst SH=' + open('shift.json').read() + ';\nconst CH=' + json.dumps(mk('tr'), ensure_ascii=False) + ';')
h = h.replace('/*GT*/', tr2.GT_JS)
h = h.replace('/*HAR*/', tr2.apply_js(open('har.js').read())).replace('/*SK*/', tr2.apply_js(open('sk.js').read()) + tr2.SETS_JS).replace('/*P*/', 'const PL=' + open('pl_tr.json').read() + ';\n' + tr2.apply_js(open('p.js').read()))
i = h.index('</style>') + len('</style>'); h = h[:i] + '\n' + TR_CSS + h[i:]
open('Rihlati_online_tr.html', 'w').write(h)
print('tr', len(h))
