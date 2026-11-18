"""Общие элементы вёрстки книги «رِحْلَتِي مَعَ الْقُرْآنِ»."""
import math, random, json, re, pathlib
from chars import adam, maryam

ROOT = pathlib.Path(__file__).parent
IND, CHOC, CREAM, GOLD, GOLD2 = "#3E5180", "#5C342E", "#F4EBE2", "#D8B26A", "#C9A15B"
ROSE, LATTE, SKY, INDL, INK, SOFT, RED = "#E5BFAE", "#D3B8A4", "#C9D3EA", "#8E9DC6", "#4A2C27", "#7A5A52", "#A8473B"

# цвета разделов: (тёмный акцент, светлый фон)
SECCOL = {
    "intro": ("#B8914A", "#F5E8CC"),
    1: ("#5E7F4E", "#DCE8D2"),   # Мир букв — оливковый сад
    2: ("#3E5180", "#DCE2F0"),   # Прописи — индиго
    3: ("#C76A86", "#F6DCE4"),   # Огласовки — роза
    4: ("#4B3A8C", "#E3DDF3"),   # Сукун и шадда — слива
    5: ("#B8914A", "#F5E8CC"),   # Танвин — золото
    6: ("#3F8F86", "#D6ECE8"),   # Мадд — бирюза
    7: ("#C9734F", "#F6E0D3"),   # Соединение — терракота
    8: ("#3C7FB0", "#D8E8F3"),   # Таджвид — небесно-синий
    9: ("#5C342E", "#EFE3D6"),   # Коран — шоколад
    10: ("#8C6BB8", "#EADFF5"),  # Я — друг Корана — лаванда
}

# ---------------------------------------------------------------- Коран
_Q = json.load(open(ROOT / "quran_hafs.json", encoding="utf-8"))

def _clean(t):
    t = t.replace("‏", "").strip()
    # в источнике после открытого фатхатана/дамматана вставлен лишний пробел перед ا/ى
    return re.sub("([ࣰࣱࣲ]) ([اى])", r"\1\2", t)

def ayah(s, v):
    return _clean(_Q[f"{s}:{v}"])

def qwords(s, v, a, b=None):
    """Слова аята s:v с индекса a по b включительно — фрагмент берётся из эталонного текста."""
    w = ayah(s, v).split()
    b = a if b is None else b
    return " ".join(w[a:b + 1])

AR_DIG = "٠١٢٣٤٥٦٧٨٩"
def ar_num(n):
    return "".join(AR_DIG[int(c)] for c in str(n))

SURAH_RU = {1: "аль-Фатиха", 2: "аль-Бакара", 13: "ар-Раад", 22: "аль-Хадж", 23: "аль-Муминун", 103: "аль-Аср",
            104: "аль-Хумаза", 105: "аль-Филь", 108: "аль-Каусар", 109: "аль-Кафирун", 110: "ан-Наср", 111: "аль-Масад",
            112: "аль-Ихлас", 113: "аль-Фаляк", 114: "ан-Нас", 106: "Курайш", 55: "ар-Рахман"}

def qref(s, v):
    return f"сура {SURAH_RU.get(s, s)} ({s}:{v})"

def qfrag(s, v, a, b=None, mark=None):
    t = qwords(s, v, a, b)
    return (f'<div class="qf"><div class="qf-ar" lang="ar" dir="rtl">{t}</div>'
            + (f'<div class="qf-ref">{mark}</div>' if mark else "") + '</div>')

# ---------------------------------------------------------------- декор
def star(x, y, r=8, fill=GOLD, rot=0, stroke=None):
    pts = []
    for i in range(10):
        a = math.pi / 5 * i - math.pi / 2 + rot
        rr = r if i % 2 == 0 else r * 0.45
        pts.append(f"{x + rr*math.cos(a):.1f},{y + rr*math.sin(a):.1f}")
    st = f' stroke="{stroke}" stroke-width="2" stroke-linejoin="round"' if stroke else ""
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"{st}/>'

