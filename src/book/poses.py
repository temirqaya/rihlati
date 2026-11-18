"""Позы намаза (вид сбоку) в стиле Зейнеб и Юсуфа + иконки абдеста."""
SK, SKD, OUT = "#F6DCC6", "#E8BFA2", "#6B4238"

def _head(x, y, girl, r=15):
    if girl:
        return (f'<circle cx="{x}" cy="{y}" r="{r+5}" fill="#6C7FB4" stroke="#3E5180" stroke-width="2"/>'
                f'<ellipse cx="{x+5}" cy="{y+1}" rx="{r-4}" ry="{r-3}" fill="{SK}"/><circle cx="{x+9}" cy="{y-1}" r="1.8" fill="{OUT}"/>')
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SK}" stroke="{SKD}" stroke-width="1.5"/>'
            f'<path d="M{x-r} {y-3} Q{x-r} {y-r-6} {x} {y-r-6} Q{x+r} {y-r-6} {x+r} {y-3}Z" fill="#fff" stroke="{OUT}" stroke-width="1.5"/>'
            f'<path d="M{x-r+1} {y-5} H{x+r-1}" stroke="#3E5180" stroke-width="2.5"/><circle cx="{x+8}" cy="{y+1}" r="1.8" fill="{OUT}"/>'
            f'<path d="M{x-r} {y-1} q-2 6 2 10" stroke="#5C342E" stroke-width="3" fill="none"/>')

def _robe(girl):
    return ("#D9A291", "#B87C6C") if girl else ("#FBF4EA", "#C9B39C")

def pose(kind, girl=False, w=110):
    c, cd = _robe(girl)
    s = f'stroke="{cd}" stroke-width="2" stroke-linejoin="round"'
    hand = lambda x, y: f'<circle cx="{x}" cy="{y}" r="5.5" fill="{SK}" stroke="{SKD}" stroke-width="1.2"/>'
    mat = '<rect x="6" y="152" width="108" height="8" rx="3" fill="#A8C49A"/><path d="M14 156 H106" stroke="#fff" stroke-width="1.2" stroke-dasharray="3 4"/>'
    if kind == "stand":            # кыям
        g = (f'<path d="M48 64 Q60 58 72 64 L76 150 H44Z" fill="{c}" {s}/>' + _head(60, 46, girl)
             + (f'<path d="M58 78 Q66 92 64 96" stroke="{cd}" stroke-width="9" fill="none" stroke-linecap="round"/>{hand(64, 96 if not girl else 82)}' if not girl else f'<path d="M58 72 Q68 80 66 82" stroke="{cd}" stroke-width="9" fill="none" stroke-linecap="round"/>{hand(66, 82)}'))
    elif kind == "takbir":         # такбир
        g = (f'<path d="M48 64 Q60 58 72 64 L76 150 H44Z" fill="{c}" {s}/>' + _head(60, 46, girl)
             + f'<path d="M60 70 Q74 62 72 {46 if not girl else 58}" stroke="{cd}" stroke-width="9" fill="none" stroke-linecap="round"/>{hand(72, 44 if not girl else 58)}')
    elif kind == "ruku":           # руку
        g = (f'<path d="M40 150 L44 96 Q46 86 56 84 L98 80 Q104 86 98 94 L60 100 L58 150Z" fill="{c}" {s}/>'
             + _head(104, 86, girl, 13) + f'<path d="M66 92 L70 124" stroke="{cd}" stroke-width="8" stroke-linecap="round"/>{hand(70, 126)}')
    elif kind == "sajda":          # саджда
        g = (f'<path d="M22 150 Q20 120 36 112 Q50 106 70 116 L92 136 Q96 146 88 150Z" fill="{c}" {s}/>'
             + _head(96, 140, girl, 12) + f'<path d="M76 128 L82 148" stroke="{cd}" stroke-width="8" stroke-linecap="round"/>{hand(84, 149)}'
             + f'<path d="M22 150 Q18 140 24 134" stroke="{cd}" stroke-width="7" fill="none" stroke-linecap="round"/>')
    elif kind == "sit":            # джульс
        g = (f'<path d="M30 150 Q28 128 44 124 L48 82 Q60 74 70 82 L74 124 Q92 128 90 150Z" fill="{c}" {s}/>' + _head(60, 62, girl)
             + f'<path d="M64 96 Q72 112 78 122" stroke="{cd}" stroke-width="8" fill="none" stroke-linecap="round"/>{hand(80, 124)}')
    elif kind == "salam":          # салям (вид спереди, поворот головы)
        g = (f'<path d="M30 150 Q28 128 44 124 L48 82 Q60 74 72 82 L76 124 Q92 128 90 150Z" fill="{c}" {s}/>' + _head(64, 62, girl)
             + f'<path d="M88 52 q10 6 10 14" stroke="#C9A15B" stroke-width="3" fill="none" marker-end="url(#arr)"/>'
             + '<defs><marker id="arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#C9A15B"/></marker></defs>')
    else:
        g = ""
    return f'<svg viewBox="0 0 126 162" width="{w}" class="pose">{mat}{g}</svg>'

# ---- иконки шагов абдеста
DR = '#6F9FD8'
def drops(*pts):
    return "".join(f'<path d="M{x} {y} q-4 7 0 10 q4 -3 0 -10z" fill="{DR}"/>' for x, y in pts)
def _ic(body):
    return f'<svg viewBox="0 0 100 100" class="wic">{body}</svg>'
