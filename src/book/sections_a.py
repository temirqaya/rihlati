"""Обложка, вступление, разделы 1–3."""
import random
from lib import *
from data import LETTERS, TWINS, TWIN_AFTER, forms

SEC1 = ("عَالَمُ الْحُرُوفِ", "Раздел 1 · Мир арабских букв", SECCOL[1])
SEC2 = ("كِتَابَةُ الْحُرُوفِ", "Раздел 2 · Мои первые прописи", SECCOL[2])
SEC3 = ("الْحَرَكَاتُ", "Раздел 3 · Волшебные огласовки", SECCOL[3])

CHEERS = [("أَحْسَنْتَ!", "Ищи внимательно — ты сможешь!"), ("هَيَّا نَتَعَلَّمُ!", "Обводи медленно, не спеши."),
          ("لِنَقْرَأْ مَعًا", "Скажи звук вслух три раза!"), ("بَارَكَ اللَّهُ فِيكَ", "У тебя отлично получается!")]

def cheer(i):
    a, r = CHEERS[i % len(CHEERS)]
    return f'{AR(a, "bub-ar")}<br>{r}'

# ===================================================================== обложка
def cover(book):
    from cover_min import cover as cm
    cm(book, "Рабочая книга для детей")

def meet(book):
    phrases = [("أَحْسَنْتَ!", "Молодец!"), ("هَيَّا نَتَعَلَّمُ!", "Давай учиться!"),
               ("بَارَكَ اللَّهُ فِيكَ", "Да благословит тебя Аллах"), ("لِنَقْرَأْ مَعًا", "Давай прочитаем вместе")]
    ph = "".join(f'<div class="phrase"><div class="ar ph-ar" lang="ar" dir="rtl">{a}</div><div class="ph-ru">{r}</div></div>' for a, r in phrases)
    book.add(f'''
<h1 class="title">Волшебные слова Зейнеб и Юсуфа</h1>
<p class="lead">Эти слова друзья будут говорить тебе в книге. Выучи их — и говори друг другу!</p>
<div class="phrases big">{ph}</div>
<div class="kids-c">{adam(150, right="wave", mood="open")}{maryam(150, left="wave", mood="open")}</div>
<div class="parents"><b>Для родителей.</b> Занимайтесь 10–15 минут в день. Сначала ребёнок слушает и повторяет за вами,
потом обводит и играет. Произношение звуков показывайте вживую — книга не заменяет учителя.</div>''')

def toc_page(book):
    # содержание заполняется в конце сборки
    book.add('''<h1 class="title">Содержание</h1>
<div class="toc">{TOC}</div>
<div class="parents">Страницы с аятами Корана оформлены отдельно от игровых — пожалуйста, относитесь к ним бережно.</div>''')

