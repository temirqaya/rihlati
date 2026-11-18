"""Зейнеб и Юсуф в «крымском» облике — по картинке пользователя:
Юсуф — чёрная шапочка с золотой вышивкой, белая рубашка, чёрная жилетка с золотом;
Зейнеб — кремовый платок с розовой вышитой каймой, терракотово-розовое платье с орнаментом."""
import itertools
_ids = itertools.count(1000)

SKIN, SKIN_D = "#F7DEC9", "#E9C1A4"
LINE = "#7A5444"
EYE = "#3A2A24"
GOLD, GOLD_D = "#C9A15B", "#A9823F"

def _defs(u):
    return (f'<defs><radialGradient id="ks{u}" cx=".45" cy=".4" r=".75"><stop offset="0" stop-color="#FDEBDD"/><stop offset="1" stop-color="{SKIN}"/></radialGradient>'
            f'<radialGradient id="kb{u}"><stop offset="0" stop-color="#EE9C92" stop-opacity=".7"/><stop offset="1" stop-color="#EE9C92" stop-opacity="0"/></radialGradient>'
            f'<filter id="kp{u}" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="3"/>'
            f'<feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .06 0"/><feComposite in2="SourceGraphic" operator="in"/><feBlend in="SourceGraphic" mode="multiply"/></filter></defs>')

def _face(u, cx, cy, mood):
    def eye(x):
        if mood == "closed":
            return f'<path d="M{x-7} {cy+1} q7 6 14 0" stroke="{EYE}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
        return (f'<ellipse cx="{x}" cy="{cy}" rx="7.5" ry="9" fill="{EYE}"/>'
                f'<circle cx="{x+2.5}" cy="{cy-3}" r="2.8" fill="#fff"/><circle cx="{x-2.2}" cy="{cy+3.2}" r="1.3" fill="#fff" opacity=".9"/>')
    brows = (f'<path d="M{cx-25} {cy-15} q7 -4 13 -1" stroke="{EYE}" stroke-width="2" fill="none" stroke-linecap="round" opacity=".6"/>'
             f'<path d="M{cx+12} {cy-16} q6 -3 13 1" stroke="{EYE}" stroke-width="2" fill="none" stroke-linecap="round" opacity=".6"/>')
    if mood == "open":
        mouth = f'<path d="M{cx-7} {cy+17} q7 2 14 0 q-2 9 -7 9 q-5 0 -7 -9z" fill="#B5544E"/>'
    else:
        mouth = f'<path d="M{cx-6} {cy+18} q6 6 12 0" stroke="#A54A44" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
    blush = (f'<ellipse cx="{cx-27}" cy="{cy+12}" rx="9" ry="6" fill="url(#kb{u})"/><ellipse cx="{cx+27}" cy="{cy+12}" rx="9" ry="6" fill="url(#kb{u})"/>')
    nose = f'<path d="M{cx-2} {cy+10} q2 2 4 0" stroke="{SKIN_D}" stroke-width="2.2" fill="none" stroke-linecap="round"/>'
    return brows + eye(cx - 18) + eye(cx + 18) + blush + nose + mouth

def _arm(side, pose, sleeve, cuff, x0, y0, u):
    s = side
    if pose == "wave":
        d, hx, hy = f"M{x0} {y0} q{s*24} -2 {s*30} -42", x0 + s*31, y0 - 50
    elif pose == "point":
        d, hx, hy = f"M{x0} {y0} q{s*22} 4 {s*40} -8", x0 + s*46, y0 - 10
    elif pose == "dua":
        d, hx, hy = f"M{x0} {y0} q{s*10} 30 {-s*12} 22", x0 - s*14, y0 + 16
    elif pose == "hold":
        d, hx, hy = f"M{x0} {y0} q{s*10} 24 {-s*8} 36", x0 - s*12, y0 + 40
    else:
        d, hx, hy = f"M{x0} {y0} q{s*14} 20 {s*11} 44", x0 + s*11, y0 + 50
    if pose == "dua":
        hand = f'<ellipse cx="{hx}" cy="{hy}" rx="9" ry="12" transform="rotate({-s*20} {hx} {hy})" fill="url(#ks{u})" stroke="{SKIN_D}" stroke-width="1.6"/>'
    else:
        hand = f'<circle cx="{hx}" cy="{hy}" r="9" fill="url(#ks{u})" stroke="{SKIN_D}" stroke-width="1.6"/>'
    return (f'<path d="{d}" stroke="{LINE}" stroke-width="22" fill="none" stroke-linecap="round" opacity=".35"/>'
            f'<path d="{d}" stroke="{sleeve}" stroke-width="18.5" fill="none" stroke-linecap="round"/>'
            f'<circle cx="{hx - (hx-x0)*0.1:.1f}" cy="{hy - (hy-y0)*0.1:.1f}" r="9.5" fill="{cuff}"/>' + hand)

