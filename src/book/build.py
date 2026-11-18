#!/usr/bin/env python3
"""Сборка рабочей книги «رِحْلَتِي مَعَ الْقُرْآنِ» — часть 1 (стр. 1–10).
HTML + CSS + SVG → Chrome headless → PDF (A4, вертикально)."""
import pathlib, random
from chars import adam, maryam

ROOT = pathlib.Path(__file__).parent
random.seed(7)

# ---------------------------------------------------------------- декор
def star(x, y, r=8, fill="#D8B26A", rot=0):
    import math
    pts = []
    for i in range(10):
        a = math.pi / 5 * i - math.pi / 2 + rot
        rr = r if i % 2 == 0 else r * 0.45
        pts.append(f"{x + rr*math.cos(a):.1f},{y + rr*math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke-linejoin="round"/>'

def cloud(x, y, s=1, fill="#fff", op=1):
    return (f'<g transform="translate({x} {y}) scale({s})" opacity="{op}" fill="{fill}">'
            '<ellipse cx="0" cy="10" rx="46" ry="16"/><circle cx="-18" cy="2" r="18"/>'
            '<circle cx="8" cy="-6" r="24"/><circle cx="30" cy="4" r="16"/></g>')

def crescent(x, y, r=14, fill="#D8B26A", bg="#fff"):
    return (f'<g><circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>'
            f'<circle cx="{x + r*0.45}" cy="{y - r*0.2}" r="{r*0.85}" fill="{bg}"/></g>')

def flower(x, y, s=1, petal="#E9C9C0", core="#D8B26A"):
    p = "".join(f'<ellipse cx="0" cy="-7" rx="4.5" ry="7" transform="rotate({a})" fill="{petal}"/>' for a in range(0, 360, 72))
    return f'<g transform="translate({x} {y}) scale({s})">{p}<circle r="3.6" fill="{core}"/></g>'

def sky_svg(w=794, h=1123, top=True):
    """Фоновые облака/звёзды для краёв страницы (не заходят в рабочую зону)."""
    els = []
    if top:
        els += [cloud(90, 40, .9, "#fff", .9), cloud(700, 30, 1.1, "#fff", .9)]
    for (x, y, r, c) in [(30, 300, 6, "#D8B26A"), (765, 420, 7, "#E9C9C0"), (25, 760, 5, "#D3B8A4"),
                         (770, 900, 6, "#D8B26A"), (40, 1060, 7, "#8E9DC6"), (760, 140, 5, "#D3B8A4")]:
        els.append(star(x, y, r, c))
    return f'<svg class="sky" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{"".join(els)}</svg>'

def arch_frame(color="#D3B8A4", fill="#FBF6F0", w=300, h=360):
    """Восточная арка для большой буквы."""
    d = (f"M14 {h-10} L14 150 Q14 92 {w/2-40} 60 Q{w/2-8} 40 {w/2} 10 "
         f"Q{w/2+8} 40 {w/2+40} 60 Q{w-14} 92 {w-14} 150 L{w-14} {h-10} Z")
    return (f'<svg class="arch" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="8" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="#fff" stroke-width="2.5" stroke-dasharray="1 9" stroke-linecap="round" transform="translate(0 0)"/>'
            f'{star(w/2, 26, 7, "#D8B26A")}</svg>')

def bubble(text_html, who="adam", side="left"):
    return f'<div class="bubble {who} {side}">{text_html}</div>'

def qr_slot(label="Аудио: произношение"):
    return (f'<div class="qr"><div class="qr-box"><span>QR</span></div>'
            f'<div class="qr-t">{label}<br><small>место для QR-кода<br>(аудио будет добавлено)</small></div></div>')

def reward(n):
    return f'<div class="reward"><svg viewBox="0 0 40 40" width="34">{star(20,21,17,"#fff")}</svg><span>Закрась звёздочку, когда закончишь!</span></div>'

def trace_svg(letter, size=150, w=170, h=200, dashed=True, base=None, solid=False, font="Amiri", y=None, pale=False):
    """Буква для обведения: бледная заливка + пунктирный контур."""
    y = y if y is not None else h * 0.66
    if solid:
        style = 'fill="#4A2C27"'
    elif pale:
        style = 'fill="#E2D3C6"'
    else:
        style = 'fill="#F6EEE6" stroke="#8E6F63" stroke-width="2.2" stroke-dasharray="7 5" stroke-linecap="round" stroke-linejoin="round"'
    bl = f'<line x1="6" y1="{base}" x2="{w-6}" y2="{base}" stroke="#C9D0E4" stroke-width="2" stroke-dasharray="3 6"/>' if base else ""
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" class="tr">{bl}'
            f'<text x="{w/2}" y="{y}" text-anchor="middle" direction="rtl" font-family="{font}" font-size="{size}" {style}>{letter}</text></svg>')