def map_page(book):
    stops = [("عَالَمُ الْحُرُوفِ", "Мир букв"), ("كِتَابَةُ الْحُرُوفِ", "Прописи"), ("الْحَرَكَاتُ", "Огласовки"),
             ("السُّكُونُ وَالشَّدَّةُ", "Сукун и шадда"), ("التَّنْوِينُ", "Танвин"), ("الْمَدُّ", "Мадд"),
             ("تَرْكِيبُ الْحُرُوفِ", "Соединяем буквы"), ("أَحْكَامُ التَّجْوِيدِ", "Таджвид"),
             ("نَسْتَعِدُّ لِقِرَاءَةِ الْقُرْآنِ", "Готовимся к Корану"), ("أَنَا صَدِيقُ الْقُرْآنِ", "Я — друг Корана")]
    pos = [(150, 930), (395, 960), (630, 890), (590, 745), (340, 725), (135, 625), (290, 500), (560, 515), (610, 360), (360, 290)]
    cols = [SECCOL[i][0] for i in range(1, 11)]
    road = "M" + " L".join(f"{x} {y}" for x, y in pos)
    houses = ""
    for i, ((x, y), c) in enumerate(zip(pos, cols), 1):
        houses += (f'<g transform="translate({x} {y})">'
                   f'<path d="M-34 0 L-34 -38 Q-34 -64 0 -78 Q34 -64 34 -38 L34 0Z" fill="{c}" stroke="#fff" stroke-width="4"/>'
                   f'<path d="M-12 0 L-12 -22 Q0 -34 12 -22 L12 0Z" fill="#fff" opacity=".9"/>'
                   f'<circle cx="0" cy="-50" r="14" fill="#fff"/><text x="0" y="-44" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="17" fill="{INK}">{i}</text>'
                   f'{star(46, -64, 11, "#fff", stroke=GOLD2)}</g>')
    labels = "".join(f'<div class="stop-l" style="left:{x/794*100:.2f}%;top:{(y+10)/1123*100:.2f}%"><span lang="ar" dir="rtl">{ar}</span>{ru}</div>' for (x, y), (ar, ru) in zip(pos, stops))
    svg = f'''<svg class="map" viewBox="0 0 794 1123" xmlns="http://www.w3.org/2000/svg">
<rect x="34" y="185" width="726" height="870" rx="40" fill="#EFE6DB"/>
{cloud(150, 230, .9, "#fff")}{cloud(640, 620, .8, "#fff")}{cloud(470, 1000, .7, "#fff")}
{"".join(flower(x, y, 1.1, p) for x, y, p in [(80, 760, "#E9C9C0"), (720, 560, LATTE), (470, 800, "#EED9A8"), (90, 400, "#fff"), (720, 980, "#E9C9C0")])}
<path d="{road}" stroke="#F3E3C6" stroke-width="40" fill="none" stroke-linejoin="round" stroke-linecap="round"/>
<path d="{road}" stroke="{GOLD2}" stroke-width="3.5" fill="none" stroke-dasharray="2 14" stroke-linecap="round" stroke-linejoin="round"/>{houses}</svg>'''
    book.add(f'''<section class="page">{sky_svg()}{svg}
<div class="inner"><h1 class="title">Карта нашего путешествия</h1>
<p class="lead">Зейнеб и Юсуф пройдут 10 остановок. За каждую пройденную тему ты получишь звёздочку ⭐ — закрась её прямо на домике!</p></div>
{labels}<div class="map-kids">{adam(110, right="point")}</div>{{PNUM}}</section>''', raw=True)
    book.pages[-1] = book.pages[-1].replace("{PNUM}", book.pnum_html(len(book.pages)))

# ===================================================================== раздел 1
def letter_page(book, idx, L):
    letter, ar_name, ru_name, sound, shape, connects = L
    sound = sound.replace("{ء}", AR("ء", "inl")).replace("{أَ}", AR("أَ", "inl"))
    big = f'<div class="big-wrap">{arch_frame()}<div class="big-letter" lang="ar" dir="rtl">{letter}</div></div>'
    fm = "".join(f'<div class="form"><div class="ar f-ar" lang="ar" dir="rtl">{f}</div><small>{lab}</small></div>' for f, lab in forms(letter, connects))
    with_h = "" if letter == "ا" else f' С огласовкой: {AR(letter + "َ", "inl")} {AR(letter + "ِ", "inl")} {AR(letter + "ُ", "inl")}'
    traces = "".join(trace_svg(letter, 120, 130, 150, base=104, y=104) for _ in range(4))
    random.seed(idx * 13)
    group = next((g.split() for g, _, _ in TWINS if letter in g.split()), [])
    pool = [x for x in group if x != letter] + random.sample([l[0] for l in LETTERS if l[0] != letter], 3)
    cells = [letter] * 7 + random.choices(pool, k=13)
    random.shuffle(cells)
    grid = "".join(f'<div class="hc"><span lang="ar" dir="rtl">{c}</span></div>' for c in cells)
    kid = "adam" if idx % 2 else "maryam"
    special = {"ا": "Алиф не соединяется с буквой после себя!", "ب": "Смотри: точка у ба — под лодочкой!"}
    btxt = special.get(letter) or cheer(idx)
    kidsvg = adam(118, right="point") if kid == "adam" else maryam(118, left="point")
    nc = "" if connects else '<div class="nc">Эта буква <b>не соединяется</b> с буквой после себя</div>'
    from games import game_for
    ghead, gbody, _ = game_for(idx, letter, group, [l[0] for l in LETTERS])
    book.add(f'''
<div class="lt-top">{big}
  <div class="lt-info">
    <div class="lt-name">{AR(ar_name, "lt-name-ar")}<span>{ru_name}</span><em>{idx}/28</em></div>
    <div class="sound">{sound}</div>
    <div class="hint">{shape}.{with_h}</div>
    <div class="forms">{fm}</div>{nc}
      </div></div>
{task(1, "Обведи букву по пунктиру. Пиши справа налево.", f'<div class="trace-row" dir="rtl">{traces}</div>')}
{task(2, ghead, f'{gbody}<div class="kid-side">{kidsvg}{bubble(btxt, kid)}</div>', "with-kid")}
''', section=SEC1, toc=("Раздел 1 · Мир арабских букв", SEC1[0]) if idx == 1 else None, mark=f"L{idx}")

