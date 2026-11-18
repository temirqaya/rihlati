"""Вступительные страницы: хадисы и дуа, алфавит, солнечные и лунные буквы; практика «лям в аль»."""
from lib import *
from data import LETTERS

SUN = "ت ث د ذ ر ز س ش ص ض ط ظ ل ن".split()
MOON = "ا ب ج ح خ ع غ ف ق ك م و ه ي".split()

def hadith_page(book):
    hs = [("خَيْرُكُمْ مَنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ",
           "«Лучший из вас — тот, кто изучил Коран и обучил ему других».", "аль-Бухари"),
          ("مَنْ قَرَأَ حَرْفًا مِنْ كِتَابِ اللَّهِ فَلَهُ بِهِ حَسَنَةٌ، وَالْحَسَنَةُ بِعَشْرِ أَمْثَالِهَا، لَا أَقُولُ الم حَرْفٌ، وَلَكِنْ أَلِفٌ حَرْفٌ، وَلَامٌ حَرْفٌ، وَمِيمٌ حَرْفٌ",
           "«Кто прочитает одну букву из Книги Аллаха, тому за неё — одно доброе дело, а доброе дело — в десятикратном размере. Я не говорю, что „алиф-лям-мим“ — одна буква: алиф — буква, лям — буква и мим — буква».",
           "ат-Тирмизи"),
          ("الْمَاهِرُ بِالْقُرْآنِ مَعَ السَّفَرَةِ الْكِرَامِ الْبَرَرَةِ، وَالَّذِي يَقْرَأُ الْقُرْآنَ وَيَتَتَعْتَعُ فِيهِ وَهُوَ عَلَيْهِ شَاقٌّ لَهُ أَجْرَانِ",
           "«Искусный в чтении Корана будет с благородными и покорными писцами-ангелами, а тот, кто читает Коран, запинаясь, и ему трудно, получит двойную награду».",
           "аль-Бухари и Муслим")]
    cards = "".join(f'<div class="hadith"><div class="h-ar" lang="ar" dir="rtl">{a}</div><div class="h-ru">{r}</div><div class="h-src">{s}</div></div>' for a, r, s in hs)
    book.add(f'''<h1 class="title sm">Зачем мы учимся читать Коран?</h1>
<p class="lead">Пророк Мухаммад ﷺ сказал:</p>
<div class="hadiths">{cards}</div>
<div class="dua"><div class="dua-h">Дуа перед каждым занятием</div>
<div class="dua-ar" lang="ar" dir="rtl">رَبِّ يَسِّرْ وَلَا تُعَسِّرْ، رَبِّ تَمِّمْ بِالْخَيْرِ</div>
<div class="dua-ru">«Господи, облегчи и не затрудняй, Господи, заверши благом»</div></div>
<div class="row-kids">{maryam(105, left="wave", mood="open")}{bubble("Даже если трудно — за каждую букву есть награда! Не сдавайся!", "maryam")}</div>''', sky=False, cls="softpage")

def alphabet_page(book):
    cells = "".join(f'<div class="ab-c"><span lang="ar">{l[0]}</span><b>{l[2]}</b><small lang="ar" dir="rtl">{l[1]}</small><i>{i}</i></div>' for i, l in enumerate(LETTERS, 1))
    book.add(f'''<h1 class="title sm">Арабский алфавит — {AR("الْحُرُوفُ الْهِجَائِيَّةُ", "inl")}</h1>
<div class="ab-facts">
<div><b>28</b><span>букв в алфавите</span></div>
<div><b>⬅</b><span>пишем и читаем справа налево</span></div>
<div><b>6</b><span>букв не соединяются со следующей: {AR("ا د ذ ر ز و", "inl")}</span></div>
<div><b>4</b><span>формы у буквы: отдельно, в начале, в середине, в конце</span></div></div>
<div class="ab-grid" dir="rtl">{cells}</div>
<div class="parents sm">Кроме 28 букв, в книге встретятся <b>хамза</b> {AR("ء", "inl")} (короткая «заминка» горла, часто сидит на алифе: {AR("أ", "inl")}),
<b>лям-алиф</b> {AR("لا", "inl")} (так пишутся лям и алиф вместе) и <b>та марбута</b> {AR("ة", "inl")} (бывает только в конце слова).
Гласных букв как в русском нет — гласные звуки показывают огласовки (раздел 3).</div>''', section=("الْحُرُوفُ الْهِجَائِيَّةُ", "Знакомство с алфавитом", SECCOL["intro"]))

