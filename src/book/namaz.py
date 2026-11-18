#!/usr/bin/env python3
"""Методичка для детей: абдест, гусуль и намаз (ханафитский мазхаб). Без игр."""
import lib
from lib import *
import cover_min as CM, extras as E, fancy as F, metod as M
from poses import pose, WIC

COL = ("#3C7FB0", "#D8E8F3")
SEC_W = ("الطَّهَارَةُ", "Чистота · абдест и гусуль", ("#3F8F86", "#D6ECE8"))
SEC_N = ("الصَّلَاةُ", "Намаз", ("#3C7FB0", "#D8E8F3"))
SEC_0 = ("طَهَارَتِي وَصَلَاتِي", "Мой абдест и мой намаз", ("#B8914A", "#F5E8CC"))

lib.KIDNOTES = [
    ("adam", "Делай медленно и аккуратно — Аллах любит старание."),
    ("maryam", "Не торопись: лучше правильно, чем быстро."),
    ("adam", "Если что-то забыл — спроси папу или маму."),
    ("maryam", "Чистота — это красиво и угодно Аллаху!"),
]

def txt(ar, tr, ru, size=30):
    return (f'<div class="nt-card"><div class="nt-ar" lang="ar" dir="rtl" style="font-size:{size}px">{ar}</div>'
            f'<div class="nt-tr">{tr}</div><div class="nt-ru">{ru}</div></div>')

def wsteps(items, start=1):
    return '<div class="wsteps">' + "".join(
        f'<div class="ws"><div class="ws-i">{WIC[k]}</div><div class="ws-b"><span>{n}</span><b>{t}</b><p>{d}</p></div></div>'
        for n, (k, t, d) in enumerate(items, start)) + '</div>'