def twin_page(book, ti):
    letters_s, base, descs = TWINS[ti]
    letters = letters_s.split()
    cols = [SKY, "#E9C9C0", "#EED9A8"]
    twins = "".join(f'<div class="boat" style="--bc:{cols[i]}"><div class="boat-l" lang="ar" dir="rtl">{l}</div><div class="boat-dots">{d}</div></div>'
                    for i, (l, d) in enumerate(zip(letters, descs)))
    random.seed(100 + ti)
    if base:
        targets = (letters * 2)[:3]
        random.shuffle(targets)
        dt = "".join(f'<div class="dt"><div class="dt-target">{AR(t, "dt-ar")}</div><div class="dt-blank">{trace_svg(base, 100, 120, 130, y=88)}</div></div>' for t in targets)
        t1 = task(1, "Расставь точки! Посмотри на букву и дорисуй точки на пустой фигуре (если они нужны).", f'<div class="dots-row" dir="rtl">{dt}</div>')
    else:
        cells = random.choices(letters, k=16)
        t1 = task(1, f'Раскрась {AR("ق", "inl")} синим, а {AR("ك", "inl")} — коричневым.', '<div class="hunt hunt8" dir="rtl">' + "".join(f'<div class="hc"><span lang="ar">{c}</span></div>' for c in cells) + '</div>')
    target = letters[0] if ti != 1 else "ج"
    others = [l for l in letters if l != target]
    path = {(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5)}
    maze = "".join(f'<div class="mz">{AR(target if (r, c) in path else random.choice(others))}</div>' for r in range(5) for c in range(6))
    kid = adam(105, right="wave", mood="open") if ti % 2 == 0 else maryam(105, left="wave", mood="open")
    t2 = task(2, f'Лабиринт: шагай только по буквам {AR(target, "inl")} от старта до финиша',
              f'<div class="maze-wrap"><div class="mz-start">старт</div><div class="maze" dir="rtl">{maze}</div><div class="mz-end">финиш</div></div><div class="kid-side2">{bubble(["Считай точки — и не ошибёшься!", "Смотри внимательно — у тебя получится!"][ti % 2], "adam" if ti % 2 == 0 else "maryam")}{kid}</div>', "with-kid2")
    names = " · ".join(f'{AR(l, "inl")} — {next(x[2] for x in LETTERS if x[0] == l)}' for l in letters)
    book.add(f'''
<h1 class="title sm">Похожие буквы {AR(letters_s, "inl big")}</h1>
<p class="lead">Эти буквы очень похожи. Внимательно смотри на <b>точки</b> и <b>форму</b>!</p>
<div class="twins n{len(letters)}">{twins}</div>{t1}{t2}
<div class="audio-note">🔊 {names}. Слушай и повторяй за учителем: звуки этих букв разные!</div>''', section=SEC1)

def houses_page(book):
    tiles = "ب ت ث ح خ د ذ ر ز س ش ف ق ن ي ع غ".split()
    random.seed(5); random.shuffle(tiles)
    t = "".join(f'<span lang="ar">{x}</span>' for x in tiles)
    def house(title, col, n):
        return (f'<div class="house" style="--hc:{col}"><svg viewBox="0 0 200 60" class="roof"><path d="M10 58 L100 4 L190 58Z" fill="{col}" stroke="#fff" stroke-width="4"/>{star(100, 36, 9, "#fff")}</svg>'
                f'<div class="house-b"><div class="house-t">{title}</div>' + '<div class="slot"></div>' * n + '</div></div>')
    book.add(f'''
<h1 class="title sm">Домики букв</h1>
<p class="lead">Помоги буквам найти свой домик! Напиши каждую букву в нужный домик.</p>
<div class="tiles" dir="rtl">{t}</div>
<div class="houses">{house("Точки сверху", SKY, 10)}{house("Точки снизу", ROSE, 4)}{house("Без точек", "#EED9A8", 6)}</div>
<div class="row-kids">{maryam(110, left="point")}{bubble(f'Подсказка: у буквы {AR("ي", "inl")} две точки снизу!', "maryam")}</div>''', section=SEC1)

