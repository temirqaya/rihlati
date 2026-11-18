"""28 картинок-слов (по одной на букву), нарисованы для книги. viewBox 0 0 100 100."""

OUT = "#5C342E"
def _s(body):
    return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="ico">{body}</svg>'
def eyes(x1, x2, y, r=3):
    return (f'<circle cx="{x1}" cy="{y}" r="{r}" fill="{OUT}"/><circle cx="{x2}" cy="{y}" r="{r}" fill="{OUT}"/>'
            f'<circle cx="{x1+1}" cy="{y-1}" r="1" fill="#fff"/><circle cx="{x2+1}" cy="{y-1}" r="1" fill="#fff"/>')
def smile(x, y, w=8):
    return f'<path d="M{x-w/2} {y} q{w/2} {w/2} {w} 0" stroke="{OUT}" stroke-width="2.2" fill="none" stroke-linecap="round"/>'
SW = f'stroke="{OUT}" stroke-width="2.5" stroke-linejoin="round"'

ICONS = {
# лев
"أَسَدٌ": _s(f'<circle cx="50" cy="48" r="34" fill="#C9813F" {SW}/>' + "".join(f'<circle cx="{50+30*__import__("math").cos(a/57.3):.1f}" cy="{48+30*__import__("math").sin(a/57.3):.1f}" r="9" fill="#B5692E"/>' for a in range(0, 360, 30)) +
             f'<circle cx="50" cy="50" r="23" fill="#EFB866" {SW}/>{eyes(42, 58, 46)}<ellipse cx="50" cy="56" rx="5" ry="3.5" fill="{OUT}"/>{smile(50, 61, 10)}<circle cx="31" cy="30" r="6" fill="#EFB866" {SW}/><circle cx="69" cy="30" r="6" fill="#EFB866" {SW}/>'),
# дверь
"بَابٌ": _s(f'<path d="M24 92 V22 Q24 8 50 8 Q76 8 76 22 V92Z" fill="#8B5A3C" {SW}/><path d="M32 86 V26 Q32 16 50 16 Q68 16 68 26 V86Z" fill="#A56C47"/>'
            f'<path d="M50 16 V86" stroke="#7A4A30" stroke-width="2"/><circle cx="60" cy="54" r="3.5" fill="#D8B26A"/><circle cx="40" cy="54" r="3.5" fill="#D8B26A"/><rect x="16" y="90" width="68" height="6" rx="2" fill="#C9A15B"/>'),
# финики
"تَمْرٌ": _s(f'<ellipse cx="50" cy="80" rx="40" ry="10" fill="#E8DCD0" {SW}/>' + "".join(f'<ellipse cx="{x}" cy="{y}" rx="10" ry="15" transform="rotate({r} {x} {y})" fill="#7A3B1E" {SW}/><path d="M{x-3} {y-8} q3 6 0 14" stroke="#A25A30" stroke-width="2" fill="none"/>' for x, y, r in [(32, 62, -30), (50, 58, 0), (68, 62, 30), (40, 45, -15), (60, 45, 15)])),
# тауб (одежда)
"ثَوْبٌ": _s(f'<path d="M36 10 L22 18 L8 40 L20 48 L28 36 L28 92 L72 92 L72 36 L80 48 L92 40 L78 18 L64 10 Q50 20 36 10Z" fill="#FBF6F0" {SW}/><path d="M50 18 V60" stroke="#3E5180" stroke-width="2.5"/>'
            f'<circle cx="50" cy="30" r="2" fill="#C9A15B"/><circle cx="50" cy="40" r="2" fill="#C9A15B"/><circle cx="50" cy="50" r="2" fill="#C9A15B"/><path d="M43 12 Q50 22 57 12" stroke="#3E5180" stroke-width="3" fill="none"/>'),
# верблюд
"جَمَلٌ": _s(f'<path d="M14 58 Q16 40 30 38 Q38 20 48 36 Q56 22 64 38 L72 40 Q74 24 80 20 Q90 18 92 26 L86 30 Q82 40 82 56 Q80 64 72 64 L28 64 Q16 64 14 58Z" fill="#D9A866" {SW}/>'
            f'<path d="M26 64 V90 M36 64 V90 M64 64 V90 M74 64 V90" stroke="#B88544" stroke-width="5" stroke-linecap="round"/><circle cx="86" cy="24" r="2" fill="{OUT}"/><path d="M14 56 q-6 6 -2 14" stroke="#B88544" stroke-width="3" fill="none"/>'),
# кит
"حُوتٌ": _s(f'<path d="M10 56 Q12 30 46 30 Q78 30 80 52 L94 36 L92 70 L80 60 Q72 80 44 80 Q10 80 10 56Z" fill="#6F86C2" {SW}/><path d="M16 62 Q44 74 76 60" fill="#C9D3EA"/>'
            f'{eyes(30, 30, 50, 3.4)}{smile(40, 60, 10)}<path d="M40 28 q-4 -12 4 -18 M40 28 q4 -14 12 -14" stroke="#8E9DC6" stroke-width="3" fill="none" stroke-linecap="round"/>'),
# хлеб
"خُبْزٌ": _s(f'<path d="M12 64 Q8 40 30 34 Q50 26 70 34 Q92 40 88 64 Q86 76 70 76 L30 76 Q14 76 12 64Z" fill="#E0A55B" {SW}/><path d="M28 44 q6 6 0 14 M44 40 q6 6 0 14 M60 40 q6 6 0 14 M74 44 q5 6 0 12" stroke="#C07E36" stroke-width="3" fill="none" stroke-linecap="round"/>'),
# дом
"دَارٌ": _s(f'<path d="M14 46 L50 14 L86 46Z" fill="#A8473B" {SW}/><rect x="22" y="44" width="56" height="46" fill="#F4EBE2" {SW}/><path d="M42 90 V66 Q50 58 58 66 V90Z" fill="#5C342E"/>'
            f'<rect x="28" y="54" width="10" height="10" fill="#C9D3EA" {SW}/><rect x="62" y="54" width="10" height="10" fill="#C9D3EA" {SW}/>'),
# золото
"ذَهَبٌ": _s(f'<path d="M10 80 L22 60 L48 60 L36 80Z M36 80 L48 60 L74 60 L62 80Z M62 80 L74 60 L90 60 L90 80Z" fill="#E8C259" {SW}/><path d="M24 58 L36 38 L62 38 L50 58Z M50 58 L62 38 L80 38 L76 58Z" fill="#F2D378" {SW}/>'
            f'<path d="M58 18 l3 7 7 3 -7 3 -3 7 -3 -7 -7 -3 7 -3z" fill="#fff" stroke="#E8C259" stroke-width="1.5"/>'),
# гранат
"رُمَّانٌ": _s(f'<circle cx="50" cy="56" r="34" fill="#C23B3B" {SW}/><path d="M40 24 L42 14 L46 22 L50 12 L54 22 L58 14 L60 24Z" fill="#C23B3B" {SW}/><path d="M28 48 q4 -14 16 -18" stroke="#E57373" stroke-width="5" fill="none" stroke-linecap="round"/>'),
# оливки
"زَيْتُونٌ": _s(f'<path d="M14 80 Q50 50 90 20" stroke="#7A5A3C" stroke-width="4" fill="none" stroke-linecap="round"/>' + "".join(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="5" transform="rotate({r} {x} {y})" fill="#8BA65A" {SW}/>' for x, y, r in [(30, 58, -50), (54, 40, 20), (70, 26, -40), (44, 70, 10)]) +
                "".join(f'<ellipse cx="{x}" cy="{y}" rx="8" ry="10" fill="#3F4F2A" {SW}/>' for x, y in [(40, 54), (62, 46), (76, 34)])),
# рыба
"سَمَكٌ": _s(f'<path d="M12 50 Q30 22 62 30 Q76 34 80 50 Q76 66 62 70 Q30 78 12 50Z" fill="#F29A4A" {SW}/><path d="M78 50 L94 34 L92 66Z" fill="#F29A4A" {SW}/><path d="M40 32 V68 M54 31 V69" stroke="#fff" stroke-width="5"/>'
            f'{eyes(26, 26, 46, 3.5)}{smile(24, 56, 6)}'),
# солнце
"شَمْسٌ": _s("".join(f'<rect x="47" y="4" width="6" height="16" rx="3" fill="#F2B544" transform="rotate({a} 50 50)"/>' for a in range(0, 360, 45)) + f'<circle cx="50" cy="50" r="26" fill="#F7D774" {SW}/>{eyes(42, 58, 46)}{smile(50, 56, 12)}<circle cx="36" cy="56" r="4" fill="#F4A9A0" opacity=".7"/><circle cx="64" cy="56" r="4" fill="#F4A9A0" opacity=".7"/>'),
# сундук
"صُنْدُوقٌ": _s(f'<rect x="12" y="46" width="76" height="42" rx="4" fill="#9C6B3E" {SW}/><path d="M12 46 Q12 18 50 18 Q88 18 88 46Z" fill="#B57D4B" {SW}/><path d="M30 20 V88 M70 20 V88" stroke="#D8B26A" stroke-width="5"/>'
            f'<rect x="42" y="40" width="16" height="16" rx="3" fill="#D8B26A" {SW}/><circle cx="50" cy="48" r="2.5" fill="{OUT}"/>'),
# лягушка
"ضِفْدَعٌ": _s(f'<ellipse cx="50" cy="62" rx="36" ry="24" fill="#6DBE6A" {SW}/><circle cx="32" cy="36" r="12" fill="#6DBE6A" {SW}/><circle cx="68" cy="36" r="12" fill="#6DBE6A" {SW}/>'
            f'<circle cx="32" cy="36" r="6" fill="#fff"/><circle cx="68" cy="36" r="6" fill="#fff"/><circle cx="33" cy="37" r="3" fill="{OUT}"/><circle cx="69" cy="37" r="3" fill="{OUT}"/>{smile(50, 60, 24)}<ellipse cx="50" cy="76" rx="18" ry="6" fill="#A8DCA2"/>'),
# птица
"طَائِرٌ": _s(f'<ellipse cx="46" cy="56" rx="30" ry="24" fill="#7FB7E6" {SW}/><circle cx="66" cy="38" r="16" fill="#7FB7E6" {SW}/><path d="M80 36 L94 40 L80 44Z" fill="#F2B544" {SW}/>'
            f'<circle cx="70" cy="34" r="3" fill="{OUT}"/><path d="M30 50 Q44 40 54 58 Q40 68 30 50Z" fill="#5A93C9" {SW}/><path d="M18 52 L4 44 L8 62Z" fill="#5A93C9" {SW}/><path d="M42 80 V92 M52 80 V92" stroke="#F2B544" stroke-width="3"/>'),
# конверт
"ظَرْفٌ": _s(f'<rect x="10" y="24" width="80" height="54" rx="4" fill="#FBF6F0" {SW}/><path d="M10 26 L50 56 L90 26" fill="none" {SW}/><path d="M10 78 L40 50 M90 78 L60 50" {SW}/>'
            f'<rect x="70" y="30" width="14" height="16" fill="#E5BFAE" stroke="#A8473B" stroke-width="1.5"/>'),
# виноград
"عِنَبٌ": _s(f'<path d="M50 20 Q52 10 60 6" stroke="#7A5A3C" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M52 18 Q70 8 80 20 Q66 26 52 18Z" fill="#8BA65A" {SW}/>' +
             "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="#7D4E9E" {SW}/>' for x, y in [(34, 30), (50, 28), (66, 30), (42, 44), (58, 44), (34, 58) if False else (26, 44), (74, 44), (50, 58), (34, 58), (66, 58), (42, 72), (58, 72), (50, 86)])),
# облако
"غَيْمٌ": _s(f'<path d="M22 72 Q6 72 8 56 Q10 42 26 44 Q28 24 50 24 Q70 24 74 42 Q92 40 92 58 Q92 72 76 72Z" fill="#DCE6F5" {SW}/>{eyes(42, 60, 52)}{smile(51, 60, 10)}'),
# слон
"فِيلٌ": _s(f'<ellipse cx="54" cy="56" rx="34" ry="26" fill="#A6A9C4" {SW}/><circle cx="28" cy="44" r="18" fill="#A6A9C4" {SW}/><path d="M14 50 Q6 70 16 82" stroke="#A6A9C4" stroke-width="9" fill="none" stroke-linecap="round"/>'
            f'<ellipse cx="40" cy="44" rx="10" ry="14" fill="#C4C6DA" {SW}/><circle cx="24" cy="40" r="2.6" fill="{OUT}"/><path d="M34 78 V92 M48 80 V92 M64 80 V92 M78 76 V92" stroke="#8F92B0" stroke-width="7" stroke-linecap="round"/>'),
# луна
"قَمَرٌ": _s(f'<path d="M62 10 A40 40 0 1 0 90 66 A32 32 0 1 1 62 10Z" fill="#F7D774" {SW}/><circle cx="40" cy="50" r="2.6" fill="{OUT}"/>{smile(44, 60, 8)}<path d="M80 18 l2 5 5 2 -5 2 -2 5 -2 -5 -5 -2 5 -2z" fill="#D8B26A"/>'),
# книга
"كِتَابٌ": _s(f'<path d="M50 24 Q30 14 10 20 V82 Q30 76 50 86 Q70 76 90 82 V20 Q70 14 50 24Z" fill="#3E5180" {SW}/><path d="M50 26 Q32 18 16 24 V76 Q32 72 50 80Z M50 26 Q68 18 84 24 V76 Q68 72 50 80Z" fill="#FBF6F0"/>'
            f'<path d="M22 36 H42 M22 46 H42 M22 56 H38 M58 36 H78 M58 46 H78 M58 56 H74" stroke="#C9A15B" stroke-width="2.5" stroke-linecap="round"/>'),
# лимон
"لَيْمُونٌ": _s(f'<ellipse cx="50" cy="56" rx="36" ry="26" fill="#F5D63D" {SW}/><path d="M86 52 l8 -2 -6 8z M14 60 l-8 2 6 -8z" fill="#F5D63D" {SW}/><path d="M50 30 Q56 16 70 14 Q66 28 50 30Z" fill="#8BA65A" {SW}/><path d="M30 46 q8 -8 18 -8" stroke="#FFF3A6" stroke-width="5" fill="none" stroke-linecap="round"/>'),
# ключ
"مِفْتَاحٌ": _s(f'<circle cx="30" cy="40" r="18" fill="#D8B26A" {SW}/><circle cx="30" cy="40" r="7" fill="#FBF6F0" {SW}/><path d="M44 50 L84 84" stroke="#D8B26A" stroke-width="10" stroke-linecap="round"/><path d="M44 50 L84 84" {SW} fill="none" opacity=".0"/>'
            f'<path d="M70 72 L62 80 M80 80 L72 88" stroke="#D8B26A" stroke-width="8" stroke-linecap="round"/>'),
# пальма
"نَخْلَةٌ": _s(f'<path d="M50 92 Q46 60 52 34" stroke="#9C6B3E" stroke-width="9" fill="none" stroke-linecap="round"/>' + "".join(f'<path d="M52 34 Q{x} {y} {ex} {ey}" stroke="#5E9E4E" stroke-width="7" fill="none" stroke-linecap="round"/>' for x, y, ex, ey in [(30, 18, 10, 34), (74, 18, 92, 34), (40, 8, 26, 12), (64, 8, 80, 12), (52, 14, 52, 6)]) +
                "".join(f'<circle cx="{x}" cy="42" r="4.5" fill="#B5692E"/>' for x in (44, 52, 60))),
# полумесяц
"هِلَالٌ": _s(f'<rect x="0" y="0" width="100" height="100" rx="20" fill="#3E5180"/><path d="M60 14 A36 36 0 1 0 84 74 A28 28 0 1 1 60 14Z" fill="#F7D774"/><path d="M76 26 l2 5 5 2 -5 2 -2 5 -2 -5 -5 -2 5 -2z" fill="#fff"/><circle cx="84" cy="50" r="2" fill="#fff"/>'),
# роза
"وَرْدَةٌ": _s(f'<path d="M50 52 Q48 72 50 94" stroke="#5E9E4E" stroke-width="5" fill="none"/><path d="M50 74 Q66 62 76 70 Q64 82 50 74Z M50 82 Q34 72 26 80 Q38 90 50 82Z" fill="#6DBE6A" {SW}/>'
            f'<circle cx="50" cy="36" r="22" fill="#E06A7E" {SW}/><path d="M50 22 Q62 30 56 42 Q48 48 42 40 Q40 32 50 30" stroke="#B43F55" stroke-width="3" fill="none"/>'),
# рука
"يَدٌ": _s(f'<path d="M30 92 Q22 74 22 56 L22 36 Q22 30 28 30 Q34 30 34 36 V50 V20 Q34 14 40 14 Q46 14 46 20 V48 V14 Q46 8 52 8 Q58 8 58 14 V48 V20 Q58 14 64 14 Q70 14 70 20 V56 L78 46 Q84 40 90 46 Q92 50 88 56 L72 80 Q66 92 56 92Z" fill="#F6DCC6" stroke="#C99A7A" stroke-width="2.5" stroke-linejoin="round"/>'),
}

WORDS = [  # буква, слово, перевод, иконка
    ("ا", "أَسَدٌ", "лев"), ("ب", "بَابٌ", "дверь"), ("ت", "تَمْرٌ", "финики"), ("ث", "ثَوْبٌ", "одежда (тауб)"),
    ("ج", "جَمَلٌ", "верблюд"), ("ح", "حُوتٌ", "кит"), ("خ", "خُبْزٌ", "хлеб"), ("د", "دَارٌ", "дом"),
    ("ذ", "ذَهَبٌ", "золото"), ("ر", "رُمَّانٌ", "гранат"), ("ز", "زَيْتُونٌ", "оливки"), ("س", "سَمَكٌ", "рыба"),
    ("ش", "شَمْسٌ", "солнце"), ("ص", "صُنْدُوقٌ", "сундук"), ("ض", "ضِفْدَعٌ", "лягушка"), ("ط", "طَائِرٌ", "птица"),
    ("ظ", "ظَرْفٌ", "конверт"), ("ع", "عِنَبٌ", "виноград"), ("غ", "غَيْمٌ", "облако"), ("ف", "فِيلٌ", "слон"),
    ("ق", "قَمَرٌ", "луна"), ("ك", "كِتَابٌ", "книга"), ("ل", "لَيْمُونٌ", "лимон"), ("م", "مِفْتَاحٌ", "ключ"),
    ("ن", "نَخْلَةٌ", "пальма"), ("ه", "هِلَالٌ", "полумесяц"), ("و", "وَرْدَةٌ", "роза"), ("ي", "يَدٌ", "рука"),
]

# --- раскраска слова: первая буква (со своими огласовками) — красная, буквы мадда — синие
MARKS = set("ًٌٍَُِّْ")
NONJOIN = set("اأإآدذرزوةء")
def clusters(word):
    out = []
    for ch in word:
        if ch in MARKS and out:
            out[-1] += ch
        else:
            out.append(ch)
    return out

def is_madd(clist, i):
    c = clist[i]
    if i == 0:
        return False
    prev = clist[i-1]
    base = c[0]
    if c[1:] and set(c[1:]) - {"ْ"}:
        return False
    return (base == "ا" and "َ" in prev) or (base == "و" and "ُ" in prev and len(c) == 1) or (base == "ي" and "ِ" in prev and len(c) == 1)

def color_word(word, stretch=True, key=0):
    cl = clusters(word)
    html = ""
    for i, c in enumerate(cl):
        col = "#C23B3B" if i == key else ("#2F8FD8" if is_madd(cl, i) else "#2E1A16")
        tat = ""
        if stretch and i < len(cl) - 1 and c[0] not in NONJOIN:
            tat = "ـــ"
        html += f'<span style="color:{col}">{c}{tat}</span>'
    return html
