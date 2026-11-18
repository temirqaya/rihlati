"""Голова в разрезе (вид сбоку, анатомический стиль) для раздела «Откуда выходят звуки».
Зоны: throat (горло), tongue (язык), lips (губы), nose (нос), mouth (пустота рта).
svg(focus=['throat'], marks=[(x, y, '1'), ...])"""

SKIN, SKIN_D, TISSUE, BONE = '#F4C2A8', '#E3A487', '#EBA58F', '#F6E3CC'
LINE = '#B9715C'
CAV = '#7B2E39'        # тёмная полость
NASAL = '#A9474F'
TONGUE, TONGUE_D = '#E8848C', '#D06A74'
LIP = '#D9706C'

def svg(focus=None, marks=(), cls='mth-svg'):
    f = set(focus or [])
    def z(name, body):
        dim = f and name not in f
        glow = ' mzon' if name in f else ''
        return f'<g class="mz{glow}" data-z="{name}" style="opacity:{".3" if dim else "1"}">{body}</g>'
    # внешний контур: лоб, нос, губы, подбородок, шея
    outer = ('<path d="M120 18 C150 10 230 8 262 30 C292 60 296 120 282 168 L276 330 L150 330 L150 262 '
             'C128 252 104 246 90 232 C80 222 76 210 78 200 C70 198 66 192 68 186 C66 180 68 175 72 172 '
             'C66 168 66 160 74 156 C64 152 52 148 50 140 C48 132 60 122 72 112 C82 96 92 70 100 50 C106 34 112 22 120 18Z" '
             f'fill="{SKIN}" stroke="{LINE}" stroke-width="2.2" stroke-linejoin="round"/>')
    # кости черепа и нёба (кремовые)
    skull = (f'<path d="M110 40 C150 30 220 34 250 58 L246 96 C210 92 160 96 120 104 Z" fill="{BONE}" opacity=".85"/>'
             f'<path d="M84 158 C120 152 160 150 186 152 L186 161 C160 160 120 162 86 167 Z" fill="{BONE}" stroke="{LINE}" stroke-width="1.2"/>')
    # позвонки
    vert = ''.join(f'<rect x="242" y="{y}" width="26" height="22" rx="6" fill="{BONE}" stroke="{LINE}" stroke-width="1.2"/>' for y in (150, 178, 206, 234, 262, 290))
    # нижняя челюсть
    jaw = f'<path d="M84 206 C100 222 130 232 160 234 L162 244 C128 244 98 234 80 218 Z" fill="{BONE}" stroke="{LINE}" stroke-width="1.2"/>'
    # нос: носовая полость с раковинами
    nose = z('nose', f'<path d="M66 140 C70 126 90 112 120 108 C160 102 210 104 236 116 L236 150 C214 148 190 150 186 152 C160 150 120 152 84 158 C76 152 68 148 66 140Z" fill="{NASAL}" stroke="{LINE}" stroke-width="1.4"/>'
                     '<path d="M120 122 C150 114 190 116 214 124 M116 138 C150 130 186 132 220 138" stroke="#D27A7C" stroke-width="6" fill="none" stroke-linecap="round" opacity=".8"/>'
                     f'<ellipse cx="78" cy="138" rx="6" ry="4" fill="{CAV}"/>')
    # мягкое нёбо и язычок
    velum = f'<path d="M186 152 C200 152 214 158 222 170 C226 178 224 188 218 190 C214 184 210 176 200 168 C194 164 190 162 186 161Z" fill="{TISSUE}" stroke="{LINE}" stroke-width="1.4"/>'
    # пустота рта
    mouth = z('mouth', f'<path d="M90 170 C120 163 160 160 186 162 C196 164 206 170 214 182 C190 176 160 172 130 174 C112 176 100 180 92 184 Z" fill="{CAV}" stroke="{LINE}" stroke-width="1.2"/>')
    # глотка и гортань (горло)
    throat = z('throat', f'<path d="M236 116 C244 130 244 150 238 170 L234 330 L212 330 L214 268 C216 250 224 230 226 212 C228 196 224 182 218 172 C226 160 232 140 236 116Z" fill="{CAV}" stroke="{LINE}" stroke-width="1.4"/>'
                         f'<path d="M182 262 C196 258 210 260 214 268 L212 330 L184 330 Z" fill="#E9A28F" stroke="{LINE}" stroke-width="1.4"/>'
                         + ''.join(f'<path d="M186 {y} h24" stroke="{LINE}" stroke-width="1.2" opacity=".6"/>' for y in (282, 296, 310, 324))
                         + f'<path d="M210 262 C206 252 208 242 214 236 C216 246 216 254 212 264Z" fill="{BONE}" stroke="{LINE}" stroke-width="1.2"/>')
    # язык
    tongue = z('tongue', f'<path d="M92 186 C108 178 140 172 172 176 C196 180 214 192 222 210 C226 226 220 244 214 258 C200 252 186 246 172 242 C140 236 112 226 96 210 C88 202 86 192 92 186Z" fill="{TONGUE}" stroke="{LINE}" stroke-width="1.6"/>'
                         f'<path d="M104 196 C140 188 180 192 208 214" stroke="{TONGUE_D}" stroke-width="2.4" fill="none" stroke-linecap="round"/>')
    # зубы и губы
    teeth = (f'<path d="M84 160 h10 v16 q-5 4 -10 0z" fill="#FFFDF7" stroke="{LINE}" stroke-width="1.3"/>'
             f'<path d="M86 204 h10 v-14 q-5 -4 -10 0z" fill="#FFFDF7" stroke="{LINE}" stroke-width="1.3"/>')
    lips = z('lips', f'<path d="M68 160 C74 156 84 157 86 162 L86 176 C80 180 70 178 68 172 C64 168 64 163 68 160Z" fill="{LIP}" stroke="{LINE}" stroke-width="1.4"/>'
                     f'<path d="M70 186 C76 182 86 184 88 188 L88 202 C82 206 72 204 70 198 C66 194 66 189 70 186Z" fill="{LIP}" stroke="{LINE}" stroke-width="1.4"/>')
    eye = f'<path d="M108 76 q10 -7 20 0" stroke="#5C3A30" stroke-width="3" fill="none" stroke-linecap="round"/>'
    mk = ''.join(f'<g><circle cx="{x}" cy="{y}" r="11" fill="#fff" stroke="#5C4033" stroke-width="2"/>'
                 f'<text x="{x}" y="{y + 5}" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="900" font-size="14" fill="#5C4033">{t}</text></g>' for x, y, t in marks)
    return (f'<svg class="{cls}" viewBox="16 6 274 330" xmlns="http://www.w3.org/2000/svg" role="img">'
            + outer + skull + vert + jaw + nose + velum + mouth + throat + tongue + teeth + lips + eye + mk + '</svg>')