def _orn_line(y, x1, x2, col=GOLD, step=10):
    return "".join(f'<path d="M{x} {y} q{step/2} -6 {step} 0" stroke="{col}" stroke-width="1.6" fill="none"/><circle cx="{x+step/2}" cy="{y-5}" r="1.3" fill="{col}"/>'
                   for x in range(int(x1), int(x2) - step + 1, step))


def _adam_head(u, mood):
    return (f'<path d="M91 140 h18 v22 q-9 5 -18 0z" fill="{SKIN_D}"/>'
         f'<ellipse cx="44" cy="106" rx="9" ry="12" fill="url(#ks{u})" stroke="{SKIN_D}" stroke-width="1.8"/><ellipse cx="156" cy="106" rx="9" ry="12" fill="url(#ks{u})" stroke="{SKIN_D}" stroke-width="1.8"/>'
         f'<ellipse cx="100" cy="102" rx="56" ry="53" fill="url(#ks{u})" stroke="{SKIN_D}" stroke-width="1.8"/>'
         f'<path d="M46 96 Q46 62 100 58 Q154 62 154 96 Q146 82 134 88 Q128 76 116 84 Q106 74 96 84 Q86 74 76 86 Q64 78 58 90 Q52 86 46 96Z" fill="#3E2C24"/>'
         f'<path d="M48 92 q-5 14 1 24 M152 92 q5 14 -1 24" stroke="#3E2C24" stroke-width="7" fill="none" stroke-linecap="round"/>'
         f'<path d="M50 74 Q50 30 100 28 Q150 30 150 74 Q100 62 50 74Z" fill="#2E2622" stroke="#1E1714" stroke-width="2" stroke-linejoin="round"/>'
         f'<path d="M52 70 Q100 58 148 70" stroke="{GOLD}" stroke-width="2.4" fill="none"/>'
         f'<path d="M56 58 Q100 46 144 58" stroke="{GOLD}" stroke-width="1.4" fill="none"/>'
         + "".join(f'<path d="M{x} {62 - (14 - abs(x-96)/6)*0.35:.1f} q4 -6 8 0 q-4 6 -8 0z" fill="none" stroke="{GOLD}" stroke-width="1.5"/>' for x in range(60, 136, 12)) +
         f'<path d="M78 42 q22 -9 44 0" stroke="{GOLD}" stroke-width="1.4" fill="none" stroke-dasharray="2 4"/>'
         f'<circle cx="100" cy="34" r="2.4" fill="{GOLD}"/>'
         + _face(u, 100, 106, mood))

def _adam_vest(x1=60, x2=140, top=158, bot=244):
    return (f'<path d="M{x1+8} {top+6} Q84 {top-2} 93 {top+1} L96 {bot} Q78 {bot+4} {x1} {bot}Z" fill="#2E2622" stroke="#1E1714" stroke-width="1.5"/>'
         f'<path d="M{x2-8} {top+6} Q116 {top-2} 107 {top+1} L104 {bot} Q122 {bot+4} {x2} {bot}Z" fill="#2E2622" stroke="#1E1714" stroke-width="1.5"/>'
         f'<path d="M92 {top+4} L95 {bot-2} M108 {top+4} L105 {bot-2}" stroke="{GOLD}" stroke-width="2"/>'
         f'<path d="M76 190 q6 -8 12 0 q-6 8 -12 0z M76 214 q6 -8 12 0 q-6 8 -12 0z M112 190 q6 -8 12 0 q-6 8 -12 0z M112 214 q6 -8 12 0 q-6 8 -12 0z" fill="none" stroke="{GOLD}" stroke-width="1.6"/>'
         f'<circle cx="82" cy="202" r="1.6" fill="{GOLD}"/><circle cx="118" cy="202" r="1.6" fill="{GOLD}"/>'
         + _orn_line(bot-4, x1+2, 96) + _orn_line(bot-4, 104, x2))

def adam(w=150, left="down", right="wave", mood="smile"):
    u = next(_ids)
    la, ra = _arm(-1, left, "#FFFDF8", "#EDE3D3", 66, 172, u), _arm(1, right, "#FFFDF8", "#EDE3D3", 134, 172, u)
    g = (f'<ellipse cx="100" cy="290" rx="50" ry="6" fill="#5C342E" opacity=".1"/>'
         f'<path d="M72 276 q-12 0 -12 9 q0 5 14 5 h12 q4 0 4 -6z" fill="#3A2A24"/><path d="M128 276 q12 0 12 9 q0 5 -14 5 h-12 q-4 0 -4 -6z" fill="#3A2A24"/>'
         f'<path d="M78 240 L76 278 H96 L100 250 L104 250 L106 278 H124 L122 240Z" fill="#EFE6D6" stroke="{LINE}" stroke-width="1.8" stroke-linejoin="round"/>'
         f'<path d="M68 162 Q100 150 132 162 L140 246 Q100 256 60 246Z" fill="#FFFDF8" stroke="{LINE}" stroke-width="2" stroke-linejoin="round"/>'
         + _adam_vest() +
         f'<path d="M88 159 Q100 168 112 159" stroke="#E2D6C3" stroke-width="3" fill="none"/>'
         + _adam_head(u, mood) + la + ra)
    return f'<svg class="char" viewBox="0 0 200 300" width="{w}" xmlns="http://www.w3.org/2000/svg">{_defs(u)}<g filter="url(#kp{u})">{g}</g></svg>'