# ---------------------------------------------------------------- страницы
def page(body, cls="", num=None, section=None, sky=True):
    footer = f'<div class="pnum"><svg viewBox="0 0 40 40">{star(20,21,18,"#D8B26A")}</svg><b>{num}</b></div>' if num else ""
    sec = ""
    if section:
        ar, ru, col = section
        sec = f'<div class="sec" style="--sc:{col}"><span class="sec-ar" lang="ar" dir="rtl">{ar}</span><span class="sec-ru">{ru}</span></div>'
    return f'<section class="page {cls}">{sky_svg() if sky else ""}<div class="inner">{sec}{body}</div>{footer}</section>'

AR = lambda t, cls="": f'<span class="ar {cls}" lang="ar" dir="rtl">{t}</span>'

pages = []

# ===== 1. ОБЛОЖКА =====================================================
cover_stars = "".join(star(random.randint(40, 750), random.randint(30, 380), random.choice([5, 6, 8, 10]),
                           random.choice(["#D8B26A", "#fff", "#EED9A8"])) for _ in range(26))
cover_bg = f'''<svg class="cover-bg" viewBox="0 0 794 1123" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="cg" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#2E3D66"/><stop offset=".42" stop-color="#3E5180"/><stop offset=".7" stop-color="#9AA0BC"/><stop offset=".86" stop-color="#F4EBE2"/></linearGradient></defs>
<rect width="794" height="1123" fill="url(#cg)"/>{cover_stars}{crescent(680, 110, 34, "#D8B26A", "#31406A")}
{cloud(120, 160, 1.3, "#fff", .85)}{cloud(610, 300, 1.1, "#fff", .8)}{cloud(330, 70, .8, "#fff", .7)}
<!-- холмы и волшебная дорожка -->
<path d="M0 900 Q200 820 400 880 T794 860 L794 1123 L0 1123Z" fill="#E2CDB8"/>
<path d="M0 960 Q260 900 520 950 T794 940 L794 1123 L0 1123Z" fill="#D4B79C"/>
<path d="M330 1123 Q360 1010 400 960 Q430 925 470 905" stroke="#F3E3C6" stroke-width="54" fill="none" stroke-linecap="round"/>
<path d="M330 1123 Q360 1010 400 960 Q430 925 470 905" stroke="#D8B26A" stroke-width="4" fill="none" stroke-dasharray="2 16" stroke-linecap="round"/>
<!-- мечеть вдали -->
<g transform="translate(470 735)" fill="#FBF6F0">
<rect x="0" y="80" width="170" height="95" rx="6"/>
<path d="M40 80 Q40 20 85 8 Q130 20 130 80Z"/><rect x="82" y="-6" width="6" height="16" rx="3" fill="#D8B26A"/>
<rect x="-26" y="20" width="18" height="155" rx="6"/><path d="M-26 22 L-17 -10 L-8 22Z"/>
<rect x="178" y="20" width="18" height="155" rx="6"/><path d="M178 22 L187 -10 L196 22Z"/>
<path d="M68 175 L68 130 Q85 110 102 130 L102 175Z" fill="#5C342E"/>
<path d="M18 150 L18 120 Q28 108 38 120 L38 150Z M132 150 L132 120 Q142 108 152 120 L152 150Z" fill="#C9D3EA"/></g>
{"".join(flower(x, y, s, p) for x, y, s, p in [(60, 1000, 1.3, "#E9C9C0"), (140, 1060, 1, "#fff"), (690, 1010, 1.2, "#EED9A8"), (740, 1070, 1, "#E9C9C0"), (250, 1090, 1.1, "#D3B8A4")])}
</svg>'''
pages.append(f'''<section class="page cover">{cover_bg}
<div class="cover-title">
  <div class="cover-ar" lang="ar" dir="rtl">رِحْلَتِي مَعَ الْقُرْآنِ</div>
  <div class="cover-ru">Моё путешествие<br>к чтению Священного Корана</div>
  <div class="cover-sub">Рабочая книга с играми и прописями · для детей 4–7 лет</div>
</div>
<div class="cover-kids">{adam(220, left="down", right="wave", mood="open")}{maryam(220, left="wave", right="down", mood="smile")}</div>
<div class="cover-badge">Часть 1<br><small>буквы · прописи · огласовки</small></div>
<div class="cover-name">Эта книга принадлежит: <span></span></div>
</section>''')

