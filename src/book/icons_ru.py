"""Карточки-подсказки для русскоязычных детей: буква — русское слово с тем же звуком — картинка.
Для звуков, которых нет в русском, — картинка-подсказка о произношении и пометка «особый звук»."""
from icons import ICONS, OUT, _s, eyes, smile, SW

def tongue_face(bg, heavy=False):
    puff = f'<circle cx="30" cy="62" r="7" fill="#F4A9A0" opacity=".8"/><circle cx="70" cy="62" r="7" fill="#F4A9A0" opacity=".8"/>' if heavy else ""
    return _s(f'<circle cx="50" cy="50" r="46" fill="{bg}"/><circle cx="50" cy="52" r="34" fill="#F6DCC6" stroke="#C99A7A" stroke-width="2.5"/>{eyes(38, 62, 44)}{puff}'
              f'<rect x="36" y="62" width="28" height="7" rx="2" fill="#fff" stroke="#C99A7A" stroke-width="1.5"/><path d="M44 66 Q50 80 56 66Z" fill="#E06A7E" stroke="#B43F55" stroke-width="1.5"/>'
              f'<rect x="36" y="69" width="28" height="5" rx="2" fill="#fff" stroke="#C99A7A" stroke-width="1.5"/>')

NEW = {
"арбуз": _s(f'<path d="M8 40 A42 42 0 0 0 92 40Z" fill="#6DBE6A" {SW}/><path d="M16 40 A34 34 0 0 0 84 40Z" fill="#F4F0D0"/><path d="M20 40 A30 30 0 0 0 80 40Z" fill="#E8505B"/>' + "".join(f'<ellipse cx="{x}" cy="{y}" rx="2" ry="3.5" fill="{OUT}"/>' for x, y in [(36, 50), (50, 56), (64, 50), (44, 62), (58, 62)])),
"бабочка": _s(f'<ellipse cx="30" cy="36" rx="22" ry="20" fill="#E06A7E" {SW}/><ellipse cx="70" cy="36" rx="22" ry="20" fill="#E06A7E" {SW}/><ellipse cx="32" cy="66" rx="16" ry="15" fill="#F2B544" {SW}/><ellipse cx="68" cy="66" rx="16" ry="15" fill="#F2B544" {SW}/>'
              f'<circle cx="30" cy="36" r="6" fill="#fff"/><circle cx="70" cy="36" r="6" fill="#fff"/><rect x="45" y="24" width="10" height="58" rx="5" fill="#5C342E"/><path d="M48 24 Q40 8 34 10 M52 24 Q60 8 66 10" stroke="#5C342E" stroke-width="2.5" fill="none"/>'),
"тюльпан": _s(f'<path d="M50 56 V94" stroke="#5E9E4E" stroke-width="5"/><path d="M50 82 Q30 66 24 76 Q36 92 50 86Z" fill="#6DBE6A" {SW}/><path d="M28 22 L38 34 L50 18 L62 34 L72 22 Q76 56 50 60 Q24 56 28 22Z" fill="#E06A7E" {SW}/>'),
"джем": _s(f'<rect x="22" y="30" width="56" height="62" rx="10" fill="#B43F55" {SW}/><rect x="18" y="18" width="64" height="14" rx="5" fill="#D8B26A" {SW}/><path d="M18 22 L82 22" stroke="#fff" stroke-width="2" stroke-dasharray="4 4"/>'
           f'<rect x="32" y="48" width="36" height="26" rx="5" fill="#FBF6F0"/><circle cx="44" cy="61" r="5" fill="#E06A7E"/><circle cx="56" cy="61" r="5" fill="#E06A7E"/><path d="M50 52 v4" stroke="#5E9E4E" stroke-width="2"/>'),
"стекло": _s(f'<rect x="20" y="10" width="60" height="80" rx="30" fill="#DCE6F5" {SW}/><ellipse cx="50" cy="50" rx="18" ry="12" fill="#fff" opacity=".9"/><text x="50" y="56" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="16" fill="#8E9DC6">х-х</text><path d="M30 24 l10 -6" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'),
"ракета": _s(f'<path d="M50 6 Q72 26 70 64 L30 64 Q28 26 50 6Z" fill="#FBF6F0" {SW}/><circle cx="50" cy="34" r="9" fill="#8E9DC6" {SW}/><path d="M30 50 L16 72 L30 66Z M70 50 L84 72 L70 66Z" fill="#A8473B" {SW}/><path d="M38 64 Q50 96 62 64Z" fill="#F2B544"/><path d="M44 64 Q50 82 56 64Z" fill="#E8505B"/>'),
"зонт": _s(f'<path d="M8 50 Q10 12 50 10 Q90 12 92 50 Q84 42 78 50 Q72 42 64 50 Q57 42 50 50 Q43 42 36 50 Q28 42 22 50 Q16 42 8 50Z" fill="#3E5180" {SW}/><path d="M50 50 V82 Q50 92 40 90" stroke="{OUT}" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M50 10 V50" stroke="#8E9DC6" stroke-width="2"/>'),
"шар": _s(f'<ellipse cx="50" cy="40" rx="28" ry="32" fill="#E8505B" {SW}/><path d="M46 72 L54 72 L50 78Z" fill="#E8505B" {SW}/><path d="M50 78 Q42 88 52 96" stroke="{OUT}" stroke-width="2" fill="none"/><path d="M36 26 q4 -8 12 -10" stroke="#F4A9A0" stroke-width="5" fill="none" stroke-linecap="round"/>'),
"сом": _s(f'<path d="M10 52 Q28 28 60 34 Q76 38 80 52 Q76 66 60 70 Q28 76 10 52Z" fill="#8E9DC6" {SW}/><path d="M78 52 L94 36 L92 68Z" fill="#8E9DC6" {SW}/>{eyes(26, 26, 48, 3.5)}'
         f'<path d="M14 56 Q4 62 2 74 M16 58 Q10 70 12 82" stroke="{OUT}" stroke-width="2.2" fill="none" stroke-linecap="round"/>'),
"дуб": _s(f'<rect x="44" y="56" width="12" height="36" rx="3" fill="#9C6B3E" {SW}/><circle cx="50" cy="38" r="30" fill="#6DBE6A" {SW}/><circle cx="30" cy="48" r="14" fill="#6DBE6A" {SW}/><circle cx="70" cy="48" r="14" fill="#6DBE6A" {SW}/>'
         f'<ellipse cx="40" cy="36" rx="4" ry="5" fill="#B5692E"/><ellipse cx="60" cy="30" rx="4" ry="5" fill="#B5692E"/><path d="M36 31 h8 M56 25 h8" stroke="#7A4A30" stroke-width="3"/>'),
"торт": _s(f'<rect x="16" y="50" width="68" height="38" rx="6" fill="#F3E3C6" {SW}/><path d="M16 60 Q24 68 32 60 Q40 68 50 60 Q60 68 68 60 Q76 68 84 60 V50 H16Z" fill="#E9C9C0" {SW}/><rect x="47" y="30" width="6" height="20" fill="#8E9DC6" {SW}/><path d="M50 18 Q56 26 50 30 Q44 26 50 18Z" fill="#F2B544"/>'),
"ухо": _s(f'<path d="M36 80 Q30 60 30 44 Q30 14 56 14 Q80 14 80 40 Q80 56 66 62 Q58 66 58 76 Q58 90 44 90 Q36 90 36 80Z" fill="#F6DCC6" stroke="#C99A7A" stroke-width="2.5"/><path d="M48 40 Q52 28 62 32 Q68 36 64 46 Q58 52 56 58" stroke="#C99A7A" stroke-width="3" fill="none" stroke-linecap="round"/>'
         f'<path d="M86 30 q6 10 0 20 M92 24 q10 16 0 32" stroke="#8E9DC6" stroke-width="3" fill="none" stroke-linecap="round"/>'),
"стакан": _s(f'<path d="M26 20 L74 20 L68 90 L32 90Z" fill="#DCE6F5" {SW}/><path d="M29 44 L71 44 L68 90 L32 90Z" fill="#8FC3EC"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="#8E9DC6" stroke-width="1.5"/>' for x, y, r in [(42, 72, 4), (56, 62, 3), (48, 54, 2.5), (60, 80, 3.5)]) + '<text x="50" y="14" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="13" fill="#8E9DC6">гр-р</text>'),
"флаг": _s(f'<path d="M24 10 V94" stroke="{OUT}" stroke-width="5" stroke-linecap="round"/><path d="M26 14 Q46 6 60 16 Q74 26 88 18 V54 Q74 62 60 52 Q46 42 26 50Z" fill="#E8505B" {SW}/><circle cx="24" cy="10" r="4" fill="#D8B26A"/>'),
"кубик": _s(f'<path d="M50 10 L88 28 L88 72 L50 90 L12 72 L12 28Z" fill="#F2B544" {SW}/><path d="M12 28 L50 46 L88 28 M50 46 V90" stroke="{OUT}" stroke-width="2.5" fill="none"/><path d="M12 28 L50 10 L88 28 L50 46Z" fill="#F7D774"/>'
           f'<circle cx="50" cy="28" r="4" fill="#A8473B"/><circle cx="30" cy="56" r="4" fill="#3E5180"/><circle cx="70" cy="54" r="4" fill="#3E5180"/><circle cx="70" cy="70" r="4" fill="#3E5180"/>'),