def cloud(x, y, s=1, fill="#fff", op=1):
    return (f'<g transform="translate({x} {y}) scale({s})" opacity="{op}" fill="{fill}">'
            '<ellipse cx="0" cy="10" rx="46" ry="16"/><circle cx="-18" cy="2" r="18"/>'
            '<circle cx="8" cy="-6" r="24"/><circle cx="30" cy="4" r="16"/></g>')

def crescent(x, y, r=14, fill=GOLD, bg="#fff"):
    return (f'<g><circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>'
            f'<circle cx="{x + r*0.45}" cy="{y - r*0.2}" r="{r*0.85}" fill="{bg}"/></g>')

def flower(x, y, s=1, petal="#E9C9C0", core=GOLD):
    p = "".join(f'<ellipse cx="0" cy="-7" rx="4.5" ry="7" transform="rotate({a})" fill="{petal}"/>' for a in range(0, 360, 72))
    return f'<g transform="translate({x} {y}) scale({s})">{p}<circle r="3.6" fill="{core}"/></g>'

def sky_svg(w=794, h=1123):
    els = [cloud(90, 40, .9, "#fff", .9), cloud(700, 30, 1.1, "#fff", .9)]
    for (x, y, r, c) in [(30, 300, 6, GOLD), (765, 420, 7, "#E9C9C0"), (25, 760, 5, LATTE),
                         (770, 900, 6, GOLD), (40, 1060, 7, INDL), (760, 140, 5, LATTE)]:
        els.append(star(x, y, r, c))
    return f'<svg class="sky" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{"".join(els)}</svg>'

def arch_frame(color=LATTE, fill="#FBF6F0", w=300, h=360):
    d = (f"M14 {h-10} L14 150 Q14 92 {w/2-40} 60 Q{w/2-8} 40 {w/2} 10 "
         f"Q{w/2+8} 40 {w/2+40} 60 Q{w-14} 92 {w-14} 150 L{w-14} {h-10} Z")
    return (f'<svg class="arch" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="8" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="#fff" stroke-width="2.5" stroke-dasharray="1 9" stroke-linecap="round"/>'
            f'{star(w/2, 26, 7, GOLD)}</svg>')

def bubble(text_html, who="adam", side="top"):
    return f'<div class="bubble {who} {side}">{text_html}</div>'

def qr_slot(label="Аудио: произношение"):
    return (f'<div class="qr"><div class="qr-box"><span>QR</span></div>'
            f'<div class="qr-t">{label}<br><small>место для QR-кода<br>(аудио будет добавлено)</small></div></div>')

def reward(text="Закрась звёздочку, когда закончишь!"):
    return f'<div class="reward"><svg viewBox="0 0 40 40" width="34">{star(20,21,17,"#fff",stroke="#B8914A")}</svg><span>{text}</span></div>'

def trace_svg(letter, size=150, w=170, h=200, base=None, solid=False, pale=False, y=None, font="Amiri"):
    y = y if y is not None else h * 0.66
    if solid:
        style = f'fill="{INK}"'
    elif pale:
        style = 'fill="#E2D3C6"'
    else:
        style = 'fill="#F6EEE6" stroke="#8E6F63" stroke-width="2.2" stroke-dasharray="7 5" stroke-linecap="round" stroke-linejoin="round"'
    bl = f'<line x1="6" y1="{base}" x2="{w-6}" y2="{base}" stroke="#C9D0E4" stroke-width="2" stroke-dasharray="3 6"/>' if base else ""
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" class="tr">{bl}'
            f'<text x="{w/2}" y="{y}" text-anchor="middle" direction="rtl" font-family="{font}" font-size="{size}" {style}>{letter}</text></svg>')

def empty_cell(w=100, h=130, base=92):
    return f'<svg viewBox="0 0 {w} {h}" class="tr"><line x1="6" y1="{base}" x2="{w-6}" y2="{base}" stroke="#C9D0E4" stroke-width="2" stroke-dasharray="3 6"/></svg>'

def AR(t, cls=""):
    return f'<span class="ar {cls}" lang="ar" dir="rtl">{t}</span>'

def task(n, head, body, cls=""):
    return f'<div class="task {cls}"><div class="task-h"><span class="tn">{n}</span>{head}</div>{body}</div>'