# ===== 2. ЗНАКОМСТВО ==================================================
phrases = [("أَحْسَنْتَ!", "Молодец!"), ("هَيَّا نَتَعَلَّمُ!", "Давай учиться!"),
           ("بَارَكَ اللَّهُ فِيكَ", "Да благословит тебя Аллах"), ("لِنَقْرَأْ مَعًا", "Давай прочитаем вместе")]
ph = "".join(f'<div class="phrase"><div class="ar ph-ar" lang="ar" dir="rtl">{a}</div><div class="ph-ru">{r}</div></div>' for a, r in phrases)
pages.append(page(f'''
<h1 class="title">Знакомься: твои друзья!</h1>
<div class="meet">
  <div class="meet-card mint">
    <div class="meet-pic">{adam(190, left="down", right="wave", mood="open")}</div>
    <div class="meet-name">{AR("يُوسُفُ")} <b>Юсуф</b></div>
    <p>Любит буквы, задаёт много вопросов и никогда не сдаётся. Он будет проходить задания вместе с тобой!</p>
  </div>
  <div class="meet-card peach">
    <div class="meet-pic">{maryam(190, left="wave", right="down", mood="smile")}</div>
    <div class="meet-name">{AR("زَيْنَبُ")} <b>Зейнеб</b></div>
    <p>Добрая и внимательная. Зейнеб объяснит каждое задание и поможет, если станет трудно.</p>
  </div>
</div>
<h2 class="h2">Волшебные слова Зейнеб и Юсуфа</h2>
<div class="phrases">{ph}</div>
<div class="parents"><b>Для родителей.</b> Занимайтесь 10–15 минут в день. Сначала ребёнок слушает и повторяет за вами,
потом обводит и играет. Ориентир чтения — риваят Хафс от Асима, порядок тем — по логике «Аль-Каида ан-Нурания».
Произношение звуков обязательно показывайте вживую или по аудио: книга не заменяет учителя.</div>
''', num=2))

# ===== 3. КАРТА ПУТЕШЕСТВИЯ ===========================================
stops = [("عَالَمُ الْحُرُوفِ", "Мир букв"), ("كِتَابَةُ الْحُرُوفِ", "Прописи"), ("الْحَرَكَاتُ", "Огласовки"),
         ("السُّكُونُ وَالشَّدَّةُ", "Сукун и шадда"), ("التَّنْوِينُ", "Танвин"), ("الْمَدُّ", "Мадд"),
         ("تَرْكِيبُ الْحُرُوفِ", "Соединяем буквы"), ("أَحْكَامُ التَّجْوِيدِ", "Таджвид"),
         ("نَسْتَعِدُّ لِقِرَاءَةِ الْقُرْآنِ", "Готовимся к Корану"), ("أَنَا صَدِيقُ الْقُرْآنِ", "Я — друг Корана")]