def build():
    b = Book()
    b.pages.append(f'''<section class="page cover-min">
<div class="cm-frame"></div>
<div class="cm-in">
<svg class="cm-moon" viewBox="0 0 60 60"><circle cx="28" cy="30" r="20" fill="#D8B26A"/><circle cx="37" cy="25" r="17" fill="#FBF6F0"/>{star(46, 44, 5, "#D8B26A")}</svg>
<div class="cm-ar" lang="ar" dir="rtl">طَهَارَتِي وَصَلَاتِي</div>
<div class="cm-line"></div>
<div class="cm-ru">Мой абдест<br>и мой намаз</div>
<div class="cm-sub">Методичка для детей</div>
<div class="cm-stage">{M.CM_arch()}<div class="cm-kids">{adam(150, right="wave", mood="open")}{maryam(150, left="wave", mood="open")}</div></div>
</div></section>''')

    b.add(f'''<h1 class="title sm">Дорогие взрослые</h1>
<div class="soft-card">
<p>Пророк Мухаммад ﷺ советовал учить детей намазу с семи лет. Эта методичка поможет спокойно и по шагам объяснить ребёнку, как совершать <b>абдест</b> (малое омовение), что такое <b>гусуль</b> (полное омовение) и как совершать <b>намаз</b>.</p>
<p>Всё описано по <b>ханафитскому мазхабу</b>, которому традиционно следуют крымские татары. Показывайте каждое действие сами: дети лучше всего учатся, повторяя за родителями.</p>
<p>Не требуйте сразу всего. Сначала — абдест и короткие слова намаза, затем — суры и ташаххуд. Хвалите за старание, а не только за результат.</p></div>
{M.say("adam", "Мы с Зейнеб покажем всё по шагам. Бисмиллях!", "open", "wave", 120)}''', section=SEC_0)

    b.add(f'''<h1 class="title sm">Чистота — половина веры</h1>
<div class="qcard"><div class="qc-tr" style="font-size:18px">«Чистота — половина веры»</div><div class="qc-ru">Пророк Мухаммад ﷺ</div></div>
<div class="three">
<div class="th-c"><div class="th-i">{WIC["hands"]}</div><b>Абдест</b><p>Малое омовение. Его делают перед намазом и перед тем, как взять в руки Коран.</p></div>
<div class="th-c"><div class="th-i">{WIC["shower"]}</div><b>Гусуль</b><p>Полное омовение всего тела. Взрослым оно обязательно в особых случаях.</p></div>
<div class="th-c"><div class="th-i">{pose("stand", w=60)}</div><b>Намаз</b><p>Молитва, которую мусульманин совершает пять раз в день.</p></div></div>
<div class="soft-card"><p>Аллах любит тех, кто стремится к чистоте. Перед намазом мусульманин моет руки, лицо, ноги — и как будто смывает с себя всё плохое. Пророк ﷺ рассказывал, что вместе с водой абдеста уходят и маленькие грехи.</p></div>''', section=SEC_0)

    # ---------- абдест
    b.add(f'''<h1 class="title sm">Абдест: самое главное</h1>
<p class="lead">В абдесте есть <b>4 обязательных действия (фарз)</b>. Без них абдест не считается:</p>
<div class="fards">
<div class="fd"><div class="ws-i">{WIC["face"]}</div><b>1. Умыть лицо</b><p>от начала волос до подбородка и от уха до уха</p></div>
<div class="fd"><div class="ws-i">{WIC["arms"]}</div><b>2. Вымыть руки</b><p>вместе с локтями</p></div>
<div class="fd"><div class="ws-i">{WIC["head"]}</div><b>3. Протереть голову</b><p>влажной рукой — хотя бы четверть головы</p></div>
<div class="fd"><div class="ws-i">{WIC["feet"]}</div><b>4. Вымыть ноги</b><p>вместе с щиколотками</p></div></div>
<div class="soft-card"><p>Всё остальное — <b>сунна</b>: так делал Пророк ﷺ. Если делать абдест полностью, по сунне, награда будет больше. На следующих страницах — весь абдест по порядку.</p></div>
{M.say("maryam", "Начинаем всегда с правой стороны: правая рука, правая нога.", "smile", "point", 105)}''', section=SEC_W)

    a1 = [("niyya", "Намерение", "В сердце: «Я делаю абдест ради Аллаха»."),
          ("niyya", "«Бисмиллях»", "Начинаем с имени Аллаха: «Бисмилляхи-р-Рахмани-р-Рахим»."),
          ("hands", "Кисти рук — 3 раза", "Моем кисти рук до запястий, промываем между пальцами."),
          ("mouth", "Рот — 3 раза", "Набираем воду правой рукой и полощем рот."),
          ("nose", "Нос — 3 раза", "Правой рукой втягиваем немного воды в нос, а высмаркиваемся левой."),
          ("face", "Лицо — 3 раза", "Умываем лицо целиком: от волос до подбородка, от уха до уха.")]
    a2 = [("arms", "Правая рука — 3 раза", "Моем руку от кончиков пальцев до локтя вместе с локтем. Потом левую — тоже 3 раза."),
          ("head", "Голова — 1 раз", "Мокрыми руками проводим по голове ото лба к затылку."),
          ("ears", "Уши", "Указательными пальцами протираем уши внутри, большими — снаружи."),
          ("neck", "Шея", "Тыльной стороной пальцев проводим по шее."),
          ("feet", "Ноги — 3 раза", "Моем правую ногу вместе с щиколоткой и между пальцами, потом левую."),
          ("shahada", "Шахада", "После абдеста поднимаем взгляд и говорим свидетельство веры.")]
    b.add(f'<h1 class="title sm">Абдест по шагам · 1</h1>{wsteps(a1)}', section=SEC_W)
    b.add(f'<h1 class="title sm">Абдест по шагам · 2</h1>{wsteps(a2, 7)}', section=SEC_W)
    b.add(f'''<h1 class="title sm">После абдеста</h1>
<p class="lead">Закончив абдест, говорим:</p>
{txt("أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ",
     "Ашхаду ал-ля иляха илля-ллаху вахдаху ля шарика лях, ва ашхаду анна Мухаммадан ‘абдуху ва расулюх",
     "Свидетельствую, что нет божества, кроме Аллаха, Единого, у Которого нет сотоварища, и свидетельствую, что Мухаммад — Его раб и посланник.", 27)}
<div class="soft-card"><p><b>Полезные советы:</b> не тратить много воды — даже у реки Пророк ﷺ берёг воду; не разговаривать во время абдеста; мыть каждую часть так, чтобы не осталось сухих мест — особенно локти, пятки и между пальцами.</p></div>
{M.say("adam", "Пророк ﷺ сказал, что для того, кто так говорит после абдеста, открываются все восемь врат Рая!", "open", "point", 105)}''', section=SEC_W)

    br = [("🚻", "Сходить в туалет", "по малой или большой нужде"), ("💨", "Выход газов", ""), ("😴", "Сон лёжа", "или облокотившись так, что можно упасть"),
          ("🩸", "Кровь или гной", "если вышли и растеклись"), ("🤢", "Рвота", "полным ртом"), ("😵", "Потеря сознания", ""),
          ("😂", "Громкий смех в намазе", "у взрослых нарушает и намаз, и абдест")]
    bh = "".join(f'<div class="brk"><span>{i}</span><div><b>{t}</b>{f"<p>{d}</p>" if d else ""}</div></div>' for i, t, d in br)
    b.add(f'''<h1 class="title sm">Что нарушает абдест?</h1>
<p class="lead">Если случилось что-то из этого, нужно сделать абдест заново:</p>
<div class="brks">{bh}</div>
<div class="soft-card"><p>Если абдест не нарушился, им можно совершить несколько намазов подряд. А если сомневаешься — лучше обновить абдест.</p></div>''', section=SEC_W)

    # ---------- гусуль
    b.add(f'''<h1 class="title sm">Гусуль — полное омовение</h1>
<div class="soft-card"><p><b>Гусуль</b> — это когда мы омываем водой всё тело. Когда ты подрастёшь, гусуль станет <b>обязательным</b> в некоторых случаях — об этом тебе расскажут мама и папа.</p>
<p>А ещё гусуль — это <b>сунна</b>: его хорошо делать перед пятничным намазом, перед праздниками Ураза-байрам и Курбан-байрам.</p></div>
<p class="lead">В гусуле <b>3 обязательных действия (фарз)</b>:</p>
<div class="fards f3">
<div class="fd"><div class="ws-i">{WIC["mouth"]}</div><b>1. Прополоскать рот</b><p>так, чтобы вода дошла до горла</p></div>
<div class="fd"><div class="ws-i">{WIC["nose"]}</div><b>2. Промыть нос</b><p>до мягкой части</p></div>
<div class="fd"><div class="ws-i">{WIC["shower"]}</div><b>3. Омыть всё тело</b><p>чтобы не осталось ни одного сухого места</p></div></div>''', section=SEC_W)
    g = [("niyya", "Намерение и «Бисмиллях»", "В сердце: «Я делаю гусуль ради Аллаха»."),
         ("hands", "Вымыть руки", "Моем кисти рук и, если нужно, места, которые закрыты одеждой."),
         ("face", "Сделать абдест", "Делаем полный абдест, как перед намазом."),
         ("shower", "Голова — 3 раза", "Поливаем голову водой три раза, чтобы промокли все волосы."),
         ("shower", "Правое плечо, потом левое", "Поливаем правую сторону тела три раза, потом левую — три раза."),
         ("shower", "Всё тело", "Проверяем, чтобы вода попала везде: за ушами, в пупке, под кольцами и между пальцами.")]
    b.add(f'''<h1 class="title sm">Гусуль по шагам</h1>{wsteps(g)}''', section=SEC_W)

    # ---------- намаз
    pr = [("Фаджр", "утренний", "до восхода солнца", 2), ("Зухр", "полуденный", "после полудня", 4), ("Аср", "послеполуденный", "во второй половине дня", 4),
          ("Магриб", "вечерний", "сразу после заката", 3), ("Иша", "ночной", "когда стемнеет", 4)]
    ph = "".join(f'<div class="pr"><b>{n}</b><span>{t}</span><p>{w}</p><em>{r} ракаата</em></div>' for n, t, w, r in pr)
    b.add(f'''<h1 class="title sm">Пять намазов в день</h1>
<p class="lead">Аллах сделал обязательными пять намазов. Каждый — в своё время:</p>
<div class="prs">{ph}</div>
<div class="soft-card"><p>Здесь указаны <b>фарз</b>-ракааты — обязательные. Кроме них есть ракааты <b>сунна</b>, а после ночного намаза — <b>витр</b> (3 ракаата), обязательный (ваджиб) по ханафитскому мазхабу. <b>Ракаат</b> — это одна часть намаза: стояние, поясной поклон и два земных поклона.</p></div>''', section=SEC_N)

    cond = [("💧", "Абдест", "сделан и не нарушен"), ("👕", "Чистота", "тело, одежда и место для намаза чистые"),
            ("🧕", "Закрытое тело", "мальчики — от пупка до колен (лучше в закрытой одежде); девочки — всё тело, кроме лица, кистей рук и стоп"),
            ("🕋", "Кибла", "стоим лицом в сторону Каабы"), ("🕐", "Время", "наступило время этого намаза"), ("🤍", "Намерение", "знаем, какой намаз совершаем")]
    ch = "".join(f'<div class="brk"><span>{i}</span><div><b>{t}</b><p>{d}</p></div></div>' for i, t, d in cond)
    b.add(f'''<h1 class="title sm">Перед намазом</h1>
<p class="lead">Чтобы намаз был правильным, нужно, чтобы было всё это:</p>
<div class="brks">{ch}</div>
{M.say("maryam", "Положи коврик, повернись к кибле — и ты готов к разговору с Аллахом!", "smile", "point", 105)}''', section=SEC_N)

    def nstep(n, p, title, text, extra=""):
        return f'<div class="ns"><div class="ns-p">{p}</div><div class="ns-b"><span>{n}</span><b>{title}</b><p>{text}</p>{extra}</div></div>'

    def mini(ar, tr, ru, size=24):
        return f'<div class="ns-t"><div lang="ar" dir="rtl" style="font-size:{size}px">{ar}</div><i>{tr}</i><small>{ru}</small></div>'

    b.add(f'''<h1 class="title sm">Как совершать намаз · 1</h1>
<p class="lead">Покажем на примере намаза из двух ракаатов (как утренний фарз).</p>
<div class="nsteps">
{nstep(1, pose("stand", w=70), "Намерение", "Встаём на коврик лицом к кибле и в сердце делаем намерение: «Я совершаю ради Аллаха утренний намаз».")}
{nstep(2, pose("takbir", w=70), "Такбир", "Поднимаем руки: мальчики — к ушам, девочки — до плеч, и говорим:", mini("اللَّهُ أَكْبَرُ", "Аллаху акбар", "Аллах велик", 26))}
{nstep(3, pose("stand", w=70), "Кыям — стояние", "Мальчики кладут правую руку на левую под пупком, девочки — на груди. Тихо читаем «Сана»:", mini("سُبْحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ، وَتَبَارَكَ اسْمُكَ، وَتَعَالَى جَدُّكَ، وَلَا إِلَهَ غَيْرُكَ", "Субханака-ллахумма ва бихамдика, ва табаракя-смука, ва та‘аля джаддука, ва ля иляха гайрук", "Пречист Ты, о Аллах, хвала Тебе, благословенно Твоё имя, превыше всего Твоё величие, и нет божества, кроме Тебя.", 20))}
</div>''', section=SEC_N)

    b.add(f'''<h1 class="title sm">Как совершать намаз · 2</h1>
<div class="nsteps">
{nstep(4, pose("stand", w=70), "Аузу и Бисмиллях", "Тихо говорим:", mini("أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ ۝ بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ", "Аузу билляхи мина-ш-шайтани-р-раджим. Бисмилляхи-р-Рахмани-р-Рахим", "Прибегаю к Аллаху от проклятого шайтана. С именем Аллаха, Милостивого, Милосердного.", 20))}
{nstep(5, pose("stand", w=70), "Сура «аль-Фатиха»", "Читаем суру «аль-Фатиха» (она на отдельной странице), а после неё тихо говорим «Амин».")}
{nstep(6, pose("stand", w=70), "Ещё одна сура", "Читаем короткую суру, например «аль-Ихлас», или несколько аятов.")}
{nstep(7, pose("ruku", w=70), "Руку — поясной поклон", "Со словами «Аллаху акбар» наклоняемся, руки на коленях, спина ровная. Три раза говорим:", mini("سُبْحَانَ رَبِّيَ الْعَظِيمِ", "Субхана Раббияль-‘Азым", "Пречист мой Великий Господь", 24))}
</div>''', section=SEC_N)

    b.add(f'''<h1 class="title sm">Как совершать намаз · 3</h1>
<div class="nsteps">
{nstep(8, pose("stand", w=70), "Выпрямляемся", "Поднимаемся и говорим, а потом стоя добавляем:", mini("سَمِعَ اللَّهُ لِمَنْ حَمِدَهُ ۝ رَبَّنَا لَكَ الْحَمْدُ", "Сами‘а-ллаху лиман хамидах. Раббана ляка-ль-хамд", "Аллах слышит того, кто Его восхваляет. Господь наш, Тебе хвала!", 22))}
{nstep(9, pose("sajda", w=70), "Саджда — земной поклон", "Со словами «Аллаху акбар» опускаемся: сначала колени, потом руки, потом лоб и нос. Три раза говорим:", mini("سُبْحَانَ رَبِّيَ الْأَعْلَى", "Субхана Раббияль-А‘ля", "Пречист мой Всевышний Господь", 24))}
{nstep(10, pose("sit", w=70), "Сидение", "Со словами «Аллаху акбар» садимся ненадолго, руки на бёдрах.")}
{nstep(11, pose("sajda", w=70), "Вторая саджда", "Снова «Аллаху акбар» — и второй земной поклон, тоже три раза «Субхана Раббияль-А‘ля».")}
</div>''', section=SEC_N)

    b.add(f'''<h1 class="title sm">Как совершать намаз · 4</h1>
<div class="nsteps">
{nstep(12, pose("stand", w=70), "Второй ракаат", "Встаём со словами «Аллаху акбар». Читаем «Бисмиллях», «аль-Фатиху», ещё одну суру — и делаем руку и две саджды так же, как в первом ракаате.")}
{nstep(13, pose("sit", w=70), "Ташаххуд", "После второй саджды садимся и читаем «Ат-тахияту», затем «Салават» и дуа (тексты — на следующих страницах).")}
{nstep(14, pose("salam", w=70), "Салям", "Поворачиваем голову направо, потом налево, и каждый раз говорим:", mini("السَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللَّهِ", "Ассаляму алейкум ва рахмату-ллах", "Мир вам и милость Аллаха", 24))}
</div>
{M.say("adam", "Вот и всё! Ты совершил намаз из двух ракаатов. МашаАллах!", "open", "wave", 100)}''', section=SEC_N)

    b.add(f'''<h1 class="title sm">Слова, которые читаем сидя</h1>
<div class="nt-lab">1. Ташаххуд — «Ат-тахияту»</div>
{txt("التَّحِيَّاتُ لِلَّهِ وَالصَّلَوَاتُ وَالطَّيِّبَاتُ، السَّلَامُ عَلَيْكَ أَيُّهَا النَّبِيُّ وَرَحْمَةُ اللَّهِ وَبَرَكَاتُهُ، السَّلَامُ عَلَيْنَا وَعَلَى عِبَادِ اللَّهِ الصَّالِحِينَ، أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا اللَّهُ، وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ",
     "Ат-тахийяту лилляхи ва-с-саляваату ва-т-таййибату. Ас-саляму ‘аляйка айюха-н-набийю ва рахмату-ллахи ва баракятух. Ас-саляму ‘аляйна ва ‘аля ‘ибади-ллахи-с-салихин. Ашхаду ал-ля иляха илля-ллах, ва ашхаду анна Мухаммадан ‘абдуху ва расулюх",
     "Приветствия, молитвы и все благие слова — Аллаху. Мир тебе, о Пророк, милость Аллаха и Его благословение. Мир нам и праведным рабам Аллаха. Свидетельствую, что нет божества, кроме Аллаха, и свидетельствую, что Мухаммад — Его раб и посланник.", 22)}
<div class="nt-lab">2. Дуа в конце намаза</div>
{txt("رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ",
     "Раббана атина фи-д-дунья хасанатан ва фи-ль-ахырати хасанатан ва кына ‘азаба-н-нар",
     "Господь наш, даруй нам в этой жизни хорошее и в будущей жизни хорошее и защити нас от огня.", 24)}''', section=SEC_N)

    b.add(f'''<h1 class="title sm">Салават</h1>
<p class="lead">После «Ат-тахияту» в последнем сидении читаем благословение Пророку ﷺ:</p>
{txt("اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ ۝ اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا بَارَكْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ",
     "Аллахумма салли ‘аля Мухаммадин ва ‘аля али Мухаммад, кама салляйта ‘аля Ибрахима ва ‘аля али Ибрахим, иннака Хамидун Маджид. Аллахумма барик ‘аля Мухаммадин ва ‘аля али Мухаммад, кама баракта ‘аля Ибрахима ва ‘аля али Ибрахим, иннака Хамидун Маджид",
     "О Аллах, благослови Мухаммада и семью Мухаммада, как Ты благословил Ибрахима и семью Ибрахима. Поистине, Ты — Достойный хвалы, Славный. О Аллах, ниспошли благодать Мухаммаду и семье Мухаммада, как Ты ниспослал её Ибрахиму и семье Ибрахима. Поистине, Ты — Достойный хвалы, Славный.", 23)}
{M.say("maryam", "Учи слова понемногу: сегодня одну строчку, завтра — следующую.", "smile", "point", 100)}''', section=SEC_N)

    fat = " ".join(f'{ayah(1, v)} <span class="aend">۝{ar_num(v)}</span>' for v in range(1, 8))
    ikh = " ".join(f'{ayah(112, v)} <span class="aend">۝{ar_num(v)}</span>' for v in range(1, 5))
    b.add(f'''<h1 class="title sm">Суры для намаза</h1>
<div class="surah"><div class="s-head"><span lang="ar" dir="rtl">سُورَةُ الْفَاتِحَة</span></div><div class="s-text" lang="ar" dir="rtl">{fat}</div></div>
<div class="nt-tr2">Бисмилляхи-р-Рахмани-р-Рахим. Аль-хамду лилляхи Рабби-ль-‘алямин. Ар-Рахмани-р-Рахим. Малики яуми-д-дин. Ийяка на‘буду ва ийяка наста‘ин. Ихдина-с-сырата-ль-мустакым. Сырата-ллязина ан‘амта ‘аляйхим, гайри-ль-магдуби ‘аляйхим ва ля-д-даллин.</div>
<div class="surah"><div class="s-head"><span lang="ar" dir="rtl">سُورَةُ الْإِخْلَاص</span></div><div class="basm" lang="ar" dir="rtl">{ayah(1, 1)}</div><div class="s-text" lang="ar" dir="rtl">{ikh}</div></div>
<div class="nt-tr2">Куль хуа-ллаху ахад. Аллаху-с-самад. Лям ялид ва лям юляд. Ва лям якун ляху куфуван ахад.</div>''', section=SEC_N, cls="qpage")

    gd = [("Руки при такбире", "до ушей", "до плеч"), ("Руки в кыяме", "под пупком, правая на левой", "на груди, правая на левой"),
          ("Руку", "спина ровная, пальцы обхватывают колени", "наклон чуть меньше, руки лежат на коленях"),
          ("Саджда", "локти отведены от тела", "локти прижаты к телу, живот к бёдрам"), ("Сидение", "сидим на левой стопе, правая стоит", "сидим на полу, обе стопы выведены вправо")]
    gh = "".join(f'<div class="gd"><b>{t}</b><p><span>мальчики</span>{a}</p><p><span>девочки</span>{c}</p></div>' for t, a, c in gd)
    b.add(f'''<h1 class="title sm">Мальчики и девочки</h1>
<p class="lead">По ханафитскому мазхабу у мальчиков и девочек есть небольшие различия:</p>
<div class="gds">{gh}</div>
<div class="pair">{adam(130, right="down")}{maryam(130, left="down")}</div>''', section=SEC_N)

    b.add(f'''<h1 class="title sm">После намаза</h1>
<div class="soft-card"><p>После намаза хорошо не вставать сразу, а немного посидеть и вспомнить Аллаха. Пророк ﷺ учил говорить:</p></div>
<div class="tasbih">
<div><b>33 раза</b><span lang="ar">سُبْحَانَ اللَّهِ</span><i>Субхана-ллах — Пречист Аллах</i></div>
<div><b>33 раза</b><span lang="ar">الْحَمْدُ لِلَّهِ</span><i>Аль-хамду лилллях — Хвала Аллаху</i></div>
<div><b>33 раза</b><span lang="ar">اللَّهُ أَكْبَرُ</span><i>Аллаху акбар — Аллах велик</i></div></div>
<div class="soft-card"><p>А потом можно сделать <b>дуа</b> своими словами: поблагодарить Аллаха, попросить за маму и папу, за друзей и за всех мусульман.</p></div>
{M.say("adam", "Считать удобно на пальчиках правой руки — так делал Пророк ﷺ.", "smile", "point", 100)}''', section=SEC_N)

    b.pages.append(f'''<section class="page about-min"><div class="am-in mt-end">
<div class="am-t">Мой абдест и мой намаз</div>
<div class="am-line"></div>
<p class="mt-p">Пусть каждый абдест делает чище сердце, а каждый намаз приближает к Аллаху.</p>
<div class="mt-kids">{adam(110, right="wave")}{maryam(110, left="wave")}</div>
<p class="mt-p" style="font-size:13px">Подготовила</p>
<div class="mt-name">Эльмаза Темиркалиева</div>
<div class="wa"><span lang="ar" dir="rtl">وَاللَّهُ أَعْلَمُ</span>Аллах знает лучше. Если мы где-то ошиблись — это от нас, а всё верное — от Аллаха.</div>
<div class="bc-y mt-y">2026</div></div></section>''')
    E.back_cover(b, "Методичка для детей: как совершать абдест и гусуль и как совершать намаз — по шагам, по ханафитскому мазхабу, вместе с Зейнеб и Юсуфом.", ar="طَهَارَتِي وَصَلَاتِي")
    return b