"мяч": _s(f'<circle cx="50" cy="50" r="40" fill="#fff" {SW}/><path d="M10 50 H90" stroke="#3E5180" stroke-width="10"/><path d="M50 10 A40 40 0 0 1 50 90" fill="none" stroke="#E8505B" stroke-width="10" clip-path="circle(40px at 50px 50px)"/><circle cx="50" cy="50" r="40" fill="none" {SW}/>'),
"нота": _s(f'<ellipse cx="32" cy="74" rx="14" ry="10" fill="#3E5180" transform="rotate(-20 32 74)"/><ellipse cx="72" cy="66" rx="14" ry="10" fill="#3E5180" transform="rotate(-20 72 66)"/><path d="M44 70 V18 L84 10 V62" stroke="#3E5180" stroke-width="5" fill="none"/><path d="M44 18 L84 10 L84 22 L44 30Z" fill="#3E5180"/>'),
"очки": _s(f'<circle cx="30" cy="58" r="18" fill="#E4E9F4" {SW}/><circle cx="70" cy="58" r="18" fill="#E4E9F4" {SW}/><path d="M48 56 Q50 50 52 56" stroke="{OUT}" stroke-width="3" fill="none"/><path d="M12 54 L4 44 M88 54 L96 44" {SW}/>'
          f'<ellipse cx="30" cy="58" rx="11" ry="7" fill="#fff" opacity=".9"/><path d="M50 30 Q42 18 50 10 Q58 18 50 30" fill="#C9D3EA" opacity=".8"/><text x="50" y="26" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="10" fill="#8E9DC6">ха</text>'),