pos = [(150, 930), (395, 960), (630, 890), (590, 745), (340, 725), (135, 625), (290, 500), (560, 515), (610, 360), (360, 290)]
cols = ["#8E9DC6", "#C9D3EA", "#E5BFAE", "#D3B8A4", "#E9C9C0", "#D8B26A", "#8E9DC6", "#C9D3EA", "#E5BFAE", "#D8B26A"]
road = "M" + " L".join(f"{x} {y}" for x, y in pos)
road_smooth = f'<path d="{road}" stroke="#F3E3C6" stroke-width="40" fill="none" stroke-linejoin="round" stroke-linecap="round"/><path d="{road}" stroke="#C9A15B" stroke-width="3.5" fill="none" stroke-dasharray="2 14" stroke-linecap="round" stroke-linejoin="round"/>'
houses = ""
for i, ((x, y), (ar, ru), c) in enumerate(zip(pos, stops, cols), 1):
    houses += (f'<g transform="translate({x} {y})">'
               f'<path d="M-34 0 L-34 -38 Q-34 -64 0 -78 Q34 -64 34 -38 L34 0Z" fill="{c}" stroke="#fff" stroke-width="4"/>'
               f'<path d="M-12 0 L-12 -22 Q0 -34 12 -22 L12 0Z" fill="#fff" opacity=".9"/>'
               f'<circle cx="0" cy="-50" r="14" fill="#fff"/><text x="0" y="-44" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="17" fill="#4A2C27">{i}</text>'
               f'{star(46, -64, 11, "#fff")}'
               f'</g>')
labels = "".join(f'<div class="stop-l" style="left:{x/794*100:.2f}%;top:{(y+10)/1123*100:.2f}%"><span lang="ar" dir="rtl">{ar}</span>{ru}</div>' for (x, y), (ar, ru) in zip(pos, stops))
map_svg = f'''<svg class="map" viewBox="0 0 794 1123" xmlns="http://www.w3.org/2000/svg">
<rect x="34" y="185" width="726" height="870" rx="40" fill="#EFE6DB"/>
{cloud(150, 230, .9, "#fff")}{cloud(640, 620, .8, "#fff")}{cloud(470, 1000, .7, "#fff")}
{"".join(flower(x, y, 1.1, p) for x, y, p in [(80, 760, "#E9C9C0"), (720, 560, "#D3B8A4"), (470, 800, "#EED9A8"), (90, 400, "#fff"), (720, 980, "#E9C9C0")])}
{road_smooth}{houses}</svg>'''
pages.append(f'''<section class="page">{sky_svg()}{map_svg}
<div class="inner"><h1 class="title">Карта нашего путешествия</h1>
<p class="lead">Зейнеб и Юсуф пройдут 10 остановок. За каждую пройденную тему ты получишь звёздочку ⭐ — закрась её прямо на домике!</p></div>
{labels}
<div class="map-kids">{adam(110, right="point")}</div>
<div class="pnum"><svg viewBox="0 0 40 40">{star(20,21,18,"#D8B26A")}</svg><b>3</b></div>
</section>''')

# ===== 4–5. БУКВЫ =====================================================
SEC1 = ("عَالَمُ الْحُرُوفِ", "Раздел 1 · Мир арабских букв", "#8E9DC6")

