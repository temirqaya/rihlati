"""Открывашки разделов, раскраски, наклейки-звёздочки, смысл сур, задняя обложка."""
import re
from lib import *

STORIES = {
    1: ("Мир арабских букв", "عَالَمُ الْحُرُوفِ",
        "Однажды утром Зейнеб и Юсуф нашли на полке старую красивую книгу. Они открыли её — и из страниц посыпались буквы! Каждая буква хотела познакомиться и рассказать, как она звучит.",
        "Давай подружимся со всеми 28 буквами!", "Я помогу тебе их различать!"),
    2: ("Мои первые прописи", "كِتَابَةُ الْحُرُوفِ",
        "Буквы так понравились друзьям, что Зейнеб достала карандаши. «Давай научимся их писать!» — сказала она. Оказалось, что по-арабски пишут справа налево.",
        "Держи карандаш крепко — поехали!", "Пиши медленно и красиво!"),
    3: ("Волшебные огласовки", "الْحَرَكَاتُ",
        "На третьей остановке друзей ждал сундучок с волшебными шапочками. Стоило надеть шапочку на букву — и она начинала петь: «ба», «би», «бу»!",
        "Смотри, у букв появились голоса!", "Давай наденем им шапочки!"),
    4: ("Сукун и шадда", "السُّكُونُ وَالشَّدَّةُ",
        "В маленьком домике друзья увидели две особые буквы. Одна сладко спала на подушке-кружочке, а другая всё время повторяла своё имя дважды.",
        "Тише! Буква с сукуном спит.", "А эта — двойняшка!"),
    5: ("Танвин", "التَّنْوِينُ",
        "Дальше дорожка привела к горам. Юсуф крикнул: «Ба-а-ан!» — и горы ответили ему эхом: «н-н-н…». Так друзья узнали про двойные огласовки.",
        "Слышишь эхо? Это танвин!", "Давай поиграем в эхо!"),
    6: ("Мадд", "الْمَدُّ",
        "У широкой реки друзья увидели длинный-длинный мост. «Чтобы перейти, — сказал Юсуф, — нужно тянуть звук, как этот мост: ба-а-а!»",
        "Тянем звук — раз, два!", "Короткий — шажок, длинный — два!"),
    7: ("Соединяем буквы", "تَرْكِيبُ الْحُرُوفِ",
        "Буквы решили взяться за руки и встать в слова. Но шесть букв сказали: «Мы держим руку только той, что стоит перед нами!»",
        "Буквы дружат и держатся за руки!", "А мы читаем первые слова!"),
    8: ("Первые правила таджвида", "أَحْكَامُ التَّجْوِيدِ",
        "На восьмой остановке друзей встретил добрый учитель. Он рассказал, что Коран читают особенно красиво — по правилам таджвида.",
        "Будем читать красиво и правильно!", "Я уже знаю, что такое гунна!"),
    9: ("Готовимся к чтению Корана", "نَسْتَعِدُّ لِقِرَاءَةِ الْقُرْآنِ",
        "Вот и самая важная остановка. Зейнеб и Юсуф вымыли руки, сели спокойно и тихо сказали: «Бисмиллях». Сейчас они прочитают первые суры!",
        "Читаем медленно и с любовью.", "Это особые страницы!"),
    10: ("Я — друг Корана", "أَنَا صَدِيقُ الْقُرْآنِ",
        "Путешествие подходит к концу. Друзья оглянулись на долгую дорожку и улыбнулись: сколько всего они узнали! Теперь они — настоящие друзья Корана.",
        "Ты прошёл весь путь!", "Мы тобой гордимся!"),
}

def opener(book, n, sec):
    title, ar, story, a_say, m_say = STORIES[n]
    dark, light = SECCOL[n]
    house = (f'<svg viewBox="0 0 120 130" class="op-house"><path d="M14 126 V58 Q14 24 60 6 Q106 24 106 58 V126Z" fill="{light}" stroke="{dark}" stroke-width="3"/>'
             f'<path d="M44 126 V92 Q60 76 76 92 V126Z" fill="#fff" stroke="{dark}" stroke-width="2"/><circle cx="60" cy="52" r="20" fill="#fff" stroke="{dark}" stroke-width="2"/>'
             f'<text x="60" y="60" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="22" fill="{dark}">{n}</text>{star(100, 20, 10, GOLD)}</svg>')
    book.pages.append(f'''<section class="page opener" style="--sd:{dark};--sl:{light}">{sky_svg()}
<div class="op-in">
<div class="op-k">Остановка {n}</div>
{house}
<div class="op-ar" lang="ar" dir="rtl">{ar}</div>
<div class="op-t">{title}</div>
<div class="op-line"></div>
<p class="op-story">{story}</p>
<div class="op-kids">
<div class="op-kid"><div class="op-say a">{a_say}</div>{adam(185, right="wave", mood="open")}</div>
<div class="op-kid"><div class="op-say m">{m_say}</div>{maryam(185, left="wave", mood="open")}</div></div>
</div>{book.pnum_html(len(book.pages) + 1)}</section>''')
    book.meta.append(dict(num=len(book.pages), mark=f"OP{n}", h1=f"Остановка {n}", sec=sec))