def train_page(book):
    wag = []
    for i, L in enumerate(LETTERS):
        show = i % 3 != 2
        wag.append(f'<div class="wagon{"" if show else " blank"}"><span lang="ar">{L[0] if show else ""}</span><i></i><i></i></div>')
    rows = "".join('<div class="train" dir="rtl">' + ("<div class=\"engine\">🚂</div>" if r == 0 else "") + "".join(wag[r*7:(r+1)*7]) + '</div>' for r in range(4))
    book.add(f'''
<h1 class="title sm">Поезд букв</h1>
<p class="lead">Все 28 букв едут по порядку — справа налево! В некоторых вагонах буквы потерялись. Впиши их!</p>
{rows}
<div class="row-kids">{adam(110, right="wave", mood="open")}{bubble(f'{AR("لِنَقْرَأْ مَعًا", "bub-ar")}<br>Прочитай названия всех букв по порядку!', "adam")}</div>
{reward("Ты прошёл(-ла) весь алфавит! Закрась звёздочку на домике №1 на карте")}''', section=SEC1)

def odd_page(book):
    rows = [("ب ب ت ب"), ("ج ج ج خ"), ("د ذ د د"), ("س ش س س"), ("ص ص ض ص"), ("ع ع ع غ"), ("ق ك ق ق"), ("ن ن ب ن")]
    odd = "".join(f'<div class="odd-row" dir="rtl">' + "".join(f'<span lang="ar">{x}</span>' for x in r.split()) + '</div>' for r in rows)
    parts = [("ٮ", "• • •  сверху", ["ث", "ت", "ب"]), ("ح", "•  сверху", ["ج", "خ", "ح"]), ("ر", "•  сверху", ["ز", "ر", "ذ"]), ("ى", "• •  снизу", ["ي", "ت", "ن"])]
    build = "".join(f'<div class="build"><span class="b-base" lang="ar">{b}</span><b>+</b><span class="b-dots">{d}</span><b>=</b><div class="ch-opts" dir="rtl">' +
                    "".join(f'<span lang="ar">{o}</span>' for o in opts) + '</div></div>' for b, d, opts in parts)
    book.add(f'''
<h1 class="title sm">Найди лишнюю и собери букву</h1>
{task(1, "Найди лишнюю букву в каждом ряду и зачеркни её.", f'<div class="odd-grid">{odd}</div>')}
{task(2, "Собери букву из частей: фигура + точки. Обведи правильный ответ.", f'<div class="builds">{build}</div>', "with-kid3")}
<div class="row-kids">{maryam(105, left="wave")}{bubble(cheer(0), "maryam")}</div>''', section=SEC1)

def picture_alphabet(book):
    from icons_ru import RU, icon, ru_word
    for p in range(2):
        cells = ""
        for l, w, key, hint, special in RU[p*14:(p+1)*14]:
            name = next(x[2] for x in LETTERS if x[0] == l)
            tag = '<i class="pa-sp">⚠ особый звук</i>' if special else ""
            cells += (f'<div class="pa{" sp" if special else ""}"><div class="pa-w"><b lang="ar">{l}</b> {name} — {ru_word(w, special)}</div>'
                      f'<div class="pa-box">{trace_svg(l, 92, 120, 120, y=82)}<div class="pa-ico">{icon(key)}</div>{tag}</div><small>{hint or "&nbsp;"}</small></div>')
        book.add(f'''<h1 class="title sm">Алфавит с картинками ({p+1}/2)</h1>
<p class="lead">Буква — и русское слово-подсказка с похожим звуком. Обведи букву в рамке. ⚠ — такого звука нет в русском языке: картинка подсказывает, <b>как</b> его сказать. Слушай учителя!</p>
<div class="pa-grid" dir="rtl">{cells}</div>''', section=SEC1)