CSS = """
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}
.th-c{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:4mm;text-align:center}
.th-i{height:24mm;display:flex;justify-content:center;align-items:center}.th-i .wic{width:22mm;height:22mm}
.th-c b{display:block;font-size:16px;color:#3E5180;margin:1mm 0}.th-c p{font-size:12.5px;line-height:1.5;color:#4A2C27}
.wic{width:20mm;height:20mm}
.fards{display:grid;grid-template-columns:1fr 1fr;gap:4mm}.fards.f3{grid-template-columns:repeat(3,1fr)}
.fd{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:4mm;text-align:center}
.fd .ws-i{display:flex;justify-content:center}.fd b{display:block;font-size:15px;color:#3F8F86;margin-top:1mm}.fd p{font-size:12.5px;color:#4A2C27;line-height:1.5}
.wsteps{display:flex;flex-direction:column;gap:3mm}
.ws{display:flex;gap:4mm;align-items:center;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:3mm 5mm}
.ws-i{flex:none;width:22mm;height:22mm;border-radius:50%;background:#EAF4F2;display:grid;place-items:center}
.ws-b span{display:inline-grid;place-items:center;width:7mm;height:7mm;border-radius:50%;background:#3F8F86;color:#fff;font-weight:900;font-size:12px;margin-right:2mm}
.ws-b b{font-size:15.5px;color:#3E5180}.ws-b p{font-size:13.5px;line-height:1.55;color:#4A2C27;margin-top:1mm}
.nt-card{background:#FFFDF9;border:1.2px solid #DCC08A;border-radius:6mm;padding:4mm 7mm;text-align:center;display:flex;flex-direction:column;gap:2mm}
.nt-ar{font-family:"Amiri";font-weight:700;line-height:1.9;color:#2E1A16}
.nt-tr{font-size:13.5px;font-weight:700;color:#3C7FB0;line-height:1.55}
.nt-ru{font-size:12.5px;font-style:italic;color:#5C342E;line-height:1.55}
.nt-lab{font-weight:800;font-size:14px;color:#5C342E}
.nt-tr2{font-size:12.5px;line-height:1.6;color:#3C7FB0;font-weight:600;text-align:center;padding:0 4mm}
.brks{display:grid;grid-template-columns:1fr 1fr;gap:3mm}
.brk{display:flex;gap:3mm;align-items:center;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:3mm 4mm}
.brk span{font-size:26px}.brk b{font-size:14px;color:#3E5180}.brk p{font-size:12px;color:#7A5A52;line-height:1.4}
.prs{display:grid;grid-template-columns:repeat(5,1fr);gap:3mm}
.pr{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:4mm 2mm;text-align:center}
.pr b{display:block;font-size:17px;color:#3C7FB0}.pr span{font-size:11.5px;color:#B8914A;font-weight:700}.pr p{font-size:11.5px;color:#4A2C27;margin:2mm 0}
.pr em{font-style:normal;font-weight:900;font-size:13px;color:#5C342E;background:#F5E8CC;border-radius:20px;padding:1mm 3mm}
.nsteps{display:flex;flex-direction:column;gap:3mm}
.ns{display:flex;gap:4mm;align-items:center;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:2.5mm 5mm}
.ns-p{flex:none;width:30mm;display:flex;justify-content:center}
.ns-b{flex:1}
.ns-b span{display:inline-grid;place-items:center;width:7mm;height:7mm;border-radius:50%;background:#3C7FB0;color:#fff;font-weight:900;font-size:12px;margin-right:2mm}
.ns-b b{font-size:15.5px;color:#3E5180}.ns-b p{font-size:13.5px;line-height:1.55;color:#4A2C27;margin-top:1mm}
.ns-t{background:#F7F0E8;border-radius:4mm;padding:2mm 4mm;margin-top:2mm;text-align:center}
.ns-t div{font-family:"Amiri";font-weight:700;line-height:1.85;color:#2E1A16}
.ns-t i{display:block;font-style:normal;font-weight:700;font-size:12.5px;color:#3C7FB0}
.ns-t small{display:block;font-size:11.5px;color:#7A5A52;font-style:italic}
.gds{display:flex;flex-direction:column;gap:3mm}
.gd{display:grid;grid-template-columns:34mm 1fr 1fr;gap:3mm;align-items:center;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:3mm 5mm}
.gd b{font-size:14px;color:#3E5180}.gd p{font-size:12.5px;line-height:1.45;color:#4A2C27}
.gd span{display:block;font-size:10px;letter-spacing:.15em;text-transform:uppercase;font-weight:800;color:#B8914A}
.tasbih{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}
.tasbih div{background:#FFFDF9;border:1.2px solid #DCC08A;border-radius:6mm;padding:4mm;text-align:center}
.tasbih b{font-size:13px;color:#B8914A}.tasbih span{display:block;font-family:"Amiri";font-weight:700;font-size:30px;line-height:1.8;color:#3E5180}
.tasbih i{font-size:12px;color:#5C342E}
"""

if __name__ == "__main__":
    b = build()
    css = "".join((ROOT / f).read_text(encoding="utf-8") for f in ["style.css", "style2.css", "style3.css"]) + F.CSS + CM.CSS + E.CSS + (ROOT / "style4.css").read_text(encoding="utf-8") + M.CSS + CSS
    (ROOT / "namaz.html").write_text(f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Мой абдест и мой намаз</title><style>{css}</style></head><body>{"".join(b.pages)}</body></html>', encoding="utf-8")
    print("pages", len(b.pages))