def install_openers(book):
    orig = book.add
    def add(body, section=None, toc=None, **kw):
        if toc and section:
            m = re.search(r"Раздел (\d+)", section[1])
            if m:
                n = int(m.group(1))
                opener(book, n, section[1])
                book.toc.append((toc, len(book.pages)))
                return orig(body, section=section, toc=None, **kw)
        return orig(body, section=section, toc=toc, **kw)
    book.add = add

# --------------------------------------------------------------- раскраски
def coloring(book, sec):
    from icons_ru import RU, icon
    from data import LETTERS
    pick = [0, 1, 4, 9, 10, 12, 19, 20, 22, 23, 24, 27]   # ا ب ج ر ز ش ف ق ل م ن ي
    for p in range(3):
        cells = ""
        for k in pick[p*4:(p+1)*4]:
            l, w, key, _, _ = RU[k]
            name = LETTERS[k][2]
            cells += (f'<div class="col-c"><svg viewBox="0 0 200 200" class="col-l"><text x="100" y="150" text-anchor="middle" font-family="Amiri" font-weight="700" font-size="190" '
                      f'fill="#fff" stroke="#5C342E" stroke-width="2.5" stroke-linejoin="round">{l}</text></svg>'
                      f'<div class="col-ico">{icon(key)}</div><div class="col-n"><b lang="ar">{l}</b> {name} — {w}</div></div>')
        book.add(f'''<h1 class="title sm">Раскраска букв ({p+1}/3)</h1>
<p class="lead">Раскрась букву и картинку любимыми цветами. Назови букву вслух!</p>
<div class="col-grid">{cells}</div>''', section=sec)

# --------------------------------------------------------------- наклейки
def stickers(book, sec):
    names = ["Мир букв", "Прописи", "Огласовки", "Сукун и шадда", "Танвин", "Мадд", "Соединяем буквы", "Таджвид", "Готовимся к Корану", "Я — друг Корана"]
    big = "".join(f'<div class="stk"><svg viewBox="0 0 100 100">{star(50, 53, 46, ["#F2C14E", "#E9A0B8", "#9FC7E8", "#A8C49A", "#C9A0DC"][i % 5], stroke="#fff")}</svg><b>{i+1}</b><small>{n}</small></div>' for i, n in enumerate(names))
    small = "".join(f'<div class="stk s"><svg viewBox="0 0 100 100">{star(50, 53, 44, ["#F2C14E", "#E9A0B8", "#9FC7E8", "#A8C49A", "#C9A0DC"][i % 5], stroke="#fff")}</svg></div>' for i in range(20))
    book.add(f'''<h1 class="title sm">Мои звёздочки-наклейки</h1>
<p class="lead">Вырежи звёздочку и приклей её на домик на карте, когда пройдёшь остановку. Маленькие звёздочки — за старание!</p>
<div class="stks">{big}</div><div class="stks sm">{small}</div>''', section=sec, cls="cutpage")

# --------------------------------------------------------------- смысл сур
MEANING = {
    1: "Аль-Фатиха — «Открывающая». В ней мы хвалим Аллаха — Господа всех миров, Милостивого и Милосердного, и просим Его вести нас прямым путём. Мусульмане читают её в каждом намазе.",
    112: "Аль-Ихлас — «Искренность». Она рассказывает, что Аллах — Один, у Него нет ни детей, ни родителей и нет никого, подобного Ему.",
    108: "Аль-Каусар — «Изобилие». Аллах подарил Пророку ﷺ огромное благо — райскую реку аль-Каусар. За это мы благодарим Аллаха молитвой.",
    113: "Аль-Фаляк — «Рассвет». В этой суре мы просим Аллаха защитить нас от всякого зла, от темноты ночи и от зависти.",
    114: "Ан-Нас — «Люди». Мы просим защиты у Аллаха — Господа людей — от шайтана, который шепчет плохие мысли.",
    103: "Аль-Аср — «Время». Аллах говорит, что счастливы те, кто верит, делает добрые дела и помогает друг другу в истине и терпении.",
}
def meaning_box(s):
    return f'<div class="mean"><b>О чём эта сура?</b> {MEANING[s]}</div>'