# метки для уроков
THROAT_MARKS = [(198, 300, '1'), (226, 238, '2'), (228, 186, '3')]
TONGUE_MARKS = [(208, 222, '1'), (160, 186, '2'), (150, 222, '3'), (128, 184, '4'), (100, 200, '5')]

# точка махраджа для каждой буквы (координаты рисунка)
POINT = {'ء': (198, 304), 'ه': (198, 290), 'ع': (226, 246), 'ح': (226, 232), 'غ': (226, 198), 'خ': (226, 186),
         'ق': (212, 196), 'ك': (196, 184), 'ج': (160, 176), 'ش': (150, 177), 'ي': (140, 179), 'ض': (150, 214),
         'ل': (128, 184), 'ن': (108, 182), 'ر': (112, 187), 'ت': (97, 180), 'د': (97, 180), 'ط': (97, 180),
         'ص': (94, 198), 'س': (94, 198), 'ز': (94, 198), 'ث': (89, 176), 'ذ': (89, 176), 'ظ': (89, 176),
         'ف': (86, 186), 'ب': (72, 182), 'م': (72, 182), 'و': (70, 182), 'نّ': (112, 130), 'مّ': (112, 130),
         'ا': (150, 169), 'وٗ': (150, 169), 'يٖ': (150, 169)}