def section1(book):
    for i, L in enumerate(LETTERS, 1):
        letter_page(book, i, L)
        if L[0] in TWIN_AFTER:
            twin_page(book, TWIN_AFTER[L[0]])
    picture_alphabet(book)
    from extras import coloring
    coloring(book, SEC1)
    houses_page(book)
    odd_page(book)
    train_page(book)

# ===================================================================== раздел 2
def copy_row(letter, n_trace=4, n_free=1, size=96):
    cells = [trace_svg(letter, size, 100, 130, base=92, y=92, solid=True)]
    cells += [trace_svg(letter, size, 100, 130, base=92, y=92) for _ in range(n_trace)]
    cells += [empty_cell() for _ in range(n_free)]
    return f'<div class="copy-row" dir="rtl">{"".join(cells)}</div>'

def stroke_demo():
    mk = lambda i: f'<defs><marker id="ar{i}" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#B5523F"/></marker></defs>'
    num = lambda x, y, n, c: f'<circle cx="{x}" cy="{y}" r="7" fill="{c}"/><text x="{x}" y="{y+4}" font-size="10" text-anchor="middle" font-family="Nunito" font-weight="900" fill="#fff">{n}</text>'
    return f'''<div class="stroke-demo">
<div class="sd"><svg viewBox="0 0 120 150">{mk(1)}<text x="60" y="112" text-anchor="middle" font-family="Amiri" font-size="120" fill="#EADFD3">ا</text>
<path d="M62 22 L62 100" stroke="#B5523F" stroke-width="4" marker-end="url(#ar1)" stroke-linecap="round"/>{num(62, 20, 1, IND)}</svg>
<p>Алиф: одна линия <b>сверху вниз</b></p></div>
<div class="sd"><svg viewBox="0 0 160 150">{mk(2)}<text x="80" y="100" text-anchor="middle" font-family="Amiri" font-size="120" fill="#EADFD3">ب</text>
<path d="M138 58 Q140 86 116 88 L40 88 Q22 86 24 62" stroke="#B5523F" stroke-width="4" fill="none" marker-end="url(#ar2)" stroke-linecap="round"/>{num(138, 52, 1, IND)}{num(80, 118, 2, CHOC)}</svg>
<p>Ба: лодочка <b>справа налево</b>, потом точка</p></div>
<div class="rtl-arrow"><span>Пишем<br>справа налево</span><svg viewBox="0 0 120 40"><path d="M110 20 L14 20" stroke="{IND}" stroke-width="6" stroke-linecap="round"/><path d="M26 6 L10 20 L26 34" stroke="{IND}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div>'''

def section2(book):
    groups = [LETTERS[i:i+4] for i in range(0, 28, 4)]
    for gi, g in enumerate(groups):
        rows = ""
        for L in g:
            rows += copy_row(L[0])
            if L[5] and L[0] != "ا":
                rows += copy_row(L[0] + "ـ", 3, 2)
            else:
                rows += copy_row(L[0], 2, 3)
        head = " ".join(AR(L[0], "inl big") for L in g)
        intro = stroke_demo() if gi == 0 else f'<p class="lead">Первая клетка — образец. Обведи по пунктиру, а в пустых клетках напиши сам. Вторая строка — та же буква в начале слова.</p>'
        book.add(f'''<h1 class="title sm">Пропись: {head}</h1>{intro}
{task(1, "Образец → обведи → напиши сам. Не забывай про точки!", rows)}''', section=SEC2, cls="nokn", toc=("Раздел 2 · Мои первые прописи", SEC2[0]) if gi == 0 else None)
    # формы букв
    sets = [["ب", "ج", "س", "ص", "ع", "ف", "ق"], ["ك", "ل", "م", "ن", "ه", "ي", "ط"]]
    for si, s in enumerate(sets):
        rows = ""
        for l in s:
            fs = [l, l + "ـ", "ـ" + l + "ـ", "ـ" + l]
            rows += '<div class="forms-row" dir="rtl">' + "".join(
                f'<div class="fr-c">{trace_svg(f, 84, 110, 120, base=82, y=82, pale=True)}<small>{lab}</small></div>' for f, lab in zip(fs, ["отдельно", "в начале", "в середине", "в конце"])) + '</div>'
        kid = adam(100, right="point") if si == 0 else maryam(100, left="point")
        book.add(f'''<h1 class="title sm">Одна буква — четыре платья</h1>
<p class="lead">В слове буква меняет «платье»: в начале, в середине и в конце она выглядит чуть иначе. Обведи серые буквы карандашом.</p>
{task(1, "Обведи каждую форму. Смотри: справа — отдельная буква, слева — буква в конце слова.", rows)}
<div class="row-kids">{kid}{bubble("Голова буквы остаётся той же — меняется только хвостик!", "adam" if si == 0 else "maryam")}</div>''', section=SEC2)
    # расставь точки
    items = [("ٮ", "Ба"), ("ٮ", "Та"), ("ٮ", "Са"), ("ح", "Джим"), ("ح", "Хо"), ("د", "Заль"), ("ر", "Зайн"), ("س", "Шин"),
             ("ص", "Дад"), ("ط", "За"), ("ع", "Гайн"), ("ڡ", "Фа"), ("ٯ", "Каф"), ("ں", "Нун"), ("ى", "Йе")]
    cells = "".join(f'<div class="dotc">{trace_svg(b, 92, 120, 120, y=78)}<b>{n}</b></div>' for b, n in items)
    book.add(f'''<h1 class="title sm">Игра «Расставь точки»</h1>
<p class="lead">Буквы потеряли свои точки! Прочитай название буквы под фигурой и дорисуй нужные точки — сверху, снизу или внутри.</p>
<div class="dotgrid" dir="rtl">{cells}</div>
<div class="row-kids">{adam(105, right="wave", mood="open")}{bubble("Одна точка лишняя — и буква уже другая!", "adam")}</div>
{reward("Прописи пройдены! Закрась звёздочку на домике №2")}''', section=SEC2)