def letter_page(num, letter, ar_name, ru_name, forms, sound_html, hint, hunt_target, hunt_mix, kid, kid_text):
    big = f'<div class="big-wrap">{arch_frame()}<div class="big-letter" lang="ar" dir="rtl">{letter}</div></div>'
    fm = "".join(f'<div class="form"><div class="ar f-ar" lang="ar" dir="rtl">{f}</div><small>{lab}</small></div>' for f, lab in forms)
    traces = "".join(trace_svg(letter, 120, 120, 150, base=104, y=104) for _ in range(4))
    random.seed(num)
    cells = [hunt_target] * 7 + random.choices(hunt_mix, k=13)
    random.shuffle(cells)
    grid = "".join(f'<div class="hc"><span lang="ar" dir="rtl">{c}</span></div>' for c in cells)
    kidsvg = adam(120, right="point") if kid == "adam" else maryam(120, left="point")
    return page(f'''
<div class="lt-top">
  {big}
  <div class="lt-info">
    <div class="lt-name">{AR(ar_name, "lt-name-ar")}<span>{ru_name}</span></div>
    <div class="sound">{sound_html}</div>
    <div class="hint">{hint}</div>
    <div class="forms">{fm}</div>
    {qr_slot()}
  </div>
</div>
<div class="task"><div class="task-h"><span class="tn">1</span> Обведи букву по пунктиру. Пиши сверху вниз и справа налево.</div>
  <div class="trace-row" dir="rtl">{traces}</div></div>
<div class="task with-kid"><div class="task-h"><span class="tn">2</span> Охота за буквами! Найди и раскрась все буквы {AR(letter, "inl")}</div>
  <div class="hunt" dir="rtl">{grid}</div>
  <div class="kid-side">{kidsvg}{bubble(kid_text, kid, "top")}</div></div>
''', num=num, section=SEC1)

pages.append(letter_page(4, "ا", "أَلِف", "Алиф",
    [("ا", "отдельно"), ("ـا", "в конце")],
    f'Алиф — первая буква. Сам он <b>не звучит</b>: он держит хамзу {AR("ء", "inl")} или удлиняет звук «а».',
    f'С хамзой и огласовкой читаем: {AR("أَ", "inl")} — «а».<br>Алиф — прямая палочка, как стройное дерево 🌴',
    "ا", ["ب", "ت", "ل", "د"], "maryam", "Алиф не соединяется с буквой после себя!"))

pages.append(letter_page(5, "ب", "بَاء", "Ба",
    [("ب", "отдельно"), ("بـ", "в начале"), ("ـبـ", "в середине"), ("ـب", "в конце")],
    'Звук <b>«б»</b>. Губы мягко смыкаются и раскрываются.',
    f'Читаем с огласовкой: {AR("بَ", "inl")} — «ба».<br>Ба — лодочка с <b>одной точкой внизу</b> ⛵',
    "ب", ["ت", "ث", "ن", "ي"], "adam", "Смотри: точка у ба — под лодочкой!"))

# ===== 6. ПОХОЖИЕ БУКВЫ ب ت ث ==========================================
dotless = "ٮ"
def boat(dots, label, color):
    return f'''<div class="boat" style="--bc:{color}">
<div class="boat-l" lang="ar" dir="rtl">{label}</div>
<div class="boat-dots">{dots}</div></div>'''
twins = "".join(boat(d, l, c) for d, l, c in [("1 точка <b>внизу</b>", "ب", "#C9D3EA"), ("2 точки <b>сверху</b>", "ت", "#E9C9C0"), ("3 точки <b>сверху</b>", "ث", "#D8B26A")])
dot_tasks = "".join(f'<div class="dt"><div class="dt-target">{AR(t, "dt-ar")}</div><div class="dt-blank">{trace_svg(dotless, 110, 120, 120, y=78, solid=False)}</div></div>' for t in ["ث", "ب", "ت"])
# лабиринт: путь из ب
random.seed(66)
maze = []
path = {(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5)}
for r in range(5):
    for c in range(6):
        ch = "ب" if (r, c) in path else random.choice(["ت", "ث"])
        maze.append(f'<div class="mz">{AR(ch)}</div>')