"волна": _s(f'<path d="M4 64 Q20 40 36 58 Q44 30 64 34 Q84 38 80 58 Q90 48 96 56 L96 92 L4 92Z" fill="#6F86C2" {SW}/><path d="M4 76 Q24 64 44 76 T96 74" stroke="#C9D3EA" stroke-width="4" fill="none"/><circle cx="66" cy="46" r="5" fill="#fff"/>'),
"яблоко": _s(f'<path d="M50 30 Q30 18 18 36 Q8 56 22 78 Q34 96 50 86 Q66 96 78 78 Q92 56 82 36 Q70 18 50 30Z" fill="#E8505B" {SW}/><path d="M50 30 Q50 18 56 10" stroke="#7A4A30" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M54 18 Q68 8 76 16 Q66 26 54 18Z" fill="#6DBE6A" {SW}/><path d="M30 44 q4 -8 12 -8" stroke="#F4A9A0" stroke-width="5" fill="none" stroke-linecap="round"/>'),
"зубы_с": tongue_face("#C9D3EA"), "зубы_з": tongue_face("#EED9A8"), "зубы_толст": tongue_face("#E9C9C0", heavy=True),
}

# буква, слово (русское), картинка, подсказка (None — звук близок к русскому), особый ли звук
RU = [
    ("ا", "Арбуз", "арбуз", "С хамзой алиф читается «а», как в слове Арбуз", False),
    ("ب", "Бабочка", "бабочка", None, False),
    ("ت", "Тюльпан", "тюльпан", "Тонкое «т»", False),
    ("ث", "Снежинка", "снежинка", "Три точки сверху — как снежинки. Кончик языка чуть-чуть выглядывает между зубками", False),
    ("ج", "Джем", "джем", None, False),
    ("ح", "Стекло", "стекло", "Дыши на стекло из середины горлышка: «х-х», без хрипа", True),
    ("خ", "Хлеб", "خُبْزٌ", "Хрипловатое «х», звук толстый", False),
    ("د", "Дом", "دَارٌ", None, False),
    ("ذ", "Звёздочка", "звёздочка", "Одна точка сверху — как звёздочка. Кончик языка чуть-чуть выглядывает между зубками", False),
    ("ر", "Ракета", "ракета", "Один лёгкий удар языком — не раскатывай", False),
    ("ز", "Зонтик", "зонт", None, False),
    ("س", "Солнце", "شَمْسٌ", "Тонкое свистящее «с»", False),
    ("ش", "Шарик", "шар", None, False),
    ("ص", "Сом", "сом", "Толстое «С» — как в слове «СОм»", True),
    ("ض", "Дуб", "дуб", "Особый толстый звук — слушай учителя", True),
    ("ط", "Торт", "торт", "Толстое «Т» — как в слове «ТОрт»", True),
    ("ظ", "Замок", "замок", "Петелька с палочкой — как башня замка. Толстое «з»", False),
    ("ع", "Ушко", "ухо", "Этого звука нет в русском языке — слушай учителя!", True),
    ("غ", "Горлышко", "стакан", "Как будто полощешь горлышко: «гр-р»", True),
    ("ف", "Флаг", "флаг", None, False),
    ("ق", "Кубик", "кубик", "Глубокое «К» из горлышка — «КУ»", True),
    ("ك", "Кит", "حُوتٌ", "Тонкое, лёгкое «к»", False),
    ("ل", "Лимон", "لَيْمُونٌ", None, False),
    ("م", "Мяч", "мяч", None, False),
    ("ن", "Нота", "нота", None, False),
    ("ه", "Очки", "очки", "Лёгкий выдох, как будто дышишь на очки: «ха-а»", True),
    ("و", "Волна", "волна", "Губы трубочкой, как английское W", True),
    ("ي", "Яблоко", "яблоко", "С фатхой читается «йа» — как в слове Яблоко", False),
]