DR, DR_D, CREAM = "#C9716A", "#A85A54", "#F3E9DA"

def _maryam_scarf_back():
    return (f'<path d="M100 30 Q162 32 164 110 Q166 166 138 192 Q100 208 62 192 Q34 166 36 110 Q38 32 100 30Z" fill="{CREAM}" stroke="#CDBBA3" stroke-width="2.2" stroke-linejoin="round"/>'
         f'<path d="M50 152 Q62 178 84 192 M150 152 Q138 178 116 192" stroke="#CDBBA3" stroke-width="2" fill="none" stroke-linecap="round"/>'
         f'<path d="M64 170 q6 -3 10 2 q-5 4 -10 -2z M130 172 q6 -4 10 0 q-5 5 -10 0z" fill="#E59A9F"/><circle cx="76" cy="180" r="2" fill="#7E9A6A"/><circle cx="126" cy="182" r="2" fill="#7E9A6A"/>')

def _maryam_face(u, mood):
    return (f'<ellipse cx="100" cy="110" rx="46" ry="47" fill="url(#ks{u})" stroke="{SKIN_D}" stroke-width="1.6"/>'
         f'<path d="M52 104 Q54 54 100 52 Q146 54 148 104 Q144 74 100 72 Q56 74 52 104Z" fill="#E7A39E" stroke="{DR}" stroke-width="1.5"/>'
         f'<path d="M58 92 Q62 66 100 64 Q138 66 142 92" stroke="#fff" stroke-width="1.6" fill="none" stroke-dasharray="2 4" opacity=".9"/>'
         + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#fff" opacity=".85"/>' for x, y in [(70, 74), (85, 67), (100, 65), (115, 67), (130, 74)]) +
         f'<path d="M118 42 q14 2 22 14 q4 6 6 14" stroke="#7E9A6A" stroke-width="1.6" fill="none"/>'
         + "".join(f'<ellipse cx="{x}" cy="{y}" rx="3.4" ry="1.8" transform="rotate({r} {x} {y})" fill="#7E9A6A"/>' for x, y, r in [(126, 44, 20), (136, 52, 45), (142, 62, 70)]) +
         f'<circle cx="122" cy="40" r="3" fill="#E59A9F"/><circle cx="146" cy="72" r="3" fill="#E59A9F"/>'
         + _face(u, 100, 114, mood)
         + f'<path d="M{100-18-8} {114-6} l-3 -3 M{100+18+8} {114-6} l3 -3" stroke="{EYE}" stroke-width="1.6" stroke-linecap="round"/>')

def maryam(w=150, left="wave", right="down", mood="smile"):
    u = next(_ids)
    la, ra = _arm(-1, left, DR, CREAM, 64, 190, u), _arm(1, right, DR, CREAM, 136, 190, u)
    flowers = "".join(f'<g transform="translate({x} {y})"><circle r="4" fill="{CREAM}"/><circle r="1.6" fill="{GOLD}"/>'
                      f'<path d="M-9 6 q4 -4 8 0 M1 6 q4 -4 8 0" stroke="#7E9A6A" stroke-width="1.4" fill="none"/></g>' for x, y in [(74, 236), (100, 246), (126, 236), (86, 260), (114, 260)])
    g = (f'<ellipse cx="100" cy="290" rx="52" ry="6" fill="#5C342E" opacity=".1"/>'
         f'<path d="M74 278 q-12 0 -12 8 q0 5 14 5 h12 q4 0 4 -6z" fill="#7A4A3E"/><path d="M126 278 q12 0 12 8 q0 5 -14 5 h-12 q-4 0 -4 -6z" fill="#7A4A3E"/>'
         f'<path d="M72 168 Q100 158 128 168 L152 278 Q100 290 48 278Z" fill="{DR}" stroke="{LINE}" stroke-width="2" stroke-linejoin="round"/>'
         f'<path d="M100 176 V270" stroke="{DR_D}" stroke-width="1.5" opacity=".5"/>'
         + flowers +
         f'<path d="M54 266 Q100 280 146 266" stroke="{CREAM}" stroke-width="6" fill="none" stroke-linecap="round"/>'
         + _orn_line(268, 60, 140, GOLD, 9)
         + _maryam_scarf_back() + _maryam_face(u, mood) + la + ra)
    return f'<svg class="char" viewBox="0 0 200 300" width="{w}" xmlns="http://www.w3.org/2000/svg">{_defs(u)}<g filter="url(#kp{u})">{g}</g></svg>'