pages.append(page(f'''
<h1 class="title sm">Три сестрички-лодочки {AR("ب ت ث", "inl big")}</h1>
<p class="lead">У этих букв одинаковая лодочка. Различаются они только <b>точками</b> — считай их внимательно!</p>
<div class="twins">{twins}</div>
<div class="task"><div class="task-h"><span class="tn">1</span> Расставь точки! Посмотри на букву слева и дорисуй точки на пустой лодочке.</div>
  <div class="dots-row" dir="rtl">{dot_tasks}</div></div>
<div class="task with-kid2"><div class="task-h"><span class="tn">2</span> Лабиринт Юсуфа: шагай только по буквам {AR("ب", "inl")} от старта ▶ до финиша 🏁</div>
  <div class="maze-wrap"><div class="mz-start">старт</div><div class="maze" dir="rtl">{"".join(maze)}</div><div class="mz-end">финиш</div></div>
  <div class="kid-side2">{adam(105, right="wave", mood="open")}</div></div>
<div class="audio-note">🔊 {AR("ت", "inl")} — «т», кончик языка у основания верхних зубов. {AR("ث", "inl")} — «с» межзубная: кончик языка между зубами (как в английском <i>think</i>).</div>
''', num=6, section=SEC1))

# ===== 7. ПРОПИСИ ======================================================
SEC2 = ("كِتَابَةُ الْحُرُوفِ", "Раздел 2 · Мои первые прописи", "#C9D3EA")
def copy_row(letter, n_trace=4, n_free=2, size=100):
    cells = [trace_svg(letter, size, 100, 130, base=92, y=92, solid=True)]
    cells += [trace_svg(letter, size, 100, 130, base=92, y=92) for _ in range(n_trace)]
    cells += [f'<svg viewBox="0 0 100 130" class="tr"><line x1="6" y1="92" x2="94" y2="92" stroke="#C9D0E4" stroke-width="2" stroke-dasharray="3 6"/></svg>' for _ in range(n_free)]
    return f'<div class="copy-row" dir="rtl">{"".join(cells)}</div>'

stroke_demo = f'''<div class="stroke-demo">
<div class="sd"><svg viewBox="0 0 120 150"><text x="60" y="112" text-anchor="middle" font-family="Amiri" font-size="120" fill="#EADFD3">ا</text>
<path d="M62 22 L62 100" stroke="#B5523F" stroke-width="4" marker-end="url(#ar)" stroke-linecap="round"/>
<circle cx="62" cy="20" r="7" fill="#8E9DC6"/><text x="62" y="25" font-size="10" text-anchor="middle" font-family="Nunito" font-weight="900" fill="#fff">1</text>
<defs><marker id="ar" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#B5523F"/></marker></defs></svg>
<p>Алиф: одна линия <b>сверху вниз</b></p></div>
<div class="sd"><svg viewBox="0 0 160 150"><text x="80" y="100" text-anchor="middle" font-family="Amiri" font-size="120" fill="#EADFD3">ب</text>
<path d="M138 58 Q140 86 116 88 L40 88 Q22 86 24 62" stroke="#B5523F" stroke-width="4" fill="none" marker-end="url(#ar2)" stroke-linecap="round"/>
<circle cx="138" cy="52" r="7" fill="#8E9DC6"/><text x="138" y="57" font-size="10" text-anchor="middle" font-family="Nunito" font-weight="900" fill="#fff">1</text>
<circle cx="80" cy="118" r="7" fill="#D3B8A4"/><text x="80" y="122" font-size="10" text-anchor="middle" font-family="Nunito" font-weight="900" fill="#fff">2</text>
<defs><marker id="ar2" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#B5523F"/></marker></defs></svg>
<p>Ба: лодочка <b>справа налево</b>, потом точка</p></div>
<div class="rtl-arrow"><span>Пишем<br>справа налево</span><svg viewBox="0 0 120 40"><path d="M110 20 L14 20" stroke="#8E9DC6" stroke-width="6" stroke-linecap="round"/><path d="M26 6 L10 20 L26 34" stroke="#8E9DC6" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
</div>'''
pages.append(page(f'''
<h1 class="title sm">Пропись: {AR("ا", "inl big")} и {AR("ب", "inl big")}</h1>
{stroke_demo}
<div class="task"><div class="task-h"><span class="tn">1</span> Посмотри на образец, обведи по пунктиру, а в пустых клетках напиши сам.</div>
{copy_row("ا")}{copy_row("ا")}{copy_row("ب")}{copy_row("ب")}</div>
<div class="task"><div class="task-h"><span class="tn">2</span> Буква ба в начале слова: {AR("بـ", "inl")} — обведи хвостики, которые «держатся за руку» со следующей буквой.</div>
{copy_row("بـ", 4, 2, 100)}</div>
''', num=7, section=SEC2))

