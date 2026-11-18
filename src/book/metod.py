#!/usr/bin/env python3
"""Методичка для маленьких сердец: «Когда кто-то уходит к Аллаху».
Тот же визуальный мир (Зейнеб, Юсуф, нежный стиль). Вдохновлено пособием З. М. Баировой."""
import lib
from lib import *
import cover_min as CM, extras as E, fancy as F

COL = ("#6F86C2", "#E4EAF6")
SEC = ("لِلْقُلُوبِ الصَّغِيرَةِ", "Для маленьких сердец", COL)
INNA = qsel(2, 156, "انا", 5)

lib.KIDNOTES = [
    ("maryam", "Если хочется поплакать — можно. Я рядом."),
    ("adam", "Обними маму — ей тоже нужно тепло."),
    ("maryam", "Аллах слышит каждое наше дуа."),
    ("adam", "Хорошие воспоминания живут в сердце."),
    ("maryam", "Задавай любые вопросы — взрослые помогут."),
    ("adam", "Доброе дело — подарок для того, кого мы любим."),
]

def say(who, text, mood="smile", pose="down", w=120):
    k = adam(w, right=pose, mood=mood) if who == "adam" else maryam(w, left=pose, mood=mood)
    return f'<div class="row-kids">{k}{bubble(text, who)}</div>'