def reading_scene(w=360):
    """Зейнеб и Юсуф сидят на подушках и читают Коран на рахле."""
    u = next(_ids)
    def cushion(x):
        return (f'<ellipse cx="{x}" cy="250" rx="62" ry="13" fill="#B9C7A8" stroke="#8FA27E" stroke-width="1.6"/>'
                + _orn_line(252, x - 50, x + 50, "#F3E9DA", 10))
    def boy(x):
        s = (f'<ellipse cx="{x}" cy="236" rx="54" ry="15" fill="#EFE6D6" stroke="{LINE}" stroke-width="1.8"/>'
             f'<path d="M{x-34} 234 Q{x-36} 170 {x} 162 Q{x+36} 170 {x+34} 234Z" fill="#FFFDF8" stroke="{LINE}" stroke-width="1.8"/>'
             f'<path d="M{x-32} 232 Q{x-34} 174 {x-7} 165 L{x-6} 232Z M{x+32} 232 Q{x+34} 174 {x+7} 165 L{x+6} 232Z" fill="#2E2622"/>'
             f'<path d="M{x-7} 166 L{x-6} 230 M{x+7} 166 L{x+6} 230" stroke="{GOLD}" stroke-width="1.6"/>'
             + _orn_line(228, x - 30, x - 8) + _orn_line(228, x + 8, x + 32))
        s += (f'<path d="M{x+22} 182 Q{x+40} 206 {x+60} 206" stroke="{LINE}" stroke-width="19" fill="none" stroke-linecap="round" opacity=".35"/>'
              f'<path d="M{x+22} 182 Q{x+40} 206 {x+60} 206" stroke="#FFFDF8" stroke-width="16" fill="none" stroke-linecap="round"/>'
              f'<circle cx="{x+64}" cy="204" r="8" fill="url(#ks{u})" stroke="{SKIN_D}" stroke-width="1.5"/>')
        s += f'<g transform="translate({x-62} 60) scale(.62)">{_adam_head(u, "smile")}</g>'
        return s
    def girl(x):
        s = (f'<ellipse cx="{x}" cy="238" rx="56" ry="15" fill="{DR}" stroke="{LINE}" stroke-width="1.8"/>'
             + _orn_line(244, x - 46, x + 46, GOLD, 9) +
             f'<path d="M{x-36} 236 Q{x-38} 172 {x} 162 Q{x+38} 172 {x+36} 236Z" fill="{DR}" stroke="{LINE}" stroke-width="1.8"/>'
             + "".join(f'<circle cx="{x+dx}" cy="{y}" r="3.2" fill="{CREAM}"/><circle cx="{x+dx}" cy="{y}" r="1.2" fill="{GOLD}"/>' for dx, y in [(-16, 202), (0, 214), (16, 202)]))
        s += (f'<path d="M{x-22} 184 Q{x-40} 206 {x-60} 206" stroke="{DR}" stroke-width="16" fill="none" stroke-linecap="round"/>'
              f'<circle cx="{x-64}" cy="204" r="8" fill="url(#ks{u})" stroke="{SKIN_D}" stroke-width="1.5"/>')
        s += f'<g transform="translate({x-62} 38) scale(.62)">{_maryam_scarf_back()}{_maryam_face(u, "smile")}</g>'
        return s
    rahle = (f'<path d="M156 254 L204 200 M204 254 L156 200" stroke="#8B5A3C" stroke-width="7" stroke-linecap="round"/>'
             f'<path d="M180 228 l-4 -4 l4 -4 l4 4z" fill="{GOLD}"/>'
             f'<path d="M138 198 Q160 186 180 196 Q200 186 222 198 L218 210 Q198 200 180 210 Q162 200 142 210Z" fill="#FBF4E8" stroke="{LINE}" stroke-width="1.8"/>'
             f'<path d="M150 199 h22 M150 203 h22 M188 199 h22 M188 203 h22" stroke="#8B5A3C" stroke-width="1" opacity=".6"/>'
             f'<path d="M180 196 V210" stroke="{GOLD}" stroke-width="1.5"/>')
    return (f'<svg class="char scene" viewBox="0 0 360 270" width="{w}" xmlns="http://www.w3.org/2000/svg">{_defs(u)}<g filter="url(#kp{u})">'
            f'{cushion(86)}{cushion(274)}{boy(86)}{girl(274)}{rahle}</g></svg>')