NEW.update({'снежинка': '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="ico"><circle cx="50" cy="50" r="44" fill="#E4EEF6"/><path d="M50 50 L86.0 50.0" stroke="#53669B" stroke-width="5" stroke-linecap="round"/><path d="M64.0 50.0 L70.9 44.2" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M64.0 50.0 L70.9 55.8" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M74.0 50.0 L80.9 44.2" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M74.0 50.0 L80.9 55.8" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M50 50 L68.0 81.2" stroke="#53669B" stroke-width="5" stroke-linecap="round"/><path d="M57.0 62.1 L65.5 65.2" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M57.0 62.1 L55.4 71.0" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M62.0 70.8 L70.5 73.8" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M62.0 70.8 L60.4 79.6" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M50 50 L32.0 81.2" stroke="#53669B" stroke-width="5" stroke-linecap="round"/><path d="M43.0 62.1 L44.6 71.0" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M43.0 62.1 L34.5 65.2" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M38.0 70.8 L39.6 79.6" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M38.0 70.8 L29.5 73.8" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M50 50 L14.0 50.0" stroke="#53669B" stroke-width="5" stroke-linecap="round"/><path d="M36.0 50.0 L29.1 55.8" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M36.0 50.0 L29.1 44.2" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M26.0 50.0 L19.1 55.8" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M26.0 50.0 L19.1 44.2" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M50 50 L32.0 18.8" stroke="#53669B" stroke-width="5" stroke-linecap="round"/><path d="M43.0 37.9 L34.5 34.8" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M43.0 37.9 L44.6 29.0" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M38.0 29.2 L29.5 26.2" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M38.0 29.2 L39.6 20.4" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M50 50 L68.0 18.8" stroke="#53669B" stroke-width="5" stroke-linecap="round"/><path d="M57.0 37.9 L55.4 29.0" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M57.0 37.9 L65.5 34.8" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M62.0 29.2 L60.4 20.4" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><path d="M62.0 29.2 L70.5 26.2" stroke="#7486BA" stroke-width="3.5" stroke-linecap="round"/><circle cx="50" cy="50" r="6" fill="#fff" stroke="#53669B" stroke-width="3"/></svg>', 'звёздочка': '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="ico"><polygon points="50.0,14.0 60.6,39.4 88.0,41.6 67.1,59.6 73.5,86.4 50.0,72.0 26.5,86.4 32.9,59.6 12.0,41.6 39.4,39.4" fill="#F2C863" stroke="#5C342E" stroke-width="2.5" stroke-linejoin="round"/><circle cx="42" cy="54" r="3" fill="#5C342E"/><circle cx="58" cy="54" r="3" fill="#5C342E"/><path d="M44 62 q6 5 12 0" stroke="#5C342E" stroke-width="2.5" fill="none" stroke-linecap="round"/><circle cx="36" cy="61" r="3.5" fill="#EE9C92" opacity=".7"/><circle cx="64" cy="61" r="3.5" fill="#EE9C92" opacity=".7"/></svg>', 'замок': '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="ico"><path d="M14 90 V42 h8 v-8 h6 v8 h6 v-8 h6 v8 h4 V30 h6 v-8 h6 v8 h6 v-8 h6 v8 h6 V42 h4 v-8 h6 v8 h6 v-8 h6 v8 h8 V90Z" fill="#F6DED5" stroke="#5C342E" stroke-width="2.5" stroke-linejoin="round"/><path d="M42 90 V70 a8 8 0 0 1 16 0 V90" fill="#C9734F" stroke="#5C342E" stroke-width="2.5"/><rect x="47" y="40" width="6" height="10" rx="3" fill="#53669B"/><rect x="22" y="54" width="6" height="9" rx="3" fill="#53669B"/><rect x="72" y="54" width="6" height="9" rx="3" fill="#53669B"/><path d="M50 22 V8 l12 4 l-12 4" fill="#D9998A" stroke="#5C342E" stroke-width="2"/></svg>'})

def icon(key):
    return NEW.get(key) or ICONS[key]

def ru_word(w, special):
    if special and w in ("Язычок", "Ушко", "Горлышко", "Стекло", "Очки"):
        return f'<span class="ruw"><span class="ruw-plain">{w}</span></span>'
    return f'<span class="ruw"><span style="color:#C23B3B">{w[0]}</span>{w[1:]}</span>'