def build():
    b = Book()
    # ---------- обложка
    b.pages.append(f'''<section class="page cover-min">
<div class="cm-frame"></div>
<div class="cm-in">
<svg class="cm-moon" viewBox="0 0 60 60"><circle cx="28" cy="30" r="20" fill="#D8B26A"/><circle cx="37" cy="25" r="17" fill="#FBF6F0"/>{star(46, 44, 5, "#D8B26A")}</svg>
<div class="mt-q" lang="ar" dir="rtl">{INNA}</div>
<div class="cm-line"></div>
<div class="cm-ru">Когда кто-то<br>уходит к Аллаху</div>
<div class="cm-sub">Методичка для маленьких сердец</div>
<div class="cm-stage">{CM_arch()}<div class="cm-kids">{adam(150, right="down", mood="smile")}{maryam(150, left="wave", mood="smile")}</div></div>
</div></section>''')

    # ---------- взрослым
    b.add(f'''<h1 class="title sm">Дорогие взрослые</h1>
<div class="soft-card">
<p>Рано или поздно ребёнок встречается с утратой: уходит дедушка, бабушка, сосед или знакомый. Взрослым в эти дни и самим тяжело, а слова для ребёнка найти особенно трудно.</p>
<p>Эта книжка поможет поговорить с малышом спокойно и честно — языком, который он поймёт, и с той надеждой, которую даёт нам вера.</p>
<p>Читайте её вместе, понемногу, по одной-две странице. Остановитесь, если ребёнок устал или хочет поиграть. Отвечайте на вопросы просто и коротко — малыши часто спрашивают одно и то же много раз, и это нормально.</p>
<p>Самое главное, что ребёнку нужно услышать: <b>ты не один, мы рядом, тебя любят</b>.</p></div>
{say("maryam", "Мы с Юсуфом будем рядом на каждой странице.", "smile", "wave", 130)}''', section=SEC)

    # ---------- история: начало
    b.add(f'''<h1 class="title sm">Юсуфу грустно</h1>
<div class="story">
<p>Однажды вечером Юсуф сидел у окна и долго молчал. Зейнеб тихонько села рядом.</p>
<p>— Почему ты грустишь? — спросила она.</p>
<p>— Мой дедушка умер, — сказал Юсуф. — Мама сказала, что он ушёл к Аллаху. Я не понимаю… Я очень по нему скучаю.</p>
<p>Зейнеб взяла его за руку.</p>
<p>— Давай вместе подумаем об этом, — сказала она. — Когда говоришь о грустном вместе с кем-то, становится немножко легче.</p></div>
<div class="pair">{adam(170, right="down", mood="sad")}{maryam(170, left="down", mood="smile")}</div>''', section=SEC)

    # ---------- у всего своё время
    nature = (f'<div class="nature">'
              f'<div><svg viewBox="0 0 100 100" class="nt">{flower(50, 40, 3.2, "#E9A0B8")}<path d="M50 62 V96" stroke="#5E9E4E" stroke-width="5"/></svg><span>цветок распускается и отцветает</span></div>'
              f'<div><svg viewBox="0 0 100 100" class="nt"><path d="M50 10 Q86 40 50 92 Q14 40 50 10Z" fill="#F2B544" stroke="#C9813F" stroke-width="3"/><path d="M50 18 V88" stroke="#C9813F" stroke-width="2"/></svg><span>листья осенью опадают</span></div>'
              f'<div><svg viewBox="0 0 100 100" class="nt"><circle cx="50" cy="52" r="26" fill="#F7D774"/><path d="M8 80 H92" stroke="#9FC7E8" stroke-width="5"/></svg><span>день заканчивается закатом</span></div></div>')
    b.add(f'''<h1 class="title sm">У всего есть своё время</h1>
<div class="story"><p>Всё живое в мире создал Аллах: цветы, деревья, птиц, животных и людей. У каждого есть своё время — сколько ему жить в этом мире. Это время знает только Аллах.</p>
<p>Большинство людей живут долго-долго, до глубокой старости. А когда время заканчивается, человек уходит из этого мира и возвращается к Аллаху.</p></div>
{nature}
{task(1, "Нарисуй в рамке свой любимый цветок или дерево.", '<div class="draw-box"></div>')}''', section=SEC)

    # ---------- что значит умер
    facts = [("💛", "Тело человека перестаёт работать: он больше не дышит, не ест и не спит."),
             ("🤍", "Ему больше <b>не больно, не холодно и не страшно</b>."),
             ("🌙", "Он не вернётся домой, как раньше, — даже если мы очень сильно этого хотим."),
             ("✨", "Душа человека возвращается к Аллаху. Аллах — самый Милостивый и Милосердный.")]
    fl = "".join(f'<div class="fact"><span>{i}</span><p>{t}</p></div>' for i, t in facts)
    b.add(f'''<h1 class="title sm">Что значит «умер»?</h1>
<p class="lead">— Мама говорит, дедушка как будто уснул, — сказал Юсуф. Зейнеб покачала головой:<br>— Нет, это не сон. Давай я объясню.</p>
<div class="facts">{fl}</div>
{say("maryam", "Смерть — это не сон. Поэтому, когда ты ложишься спать, бояться не нужно: ты проснёшься утром!", "smile", "point", 120)}''', section=SEC)

    # ---------- слова
    b.add(f'''<h1 class="title sm">Слова, которые мы говорим</h1>
<p class="lead">Когда мусульмане узнают, что кто-то умер, они говорят особые слова из Корана:</p>
<div class="qcard"><div class="qc-ar" lang="ar" dir="rtl">{INNA}</div>
<div class="qc-tr">«Инна лилляхи ва инна иляйхи раджиун»</div>
<div class="qc-ru">Мы принадлежим Аллаху, и к Нему мы возвращаемся.</div></div>
<div class="soft-card"><p>Эти слова помогают, когда своих слов пока нет. А ещё мы говорим об ушедшем: <b>«Аллах рахмет эйлесин»</b> — «Пусть Аллах смилуется над ним».</p></div>
{task(1, "Повтори эти слова вместе со взрослым. Раскрась звёздочку, когда запомнишь.", f'<div class="stars-row">{"".join(f"<svg viewBox=\'0 0 60 60\' width=\'56\'>{star(30, 32, 26, chr(35)+chr(70)*6, stroke=GOLD2)}</svg>" for _ in range(3))}</div>')}''', section=SEC)

    # ---------- грустить можно
    feel = [("😢", "грустно"), ("😟", "страшно"), ("😠", "сердито"), ("😕", "непонятно"), ("🥺", "скучаю"), ("🙂", "хочется поиграть")]
    fh = "".join(f'<div class="feel"><span>{e}</span><b>{t}</b></div>' for e, t in feel)
    b.add(f'''<h1 class="title sm">Грустить — можно</h1>
<div class="story"><p>— Мне хочется плакать, — признался Юсуф. — Это стыдно?</p>
<p>— Нет! — ответила Зейнеб. — Даже наш Пророк Мухаммад ﷺ плакал, когда умер его маленький сын. Он сказал: «Глаза плачут, и сердце печалится, но мы говорим только то, чем доволен наш Господь».</p></div>
{task(1, "Что ты чувствуешь сейчас? Обведи кружком. Можно выбрать несколько — все чувства нормальные.", f'<div class="feels">{fh}</div>')}
{say("adam", "А иногда мне хочется смеяться и играть. Зейнеб говорит, что и это нормально!", "smile", "wave", 115)}''', section=SEC)

    # ---------- что помогает
    helps = ["обнять маму или папу", "поплакать", "рассказать, что чувствую", "порисовать", "сделать дуа", "погулять на улице", "посмотреть фотографии", "побыть в тишине"]
    hh = "".join(f'<div class="help"><i>♡</i>{h}</div>' for h in helps)
    b.add(f'''<h1 class="title sm">Что мне помогает, когда грустно</h1>
<p class="lead">Раскрась сердечки рядом с тем, что помогает тебе. Можно дорисовать своё!</p>
<div class="helps">{hh}<div class="help own"><i>♡</i>&nbsp;</div><div class="help own"><i>♡</i>&nbsp;</div></div>
{task(1, "Какого цвета твоя грусть? Нарисуй её облачком — а рядом нарисуй солнышко, которое её согреет.", '<div class="draw-box sm"></div>')}''', section=SEC)

    # ---------- почему дома собрались люди
    cards = [("🤲", "Все вместе молятся", "Взрослые читают суру «Ясин» и делают дуа за того, кто ушёл."),
             ("🍲", "Приносят еду", "Родные и соседи приносят семье готовую еду, чтобы маме и папе было легче."),
             ("🫓", "Угощают эльвой и локъумом", "Угощение раздают, а награду за это доброе дело дарят ушедшему."),
             ("📅", "Собираются снова", "Через несколько дней и через сорок дней родные снова собираются на дуа — чтобы вспомнить и помолиться."),
             ("🤫", "Говорят тихо", "В доме спокойно и тихо — так люди показывают уважение и заботу.")]
    ch = "".join(f'<div class="cust"><span>{i}</span><div><b>{t}</b><p>{d}</p></div></div>' for i, t, d in cards)
    b.add(f'''<h1 class="title sm">Почему дома собрались люди?</h1>
<p class="lead">— У нас дома так много людей, — удивился Юсуф. — Зачем они пришли?<br>— Чтобы семья не грустила одна, — сказала Зейнеб.</p>
<div class="custs">{ch}</div>
{say("maryam", "Когда людям тяжело, их не оставляют одних. Все помогают понемножку.", "smile", "down", 110)}''', section=SEC)

    # ---------- как я могу помочь
    acts = ["обнять маму или бабушку", "принести стакан воды", "поиграть тихо", "помочь накрыть на стол", "нарисовать открытку для семьи", "сказать: «Я тебя люблю»"]
    ah = "".join(f'<div class="act"><i>☐</i>{a}</div>' for a in acts)
    b.add(f'''<h1 class="title sm">Я тоже могу помочь!</h1>
<p class="lead">Даже маленький человек может подарить много тепла. Отметь, что ты сделаешь сегодня:</p>
<div class="acts">{ah}</div>
{task(1, "Нарисуй открытку-обнимашку для своей семьи.", '<div class="draw-box"></div>')}''', section=SEC)

    # ---------- подарки для ушедшего
    gifts = [("🤲", "Дуа", "Мы просим Аллаха простить и помиловать того, кого любим."),
             ("💝", "Садака", "Мы помогаем тем, кому трудно, и просим Аллаха передать награду ушедшему."),
             ("🌱", "Добрые дела", "Хорошие поступки — как цветы, которые мы сажаем в его честь."),
             ("💭", "Добрые воспоминания", "Мы вспоминаем хорошее, что он делал и чему нас научил.")]
    gh = "".join(f'<div class="gift"><span>{i}</span><b>{t}</b><p>{d}</p></div>' for i, t, d in gifts)
    b.add(f'''<h1 class="title sm">Подарки, которые доходят до неба</h1>
<p class="lead">— А можно что-то подарить дедушке? — спросил Юсуф.<br>— Можно! — улыбнулась Зейнеб. — Есть особые подарки.</p>
<div class="gifts">{gh}</div>
{say("adam", "Я буду делать добрые дела и дарить их дедушке!", "open", "wave", 115)}''', section=SEC)

    # ---------- моё дуа
    dua_m, dua_f = "اللَّهُمَّ اغْفِرْ لَهُ وَارْحَمْهُ", "اللَّهُمَّ اغْفِرْ لَهَا وَارْحَمْهَا"
    b.add(f'''<h1 class="title sm">Моё дуа</h1>
<p class="lead">Это короткое дуа можно говорить каждый день — после намаза или перед сном.</p>
<div class="duas">
<div class="dua-c"><small>за мужчину</small><div lang="ar" dir="rtl">{dua_m}</div><span>«Аллахумма-гфир ляху ва-рхамху»</span></div>
<div class="dua-c"><small>за женщину</small><div lang="ar" dir="rtl">{dua_f}</div><span>«Аллахумма-гфир ляха ва-рхамха»</span></div></div>
<p class="qc-ru">О Аллах, прости его (её) и помилуй.</p>
{task(1, "Обведи дуа по контуру.", f'<div class="trace-row dua-tr" dir="rtl">{trace_svg(dua_m, 50, 560, 110, base=72, y=72, pale=True)}</div>')}
{task(2, "Напиши или нарисуй своё дуа своими словами.", '<div class="lines">' + '<i></i>' * 3 + '</div>')}''', section=SEC)

    # ---------- коробочка воспоминаний
    b.add(f'''<h1 class="title sm">Моя коробочка воспоминаний</h1>
<p class="lead">Нарисуй в коробочке то, что ты помнишь о человеке, которого любишь: как вы гуляли, что он любил, чему тебя научил.</p>
<div class="memobox"><svg viewBox="0 0 600 70" class="mb-lid"><path d="M20 66 L50 8 H550 L580 66Z" fill="#E4EAF6" stroke="#6F86C2" stroke-width="3"/>{flower(300, 36, 2, "#E9A0B8")}{star(200, 36, 10, GOLD)}{star(400, 36, 10, GOLD)}</svg><div class="mb-b"></div></div>
<div class="lines memo-l"><b>Его (её) звали:</b><i></i><b>Мне нравилось, когда мы вместе…</b><i></i><i></i></div>''', section=SEC)

    # ---------- вопросы
    qa = [("Дедушка вернётся?", "Нет, он не вернётся, как раньше. Но мы можем любить его, вспоминать и делать за него дуа."),
          ("Ему больно? Ему холодно?", "Нет. Ему больше не больно, не холодно и не страшно."),
          ("Это из-за меня?", "Нет-нет! Ты ни в чём не виноват. Никакие слова или поступки ребёнка не делают так, чтобы человек умер."),
          ("А мама и папа тоже умрут?", "Большинство людей живут очень долго, до старости. Мама и папа рядом, они заботятся о тебе, и ты не останешься один."),
          ("А я?", "Ты сейчас маленький, у тебя впереди много-много жизни, игр и радости. Время каждого знает Аллах — а мы просим у Него здоровья и добра."),
          ("Где он сейчас?", "Его душа у Аллаха. Аллах самый Милостивый, и мы просим Его о милости для дедушки.")]
    qh = "".join(f'<div class="qa"><div class="qa-q">{adam(40, right="down")}<b>{q}</b></div><div class="qa-a">{maryam(40, left="down")}<p>{a}</p></div></div>' for q, a in qa)
    b.add(f'''<h1 class="title sm">Вопросы Юсуфа</h1>
<p class="lead">Юсуф задавал много вопросов. Может быть, у тебя такие же?</p>
<div class="qas">{qh}</div>''', section=SEC)

    # ---------- надежда
    b.add(f'''<h1 class="title sm">Надежда</h1>
<div class="story"><p>— Зейнеб, а мы ещё увидимся с дедушкой? — тихо спросил Юсуф.</p>
<p>— Аллах приготовил для верующих и добрых людей прекрасный Рай — сад, где нет ни болезней, ни грусти, ни слёз, — ответила Зейнеб. — Мы просим Аллаха, чтобы Он собрал нас всех вместе в Раю.</p>
<p>Юсуф улыбнулся впервые за весь день.</p></div>
{task(1, "Нарисуй самый красивый сад, какой только можешь представить.", '<div class="draw-box tall"></div>')}''', section=SEC)

    # ---------- конец истории
    b.add(f'''<h1 class="title sm">Жизнь продолжается</h1>
<div class="story"><p>Прошло несколько дней. Юсуф всё ещё иногда грустил и скучал. Но теперь он знал, что делать.</p>
<p>Каждый вечер перед сном он говорил: <b>«Аллахумма-гфир ляху ва-рхамху»</b>. По пятницам вместе с мамой он угощал соседей. А когда вспоминал, как дедушка учил его читать первые буквы, — улыбался.</p>
<p>— Знаешь, Зейнеб, — сказал Юсуф, — дедушка живёт в моём сердце. И в каждом добром деле, которое я делаю.</p></div>
<div class="pair">{adam(170, right="wave", mood="open")}{maryam(170, left="wave", mood="open")}</div>''', section=SEC)

    # ---------- советы взрослым
    tips = [("Говорите честно и просто", "«Дедушка умер. Его тело перестало работать, он больше не вернётся». Избегайте слов «уснул» или «уехал» — они пугают и запутывают ребёнка."),
            ("Разрешайте любые чувства", "Слёзы, злость, молчание и внезапная игра — нормальные реакции. Дети горюют «волнами»."),
            ("Отвечайте на вопросы — снова и снова", "Повторяющиеся вопросы помогают ребёнку постепенно понять случившееся."),
            ("Дайте ребёнку дело", "Помочь накрыть на стол, нарисовать открытку, сказать дуа — маленькое участие помогает почувствовать себя нужным."),
            ("Сохраняйте привычный распорядок", "Сон, еда, игры и прогулки в обычное время дают малышу ощущение безопасности."),
            ("Не скрывайте своё горе", "Можно плакать при ребёнке и объяснить: «Я грущу, потому что скучаю. Это пройдёт, и я рядом с тобой»."),
            ("Будьте внимательны", "Если ребёнок долго плохо спит, боится расставаться или сильно изменился, — посоветуйтесь с детским психологом.")]
    th = "".join(f'<div class="tip"><b>{t}</b><p>{d}</p></div>' for t, d in tips)
    b.add(f'<h1 class="title sm">Для взрослых: как поддержать ребёнка</h1><div class="tips">{th}</div>', section=SEC)

    # ---------- о книжке
    b.pages.append(f'''<section class="page about-min"><div class="am-in mt-end">
<div class="am-t">Об этой книжке</div>
<div class="am-line"></div>
<p class="mt-p">Эта книжка создана по мотивам методического материала<br><b>«Похоронный обряд у мусульман»</b><br><span class="mt-a">З. М. Баирова, психолог и теолог</span></p>
<p class="mt-p">Взрослые смыслы этого пособия — о вере, традиции и о том, как быть рядом с горем, — бережно пересказаны языком, понятным самым маленьким.</p>
<div class="am-line"></div>
<p class="mt-p">Для маленьких сердец с любовью подготовила</p>
<div class="mt-name">Эльмаза Темиркалиева</div>
<div class="mt-kids">{adam(110, right="wave")}{maryam(110, left="wave")}</div>
<div class="am-dua q" lang="ar" dir="rtl">{qsel(59, 10, "ربنا", 4)}</div>
<div class="am-dua-ru">Господь наш, прости нас и наших братьев</div>
<div class="wa"><span lang="ar" dir="rtl">وَاللَّهُ أَعْلَمُ</span>Аллах знает лучше. Если мы где-то ошиблись — это от нас, а всё верное — от Аллаха.</div>
<div class="bc-y mt-y">2026</div>
</div>{b.pnum_html(len(b.pages) + 1)}</section>''')

    E.back_cover(b, "Нежная книжка для детей о том, что происходит, когда близкий человек уходит к Аллаху: простые слова, чувства, дуа и надежда — вместе с Зейнеб и Юсуфом.", ar="لِلْقُلُوبِ الصَّغِيرَةِ")
    return b