# ===== 8. ОГЛАСОВКИ: объяснение =======================================
SEC3 = ("الْحَرَكَاتُ", "Раздел 3 · Волшебные огласовки", "#E5BFAE")
hk = [("◌َ", "فَتْحَةٌ", "Фатха", "чёрточка <b>сверху</b>", "«а»", "рот открываем широко", "بَ", "ба", "#F6E1D8"),
      ("◌ِ", "كَسْرَةٌ", "Касра", "чёрточка <b>снизу</b>", "«и»", "уголки губ тянутся в улыбку", "بِ", "би", "#E4E9F4"),
      ("◌ُ", "ضَمَّةٌ", "Дамма", "маленький завиток <b>сверху</b>", "«у»", "губы собираются в трубочку", "بُ", "бу", "#F3EADF")]
hcards = "".join(f'''<div class="hk" style="--hc:{c}">
<div class="hk-sign" lang="ar" dir="rtl">{s}</div>
<div class="hk-name">{AR(a)}<b>{r}</b></div>
<div class="hk-desc">{d}<br>звук {snd}</div>
<div class="hk-ex"><span lang="ar" dir="rtl">{ex}</span><em>{rd}</em></div>
<div class="hk-mouth">👄 {m}</div></div>''' for s, a, r, d, snd, m, ex, rd, c in hk)
pages.append(page(f'''
<h1 class="title sm">Буквы надевают волшебные шапочки</h1>
<p class="lead">Сама по себе буква — только согласный звук. Маленький знак над буквой или под ней говорит, <b>какой гласный</b> добавить. Такие знаки называются <b>огласовками</b> — {AR("الْحَرَكَاتُ", "inl")}</p>
<div class="hks">{hcards}</div>
<div class="say-row">
  <div class="say-kid">{maryam(120, left="point", mood="open")}</div>
  <div class="say">
    <div class="say-h">Прочитай вместе с Зейнеб — справа налево, коротко и чётко:</div>
    <div class="say-line" lang="ar" dir="rtl"><span>بَ</span><span>بِ</span><span>بُ</span></div>
    <div class="say-line" lang="ar" dir="rtl"><span>تَ</span><span>تِ</span><span>تُ</span></div>
    <div class="say-line" lang="ar" dir="rtl"><span>ثَ</span><span>ثِ</span><span>ثُ</span></div>
  </div>
  {qr_slot("Аудио: чтение слогов")}
</div>
<div class="parents sm"><b>Важно:</b> все огласовки — <b>короткие</b>. Читайте на один счёт, без растягивания:
«ба», а не «ба-а-а». Длинные звуки (мадд) появятся позже, в разделе 6.</div>
''', num=8, section=SEC3))