# --------------------------------------------------------------- задняя обложка
def back_cover(book, text, ar="رِحْلَتِي مَعَ الْقُرْآنِ"):
    book.pages.append(f'''<section class="page cover-min back">
<div class="cm-frame"></div>
<div class="cm-in bc-in">
<svg class="cm-moon" viewBox="0 0 60 60"><circle cx="28" cy="30" r="20" fill="#D8B26A"/><circle cx="37" cy="25" r="17" fill="#FBF6F0"/>{star(46, 44, 5, "#D8B26A")}</svg>
<p class="bc-t">{text}</p>
<div class="cm-line"></div>
<div class="bc-kids">{adam(170, right="wave", mood="open")}{maryam(170, left="wave", mood="open")}</div>
<div class="bc-ar" lang="ar" dir="rtl">{ar}</div>
<div class="bc-y">2026</div>
</div></section>''')

CSS = """
.opener{background:linear-gradient(180deg,color-mix(in srgb,var(--sl) 90%,#fff) 0%,#FBF6F0 45%,#FBF6F0 75%,color-mix(in srgb,var(--sl) 80%,#fff) 100%)!important}
.op-in{position:absolute;inset:20mm 22mm 18mm;display:flex;flex-direction:column;align-items:center;text-align:center;z-index:1}
.op-k{font-weight:700;font-size:12.5px;letter-spacing:.3em;text-transform:uppercase;color:#B8914A}
.op-house{width:40mm;margin:6mm 0 3mm}
.op-ar{font-family:"Amiri";font-weight:700;font-size:44px;line-height:1.5;color:var(--sd)}
.op-t{font-weight:800;font-size:26px;color:#5C342E}
.op-line{width:28mm;height:1.5px;background:#D8B26A;margin:5mm 0}
.op-story{font-size:18px;line-height:1.8;color:#4A2C27;max-width:150mm;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:6mm;padding:7mm 9mm;margin-top:3mm}
.op-kids{display:grid;grid-template-columns:1fr 1fr;gap:10mm;margin-top:auto;width:100%}
.op-kid{display:flex;flex-direction:column;align-items:center}
.op-say{position:relative;border-radius:18px;padding:3mm 6mm;font-size:14.5px;font-weight:700;margin-bottom:3mm}
.op-say::after{content:"";position:absolute;bottom:-7px;left:50%;width:13px;height:13px;transform:translateX(-50%) rotate(45deg);background:inherit;border:inherit;border-top:0;border-left:0}
.op-say.a{background:#EEF4E8;border:1.2px solid #C8DABA}.op-say.m{background:#FBEEF1;border:1.2px solid #EFC3CF}
.col-grid{display:grid;grid-template-columns:1fr 1fr;gap:4mm;flex:1}
.col-c{position:relative;background:#fff;border:1px solid #E6D8C6;border-radius:5mm;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:2mm}
.col-l{width:72%;height:auto}
.col-ico{position:absolute;left:4mm;top:4mm;width:30mm;height:30mm;filter:grayscale(1) contrast(.7) brightness(1.4)}
.col-ico .ico{width:100%;height:100%}
.col-n{font-weight:800;font-size:13px;color:#5C342E}
.col-n b{font-family:"Amiri";font-size:20px;color:#3E5180}
.stks{display:grid;grid-template-columns:repeat(5,1fr);gap:0;border-top:1.2px dashed #9C8478;border-left:1.2px dashed #9C8478}
.stk{position:relative;border-right:1.2px dashed #9C8478;border-bottom:1.2px dashed #9C8478;padding:3mm;text-align:center}
.stk svg{width:100%;height:auto}
.stk b{position:absolute;top:36%;left:0;right:0;font-size:22px;font-weight:900;color:#fff}
.stk small{display:block;font-size:10px;font-weight:800;color:#7A5A52}
.stks.sm{grid-template-columns:repeat(10,1fr);margin-top:5mm}
.stk.s{padding:1.5mm}
.mean{background:#FFFDF9;border:1px solid #E6D8C6;border-left:3px solid #D8B26A;border-radius:3mm;padding:2.5mm 5mm;font-size:13px;line-height:1.6;color:#4A2C27}
.mean b{color:#5C342E}
.bc-in{justify-content:center;gap:6mm}
.bc-t{font-size:16px;line-height:1.8;color:#5C342E;max-width:130mm;font-weight:600}
.bc-kids{display:flex;gap:8mm;margin-top:8mm}
.bc-ar{font-family:"Amiri";font-weight:700;font-size:34px;color:#3E5180}
.bc-y{font-size:12px;letter-spacing:.35em;color:#B8914A;font-weight:700}
"""