def CM_arch():
    return ('<svg class="cm-arch" viewBox="0 0 300 380" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M20 370 L20 150 Q20 90 110 60 Q140 48 150 14 Q160 48 190 60 Q280 90 280 150 L280 370" fill="none" stroke="#C9A15B" stroke-width="2.5"/>'
            '<path d="M36 370 L36 156 Q36 104 118 76 Q142 66 150 40 Q158 66 182 76 Q264 104 264 156 L264 370" fill="none" stroke="#C9A15B" stroke-width="1" opacity=".6"/></svg>')

CSS = """
.mt-q{font-family:"Amiri Quran";font-size:34px;line-height:2;color:#3E5180}
.soft-card,.story{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:5mm 7mm;font-size:15px;line-height:1.75;color:#4A2C27;display:flex;flex-direction:column;gap:2.5mm}
.story{font-size:16px}
.pair{display:flex;justify-content:center;gap:14mm;margin-top:auto}
.nature{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm;text-align:center}
.nature>div{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:3mm}
.nt{width:26mm;height:26mm}.nature span{display:block;font-size:12.5px;color:#7A5A52;font-weight:600}
.draw-box{height:62mm;border:2px dashed #C9D0E4;border-radius:5mm;background:#fff}
.draw-box.sm{height:52mm}.draw-box.tall{height:110mm}
.facts{display:flex;flex-direction:column;gap:3mm}
.fact{display:flex;gap:4mm;align-items:center;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:4mm 6mm}
.fact span{font-size:28px}.fact p{font-size:15.5px;line-height:1.6;color:#4A2C27}
.qcard{background:#FFFDF9;border:1.2px solid #DCC08A;border-radius:6mm;padding:5mm 8mm;text-align:center}
.qc-ar{font-family:"Amiri Quran";font-size:40px;line-height:2.1;color:#2E1A16}
.qc-tr{font-weight:800;font-size:16px;color:#3E5180}
.qc-ru{font-size:14px;color:#7A5A52;font-style:italic;margin-top:1mm;text-align:center}
.stars-row{display:flex;gap:6mm;justify-content:center}
.feels{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}
.feel{border:1.5px dashed #C9D0E4;border-radius:50px;padding:3mm;display:flex;align-items:center;gap:3mm;justify-content:center;background:#fff}
.feel span{font-size:30px}.feel b{font-size:14px;color:#5C342E}
.helps{display:grid;grid-template-columns:1fr 1fr;gap:3mm}
.help{display:flex;align-items:center;gap:3mm;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:30px;padding:3mm 5mm;font-size:14.5px;font-weight:600;color:#4A2C27}
.help i{font-style:normal;font-size:24px;color:#E9A0B8}
.help.own{border-style:dashed}
.custs{display:flex;flex-direction:column;gap:2.5mm}
.cust{display:flex;gap:4mm;align-items:center;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:3mm 5mm}
.cust span{font-size:28px}.cust b{font-size:14.5px;color:#3E5180}.cust p{font-size:13px;color:#4A2C27;line-height:1.5}
.acts{display:grid;grid-template-columns:1fr 1fr;gap:3mm}
.act{display:flex;gap:3mm;align-items:center;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:4mm;padding:3.5mm 5mm;font-size:14.5px;font-weight:600}
.act i{font-style:normal;font-size:20px;color:#6F86C2}
.gifts{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.gift{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:6mm;padding:5mm;text-align:center}
.gift span{font-size:38px}.gift b{display:block;font-size:17px;color:#3E5180;margin:1mm 0}.gift p{font-size:13.5px;line-height:1.55;color:#4A2C27}
.duas{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.dua-c{background:#FFFDF9;border:1.2px solid #DCC08A;border-radius:6mm;padding:4mm;text-align:center}
.dua-c small{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#B8914A;font-weight:700}
.dua-c div{font-family:"Amiri";font-weight:700;font-size:30px;line-height:1.9;color:#3E5180}
.dua-c span{font-size:13px;font-weight:700;color:#5C342E}
.dua-tr .tr{height:26mm;width:100%}
.lines{display:flex;flex-direction:column;gap:7mm;padding:3mm 2mm}
.lines i{display:block;border-bottom:1.5px dashed #C9D0E4;height:6mm}
.lines b{font-size:13.5px;color:#5C342E}
.memobox{display:flex;flex-direction:column}
.mb-lid{width:100%;height:auto;display:block}
.mb-b{height:92mm;border:3px solid #6F86C2;border-top:0;border-radius:0 0 6mm 6mm;background:#fff;margin:0 3.4%}
.memo-l{gap:5mm}
.qas{display:flex;flex-direction:column;gap:2.5mm}
.qa{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:2mm 4mm}
.qa-q,.qa-a{display:flex;align-items:center;gap:3mm}
.qa-q .char,.qa-a .char{width:9mm;height:auto;flex:none}
.qa-q b{font-size:15px;color:#5E7F4E}
.qa-a p{font-size:13.5px;line-height:1.5;color:#4A2C27}
.tips{display:flex;flex-direction:column;gap:2.5mm}
.tip{background:#FFFDF9;border:1px solid #E6D8C6;border-left:3px solid #6F86C2;border-radius:3mm;padding:3mm 5mm}
.tip b{font-size:14.5px;color:#3E5180}.tip p{font-size:13px;line-height:1.55;color:#4A2C27;margin-top:1mm}
.mt-end{justify-content:center;gap:5mm}
.mt-p{font-size:15px;line-height:1.7;color:#4A2C27;max-width:140mm}
.mt-a{font-size:13px;color:#7A5A52}
.mt-name{font-weight:600;font-size:13px;color:#7A5A52;letter-spacing:.03em;margin-top:-3mm}
.mt-kids{display:flex;gap:6mm}
.mt-y{margin-top:2mm}
.am-dua.q{font-family:"Amiri Quran";margin-top:0}

"""

if __name__ == "__main__":
    b = build()
    css = "".join((ROOT / f).read_text(encoding="utf-8") for f in ["style.css", "style2.css", "style3.css"]) + F.CSS + CM.CSS + E.CSS + (ROOT / "style4.css").read_text(encoding="utf-8") + CSS
    html = f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Когда кто-то уходит к Аллаху</title><style>{css}</style></head><body>{"".join(b.pages)}</body></html>'
    (ROOT / "metodichka.html").write_text(html, encoding="utf-8")
    print("pages", len(b.pages))