# ===== 9. ОГЛАСОВКИ: упражнения =======================================
left_items = [("«ба»", "#F6E1D8"), ("«би»", "#E4E9F4"), ("«бу»", "#F3EADF")]
right_items = ["بُ", "بَ", "بِ"]
match = "".join(f'<div class="m-row"><div class="m-l" style="background:{c}">{t}<i></i></div><div class="m-gap"></div><div class="m-r"><i></i><span lang="ar" dir="rtl">{a}</span></div></div>' for (t, c), a in zip(left_items, right_items))
choose = [("«ти»", ["تَ", "تِ", "تُ"]), ("«су»*", ["ثُ", "ثِ", "ثَ"]), ("«ба»", ["بِ", "بُ", "بَ"])]
ch_html = "".join(f'<div class="ch"><div class="ch-q">{q}</div><div class="ch-opts" dir="rtl">{"".join(f"<span lang=ar>{o}</span>" for o in opts)}</div></div>' for q, opts in choose)
syl = ["بَ", "تِ", "ثُ", "بُ", "تَ", "ثِ"]
syl_tr = "".join(trace_svg(s, 92, 105, 140, base=96, y=96, pale=True) for s in syl)
pages.append(page(f'''
<h1 class="title sm">Играем с огласовками</h1>
<div class="two-col">
 <div class="task"><div class="task-h"><span class="tn">1</span> Соедини звук со слогом линией.</div><div class="match">{match}</div></div>
 <div class="task"><div class="task-h"><span class="tn">2</span> Помоги Зейнеб найти правильное чтение — обведи кружком.</div>{ch_html}
 <div class="note-s">* «с» межзубная, как в английском <i>think</i></div></div>
</div>
<div class="task"><div class="task-h"><span class="tn">3</span> Обведи серые слоги карандашом — и букву, и огласовку, а потом прочитай их вслух.</div>
 <div class="trace-row" dir="rtl">{syl_tr}</div></div>
<div class="task with-kid"><div class="task-h"><span class="tn">4</span> Найди ошибку Юсуфа! Он прочитал: <b>«ба – би – бу»</b>. Какую букву он перепутал? Зачеркни её.</div>
 <div class="err-line" lang="ar" dir="rtl"><span>بَ</span><span>تِ</span><span>بُ</span></div>
 <div class="kid-side">{adam(110, right="hold", left="down", mood="wink")}{bubble("Ой! Кажется, я не посчитал точки…", "adam", "top")}</div></div>
{reward(9)}
''', num=9, section=SEC3))

# ===== 10. КАРТОЧКИ ===================================================
cards = [("ا", "алиф", "l"), ("ب", "ба", "l"), ("ت", "та", "l"), ("ث", "са", "l"),
         ("◌َ", "фатха · а", "h"), ("◌ِ", "касра · и", "h"), ("◌ُ", "дамма · у", "h"), ("⭐", "звезда-награда", "s"),
         ("بَ", "ба", "y"), ("تِ", "ти", "y"), ("ثُ", "су", "y"), ("بِ", "би", "y")]
cg = "".join(f'<div class="card {k}"><div class="card-in"><div class="c-ar" lang="ar" dir="rtl">{a}</div><div class="c-ru">{r}</div></div></div>' for a, r, k in cards)
pages.append(page(f'''
<div class="cut-head"><div><h1 class="title sm left">Карточки · набор 1</h1>
<p class="lead left">Распечатай на плотной бумаге (200–250 г/м²) и вырежи по пунктиру ✂</p></div>
<div class="games">
<div><b>Игра «Шапочки».</b> Положи букву, рядом карточку огласовки — прочитай слог.</div>
<div><b>Игра «Память».</b> Распечатай лист дважды, переверни карточки и ищи пары.</div>
<div><b>Игра «Поезд».</b> Выложи слоги справа налево и прочитай «поезд».</div></div></div>
<div class="cards">{cg}</div>
''', num=10, cls="cutpage", sky=False))

# ---------------------------------------------------------------- CSS
css = (ROOT / "style.css").read_text(encoding="utf-8")
html = f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Моё путешествие к чтению Священного Корана — часть 1</title>
<style>{css}</style></head><body>{"".join(pages)}</body></html>'''
(ROOT / "book_part1.html").write_text(html, encoding="utf-8")
print("pages:", len(pages))