# ---------------------------------------------------------------- страница
KIDNOTES = [
    ("adam", "У тебя всё получится — я в тебя верю!"),
    ("maryam", "Не спеши. Медленно и правильно — лучше всего!"),
    ("adam", "Ошибся? Ничего страшного, попробуй ещё раз!"),
    ("maryam", "Ты сегодня большой молодец! بَارَكَ اللَّهُ فِيكَ"),
    ("adam", "Каждая буква — шаг к чтению Корана!"),
    ("maryam", "Прочитай ещё раз вслух — так лучше запоминается."),
    ("adam", "Я тоже сначала путал эти буквы. Вместе справимся!"),
    ("maryam", "За каждую прочитанную букву — награда от Аллаха!"),
    ("adam", "Устал? Отдохни немножко и продолжим!"),
    ("maryam", "Как красиво у тебя выходит! أَحْسَنْتَ!"),
    ("adam", "Скажи «Бисмиллях» — и вперёд!"),
    ("maryam", "Я рядом. Если трудно — спроси учителя."),
]

class Book:
    def __init__(self):
        self.pages = []
        self.toc = []
        self.meta = []

    def add(self, body, section=None, cls="", sky=True, raw=False, toc=None, mark=None):
        num = len(self.pages) + 1
        if toc:
            self.toc.append((toc, num))
        m = re.search(r'<h1 class="title[^"]*">(.*?)</h1>', body)
        self.meta.append(dict(num=num, mark=mark, h1=re.sub("<[^>]+>", "", m.group(1)) if m else "", sec=section[1] if section else ""))
        if raw:
            self.pages.append(body.replace("{NUM}", str(num)))
            return num
        footer = f'<div class="pnum"><svg viewBox="0 0 40 40">{star(20,21,18,GOLD)}</svg><b>{num}</b></div>'
        sec = ""
        style = ""
        if section:
            ar, ru, col = section
            if isinstance(col, tuple):
                style = f' style="--sd:{col[0]};--sl:{col[1]}"'
                col = col[1]
            sec = f'<div class="sec" style="--sc:{col}"><span class="sec-ar" lang="ar" dir="rtl">{ar}</span><span class="sec-ru">{ru}</span></div>'
        note = ""
        if 'class="char"' not in body and "cutpage" not in cls and "qpage" not in cls and "nokn" not in cls:
            who, txt = KIDNOTES[num % len(KIDNOTES)]
            txt = re.sub(r"([\u0600-\u06FF][\u0600-\u06FF\s!]*[\u0600-\u06FF!])", r'<span lang="ar" dir="rtl" class="kn-ar">\1</span>', txt)
            k = adam(40, right="wave") if who == "adam" else maryam(40, left="wave")
            note = f'<div class="kidnote {who}">{k}<span class="kn-t">{txt}</span></div>'
            cls += " has-kn"
        self.pages.append(f'<section class="page {cls}"{style}>{sky_svg() if sky else ""}<div class="inner">{sec}{body}</div>{note}{footer}</section>')
        return num

    def pnum_html(self, num):
        return f'<div class="pnum"><svg viewBox="0 0 40 40">{star(20,21,18,GOLD)}</svg><b>{num}</b></div>'

_MARKS = re.compile("[ؐ-ًؚ-ٰٟۖ-ࣰۭ-ࣲـ]")
def bare(w):
    return _MARKS.sub("", w).replace("ٱ", "ا").replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ئ", "ي").replace("ؤ", "و")

def qsel(s, v, first, n=1, nth=1):
    """Фрагмент аята s:v: n слов, начиная со слова, совпадающего (без огласовок) с first."""
    w = ayah(s, v).split()
    k = 0
    for i, x in enumerate(w):
        if bare(x) == bare(first):
            k += 1
            if k == nth:
                return " ".join(w[i:i + n])
    raise ValueError(f"нет слова {first} в {s}:{v}: {ayah(s, v)}")

def qf(s, v, first, n=1, mark=None, nth=1):
    t = qsel(s, v, first, n, nth)
    return (f'<div class="qf"><div class="qf-ar" lang="ar" dir="rtl">{t}</div>'
            + (f'<div class="qf-ref">{mark}</div>' if mark else "") + '</div>')