# ===================================================================== раздел 3
def section3(book):
    hk = [("◌َ", "فَتْحَةٌ", "Фатха", "чёрточка <b>сверху</b>", "«а»", "рот открываем широко", "بَ", "ба", "#F6E1D8"),
          ("◌ِ", "كَسْرَةٌ", "Касра", "чёрточка <b>снизу</b>", "«и»", "уголки губ тянутся в улыбку", "بِ", "би", "#E4E9F4"),
          ("◌ُ", "ضَمَّةٌ", "Дамма", "маленький завиток <b>сверху</b>", "«у»", "губы собираются в трубочку", "بُ", "бу", "#F3EADF")]
    hcards = "".join(f'''<div class="hk" style="--hc:{c}"><div class="hk-sign" lang="ar" dir="rtl">{s}</div>
<div class="hk-name">{AR(a)}<b>{r}</b></div><div class="hk-desc">{d}<br>звук {snd}</div>
<div class="hk-ex"><span lang="ar" dir="rtl">{ex}</span><em>{rd}</em></div><div class="hk-mouth">👄 {m}</div></div>''' for s, a, r, d, snd, m, ex, rd, c in hk)
    book.add(f'''<h1 class="title sm">Буквы надевают волшебные шапочки</h1>
<p class="lead">Сама по себе буква — только согласный звук. Маленький знак над буквой или под ней говорит, <b>какой гласный</b> добавить. Эти знаки — <b>огласовки</b>, {AR("الْحَرَكَاتُ", "inl")}</p>
<div class="hks">{hcards}</div>
<div class="say-row"><div class="say-kid">{maryam(120, left="point", mood="open")}</div>
  <div class="say"><div class="say-h">Прочитай вместе с Зейнеб — справа налево, коротко и чётко:</div>
    <div class="say-line" lang="ar" dir="rtl"><span>بَ</span><span>بِ</span><span>بُ</span></div>
    <div class="say-line" lang="ar" dir="rtl"><span>تَ</span><span>تِ</span><span>تُ</span></div>
    <div class="say-line" lang="ar" dir="rtl"><span>ثَ</span><span>ثِ</span><span>ثُ</span></div></div>
  </div>
<div class="parents sm"><b>Важно:</b> все огласовки — <b>короткие</b>. Читайте на один счёт: «ба», а не «ба-а-а». Длинные звуки (мадд) — в разделе 6.</div>''',
             section=SEC3, toc=("Раздел 3 · Волшебные огласовки", SEC3[0]))
    # таблицы слогов
    rows_all = [("أ", "Алиф (хамза)")] + [(L[0], L[2]) for L in LETTERS[1:]]
    for part in range(2):
        rows = rows_all[part*14:(part+1)*14]
        tb = "".join(f'<div class="syl-row" dir="rtl"><span class="syl-l">{l}</span><span>{l}َ</span><span>{l}ِ</span><span>{l}ُ</span><em>{n}</em></div>' for l, n in rows)
        book.add(f'''<h1 class="title sm">Читаем слоги: {AR("◌َ ◌ِ ◌ُ", "inl")} ({part+1}/2)</h1>
<p class="lead">Читай каждую строку справа налево: сначала букву, потом три слога. Учитель показывает — ты повторяешь.</p>
<div class="syl-table" lang="ar">{tb}</div>
<div class="tbl-foot"><div class="checks">Прочитал(-а): <span>☐ 1 раз</span><span>☐ 2 раза</span><span>☐ 3 раза</span></div></div>''', section=SEC3)
    # упражнения 1 (из пилота)
    left_items = [("«ба»", "#F6E1D8"), ("«би»", "#E4E9F4"), ("«бу»", "#F3EADF")]
    match = "".join(f'<div class="m-row"><div class="m-l" style="background:{c}">{t}<i></i></div><div class="m-gap"></div><div class="m-r"><i></i><span lang="ar" dir="rtl">{a}</span></div></div>' for (t, c), a in zip(left_items, ["بُ", "بَ", "بِ"]))
    choose = [("«ти»", ["تَ", "تِ", "تُ"]), ("«су»*", ["ثُ", "ثِ", "ثَ"]), ("«ба»", ["بِ", "بُ", "بَ"])]
    ch_html = "".join(f'<div class="ch"><div class="ch-q">{q}</div><div class="ch-opts" dir="rtl">{"".join(f"<span lang=ar>{o}</span>" for o in opts)}</div></div>' for q, opts in choose)
    syl_tr = "".join(trace_svg(s, 92, 105, 140, base=96, y=96, pale=True) for s in ["بَ", "تِ", "ثُ", "بُ", "تَ", "ثِ"])
    book.add(f'''<h1 class="title sm">Играем с огласовками</h1>
<div class="two-col">{task(1, "Соедини звук со слогом линией.", f'<div class="match">{match}</div>')}
{task(2, "Помоги Зейнеб найти правильное чтение — обведи кружком.", ch_html + '<div class="note-s">* межзубное «с», как в английском <i>think</i></div>')}</div>
{task(3, "Обведи серые слоги карандашом — и букву, и огласовку, а потом прочитай их вслух.", f'<div class="trace-row" dir="rtl">{syl_tr}</div>')}
{task(4, "Найди ошибку Юсуфа! Он прочитал: <b>«ба – би – бу»</b>. Какую букву он перепутал? Зачеркни её.",
      f'<div class="err-line" lang="ar" dir="rtl"><span>بَ</span><span>تِ</span><span>بُ</span></div><div class="kid-side">{adam(110, right="hold", left="down", mood="wink")}{bubble("Ой! Кажется, я не посчитал точки…", "adam")}</div>', "with-kid")}''', section=SEC3)
    # упражнения 2
    same = [["جَ", "جُ", "جَ", "جِ"], ["خِ", "خَ", "حِ", "خِ"], ["دُ", "ذُ", "دُ", "دَ"], ["سَ", "شَ", "سِ", "سَ"]]
    same_h = "".join('<div class="odd-row sm" dir="rtl">' + "".join(f'<span lang="ar">{x}</span>' for x in r) + '</div>' for r in same)
    seq = "".join(f'<div class="seq"><span>{n}</span><div class="seq-cells" dir="rtl">' + "".join(f'<i lang="ar">{x}</i>' for x in cs) + '</div></div>'
                  for n, cs in [("ф → к → д", ["رُ", "رَ", "رِ"]), ("ф → к → д", ["مِ", "مُ", "مَ"]), ("ф → к → д", ["نَ", "نُ", "نِ"])])
    sign = "".join(f'<div class="ch"><div class="ch-q">{q}</div><div class="ch-opts" dir="rtl">' + "".join(f'<span lang=ar>{o}</span>' for o in ["◌َ", "◌ِ", "◌ُ"]) + '</div></div>' for q in ["«ли»", "«ку»", "«фа»"])
    book.add(f'''<h1 class="title sm">Огласовки: тренируемся</h1>
{task(1, "Найди <b>два одинаковых</b> слога в каждом ряду и соедини их дугой.", f'<div class="odd-grid">{same_h}</div>')}
<div class="two-col">{task(2, "Правильная очередь: подпиши под слогами 1, 2, 3 — сначала фатха, потом касра, потом дамма.", seq)}
{task(3, "Помоги Зейнеб найти правильный знак для звука — обведи.", sign)}</div>
<div class="row-kids">{maryam(105, left="wave", mood="open")}{bubble(cheer(3), "maryam")}</div>''', section=SEC3)
    # колесо огласовок
    wl = "ب ت ث ج ح خ د ذ ر ز س ش".split()
    import math
    lettxt = ""
    for i, l in enumerate(wl):
        a = -math.pi/2 + i * 2*math.pi/len(wl)
        x, y = 160 + 118*math.cos(a), 160 + 118*math.sin(a)
        lettxt += f'<text x="{x:.1f}" y="{y+13:.1f}" text-anchor="middle" font-family="Amiri" font-weight="700" font-size="38" fill="{INK}">{l}</text>'
    sectors = "".join(f'<path d="M160 160 L{160+150*math.cos(-math.pi/2+(i-.5)*2*math.pi/12):.1f} {160+150*math.sin(-math.pi/2+(i-.5)*2*math.pi/12):.1f} A150 150 0 0 1 {160+150*math.cos(-math.pi/2+(i+.5)*2*math.pi/12):.1f} {160+150*math.sin(-math.pi/2+(i+.5)*2*math.pi/12):.1f}Z" fill="{[SKY, "#F6E1D8", "#F3EADF"][i % 3]}"/>' for i in range(12))
    bottom = f'<svg viewBox="0 0 320 320" class="wheel"><circle cx="160" cy="160" r="156" fill="#fff" stroke="#9C8478" stroke-width="2" stroke-dasharray="6 5"/>{sectors}{lettxt}<circle cx="160" cy="160" r="5" fill="{INK}"/></svg>'
    top = f'''<svg viewBox="0 0 320 320" class="wheel"><circle cx="160" cy="160" r="156" fill="#FBF6F0" stroke="#9C8478" stroke-width="2" stroke-dasharray="6 5"/>
<circle cx="160" cy="160" r="140" fill="none" stroke="{LATTE}" stroke-width="6"/>
<rect x="128" y="10" width="64" height="62" rx="12" fill="#fff" stroke="{RED}" stroke-width="2.5" stroke-dasharray="5 4"/>
<text x="160" y="46" text-anchor="middle" font-family="Nunito" font-size="11" font-weight="800" fill="{RED}">вырежи окошко</text>
<text x="104" y="52" text-anchor="middle" font-family="Amiri" font-size="42" fill="{RED}">◌َ</text>
<text x="216" y="52" text-anchor="middle" font-family="Amiri" font-size="42" fill="{RED}">◌ُ</text>
<text x="160" y="118" text-anchor="middle" font-family="Amiri" font-size="42" fill="{RED}">◌ِ</text>
<text x="160" y="190" text-anchor="middle" font-family="Nunito" font-size="15" font-weight="900" fill="{INK}">Колесо огласовок</text>
<text x="160" y="212" text-anchor="middle" font-family="Amiri" font-size="22" font-weight="700" fill="{IND}">عَجَلَةُ الْحَرَكَاتِ</text>
{star(160, 250, 14, GOLD)}<circle cx="160" cy="160" r="5" fill="{INK}"/></svg>'''
    book.add(f'''<h1 class="title sm">Колесо огласовок — сделай сам!</h1>
<div class="wheels"><div>{bottom}<p>Нижний круг — с буквами</p></div><div>{top}<p>Верхний круг — с окошком</p></div></div>
<div class="howto"><b>Как собрать:</b> 1) вырежи оба круга и окошко; 2) положи верхний круг на нижний
и скрепи в центре кнопкой-гвоздиком; 3) крути колесо: в окошке появляется буква — прочитай её с фатхой, касрой и даммой.
<br><b>Пример:</b> в окошке {AR("ج", "inl")} — читаем {AR("جَ", "inl")} {AR("جِ", "inl")} {AR("جُ", "inl")}.</div>
{reward("Огласовки пройдены! Закрась звёздочку на домике №3")}''', section=SEC3, cls="cutpage-l")