def sun_moon_page(book):
    sun_svg = f'<svg viewBox="0 0 80 80" width="58"><g stroke="{GOLD2}" stroke-width="5" stroke-linecap="round">' + "".join(f'<line x1="40" y1="6" x2="40" y2="16" transform="rotate({a} 40 40)"/>' for a in range(0, 360, 45)) + f'</g><circle cx="40" cy="40" r="18" fill="{GOLD}"/></svg>'
    moon_svg = f'<svg viewBox="0 0 80 80" width="58"><circle cx="40" cy="40" r="26" fill="{IND}"/><circle cx="52" cy="32" r="22" fill="#E4E9F4"/>{star(62, 58, 6, GOLD)}</svg>'
    sl = "".join(f'<span lang="ar">{x}</span>' for x in SUN)
    ml = "".join(f'<span lang="ar">{x}</span>' for x in MOON)
    book.add(f'''<h1 class="title sm">Солнечные и лунные буквы</h1>
<p class="lead">Многие слова начинаются с {AR("ال", "inl")} («аль»). Читается ли лям — зависит от первой буквы слова. По этому правилу все 28 букв делятся на две семьи по 14:</p>
<div class="sm-grid">
<div class="smb moon"><div class="smb-h">{moon_svg}<div><b>Лунные буквы</b><br>{AR("الْحُرُوفُ الْقَمَرِيَّةُ", "inl")}</div></div>
<div class="smb-l" dir="rtl">{ml}</div>
<p>Лям <b>читаем ясно</b>, с сукуном: {AR("الْقَمَرُ", "inl")} — «аль-камар».</p>
<p class="mn">Запомни: {AR("ابْغِ حَجَّكَ وَخَفْ عَقِيمَهُ", "inl")}</p></div>
<div class="smb sun"><div class="smb-h">{sun_svg}<div><b>Солнечные буквы</b><br>{AR("الْحُرُوفُ الشَّمْسِيَّةُ", "inl")}</div></div>
<div class="smb-l" dir="rtl">{sl}</div>
<p>Лям <b>не читаем</b> — он «прячется», а следующая буква получает шадду: {AR("الشَّمْسُ", "inl")} — «аш-шамс».</p>
<p class="mn">Как солнце прячет звёзды, так солнечная буква прячет лям!</p></div></div>
<div class="ex-h">Примеры из Корана</div>
<div class="sm-ex"><div>{qgrid_local([qf(1, 2, "الحمد", 1, "🌙 лунная"), qf(113, 1, "الفلق", 1, "🌙 лунная")])}</div>
<div>{qgrid_local([qf(114, 1, "الناس", 1, "☀ солнечная"), qf(112, 2, "الصمد", 1, "☀ солнечная")])}</div></div>
<div class="ex-h">А здесь оба слова стоят рядом:</div>{qgrid_local([qf(55, 5, "الشمس", 2)])}
<div class="row-kids">{adam(100, right="point", mood="open")}{bubble("Посмотри на лям: есть сукун — читаем, нет сукуна, а дальше шадда — молчим!", "adam")}</div>''',
             section=("الشَّمْسِيَّةُ وَالْقَمَرِيَّةُ", "Знакомство с алфавитом", SECCOL["intro"]))

def qgrid_local(fr):
    return '<div class="qgrid">' + "".join(fr) + '</div>'

def lam_practice(book, sec):
    words = [(1, 2, "العلمين"), (1, 3, "الرحمن"), (1, 4, "الدين"), (1, 6, "المستقيم"), (1, 6, "الصرط"), (1, 7, "الضالين"),
             (108, 1, "الكوثر"), (113, 1, "الفلق"), (114, 1, "الناس"), (114, 4, "الوسواس"), (114, 4, "الخناس"), (112, 2, "الصمد")]
    cells = "".join(f'<div class="lw"><span lang="ar" dir="rtl">{qsel(s, v, w)}</span><div class="lw-c">☀ ☐ &nbsp; 🌙 ☐</div></div>' for s, v, w in words)
    book.add(f'''<h1 class="title sm">Лям в слове «аль»: солнце или луна?</h1>
<p class="lead">Найди первую букву после {AR("ٱل", "inl")}. Если над лямом сукун {AR("◌ۡ", "inl")} — это лунная буква, лям читаем. Если сукуна нет, а дальше шадда — солнечная, лям не читаем. Отметь ☀ или 🌙.</p>
<div class="lws">{cells}</div>
<div class="row-kids">{maryam(100, left="point", mood="open")}{bubble("В мусхафе алиф в начале пишется как ٱ — при чтении подряд он молчит.", "maryam")}</div>''', section=sec)