HAND = lambda x, y, r=0, sc=1: (f'<g transform="translate({x} {y}) rotate({r}) scale({sc})"><path d="M-14 30 V-6 Q-14 -12 -9 -12 Q-4 -12 -4 -6 V-20 Q-4 -26 1 -26 Q6 -26 6 -20 V-6 V-16 Q6 -22 11 -22 Q16 -22 16 -16 V8 Q16 30 0 30Z" '
                                f'fill="{SK}" stroke="#C99A7A" stroke-width="2"/></g>')
FACE = (f'<circle cx="50" cy="52" r="30" fill="{SK}" stroke="#C99A7A" stroke-width="2"/><circle cx="40" cy="48" r="3" fill="{OUT}"/><circle cx="60" cy="48" r="3" fill="{OUT}"/>'
        f'<path d="M42 64 q8 6 16 0" stroke="{OUT}" stroke-width="2.5" fill="none" stroke-linecap="round"/>')
WIC = {
 "niyya": _ic(f'<path d="M50 86 Q12 60 16 36 Q20 18 36 20 Q46 22 50 32 Q54 22 64 20 Q80 18 84 36 Q88 60 50 86Z" fill="#E9A0B8" stroke="#B43F55" stroke-width="2"/>{drops()}'
              f'<path d="M50 12 l3 6 6 2 -6 2 -3 6 -3 -6 -6 -2 6 -2z" fill="#D8B26A"/>'),
 "hands": _ic(HAND(36, 50, -10) + HAND(64, 50, 10) + drops((30, 12), (50, 8), (70, 12), (44, 20), (58, 22))),
 "mouth": _ic(FACE + drops((50, 76)) + f'<path d="M30 84 Q50 96 70 84" stroke="{DR}" stroke-width="4" fill="none"/>'),
 "nose": _ic(FACE + f'<path d="M48 54 q2 6 4 0" stroke="#C99A7A" stroke-width="3" fill="none"/>' + drops((50, 30))),
 "face": _ic(FACE + drops((20, 30), (80, 30), (26, 76), (74, 76), (50, 14))),
 "arms": _ic(f'<path d="M12 60 Q40 50 70 52" stroke="{SK}" stroke-width="18" fill="none" stroke-linecap="round"/><path d="M12 60 Q40 50 70 52" stroke="#C99A7A" stroke-width="2" fill="none" stroke-dasharray="0" opacity=".3"/>'
             + HAND(80, 52, 90, .8) + drops((24, 38), (44, 32), (64, 34)) + '<circle cx="18" cy="60" r="6" fill="none" stroke="#C9A15B" stroke-width="2" stroke-dasharray="2 2"/>'),
 "head": _ic(FACE + f'<path d="M22 38 Q50 6 78 38" fill="#5C342E"/>' + HAND(50, 20, 180, .7)),
 "ears": _ic(FACE + f'<ellipse cx="18" cy="52" rx="7" ry="10" fill="{SK}" stroke="#C99A7A" stroke-width="2"/><ellipse cx="82" cy="52" rx="7" ry="10" fill="{SK}" stroke="#C99A7A" stroke-width="2"/>'
             f'<circle cx="18" cy="52" r="13" fill="none" stroke="#C9A15B" stroke-width="2" stroke-dasharray="3 3"/><circle cx="82" cy="52" r="13" fill="none" stroke="#C9A15B" stroke-width="2" stroke-dasharray="3 3"/>'),
 "neck": _ic(FACE.replace('cy="52" r="30"', 'cy="40" r="24"').replace('cy="48"', 'cy="38"').replace('M42 64', 'M42 50') + f'<rect x="40" y="62" width="20" height="16" fill="{SK}" stroke="#C99A7A" stroke-width="2"/><path d="M20 90 Q50 76 80 90" stroke="{SK}" stroke-width="10" fill="none"/>'
             f'<path d="M30 70 H70" stroke="#C9A15B" stroke-width="2" stroke-dasharray="3 3"/>'),
 "feet": _ic(f'<path d="M22 30 V66 Q22 82 38 84 L52 84 Q58 76 48 72 L38 70 V30Z" fill="{SK}" stroke="#C99A7A" stroke-width="2"/>'
             f'<path d="M56 30 V66 Q56 82 72 84 L86 84 Q92 76 82 72 L72 70 V30Z" fill="{SK}" stroke="#C99A7A" stroke-width="2"/>' + drops((30, 14), (64, 14), (46, 50), (80, 50))),
 "shahada": _ic(f'<path d="M50 8 V40" stroke="#C99A7A" stroke-width="2"/>' + HAND(50, 58, 0, 1.2).replace('V-20 Q-4 -26 1 -26 Q6 -26 6 -20 V-6 V-16 Q6 -22 11 -22 Q16 -22 16 -16', 'V-6 Q-4 -10 1 -10 Q6 -10 6 -6 V-34 Q6 -40 11 -40 Q16 -40 16 -34') + '<path d="M60 12 l3 6 6 2 -6 2 -3 6 -3 -6 -6 -2 6 -2z" fill="#D8B26A"/>'),
 "shower": _ic(f'<path d="M30 10 V24 Q30 30 40 30 H60" stroke="#9C8478" stroke-width="4" fill="none"/><rect x="56" y="24" width="26" height="12" rx="5" fill="#8E9DC6"/>' + drops(*[(58 + i*6, 44 + (i % 2) * 10) for i in range(5)], *[(60 + i*6, 66 + (i % 2) * 8) for i in range(4)])),
}
