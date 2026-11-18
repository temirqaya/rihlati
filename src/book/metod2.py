#!/usr/bin/env python3
"""Методичка для детей 8–12 лет: «Как мы провожаем своих» — обряды и традиции.
Вдохновлено пособием З. М. Баировой «Похоронный обряд у мусульман»."""
import lib
from lib import *
import cover_min as CM, extras as E, fancy as F, metod as M

COL = ("#5E7F4E", "#DCE8D2")
SEC = ("وَدَاعُ الْأَحِبَّةِ", "Как мы провожаем своих", COL)
KULL = qsel(21, 35, "كل", 4)

lib.KIDNOTES = [
    ("adam", "Знать — значит не бояться и уметь помочь."),
    ("maryam", "Главное в эти дни — быть рядом и не оставлять человека одного."),
    ("adam", "Шариат — это обязательное, традиция — это наша народная память."),
    ("maryam", "Если что-то непонятно — спроси старших."),
    ("adam", "Каждое доброе дело — подарок для того, кто ушёл."),
    ("maryam", "Говори тихо и с уважением — так мы проявляем заботу."),
]

def say(who, text, mood="smile", pose="down", w=110):
    return M.say(who, text, mood, pose, w)

def steps(items, start=1):
    return '<div class="steps">' + "".join(f'<div class="step"><span>{i}</span><div><b>{t}</b><p>{d}</p></div></div>' for i, (t, d) in enumerate(items, start)) + '</div>'

def build():
    b = Book()
    b.pages.append(f'''<section class="page cover-min">
<div class="cm-frame"></div>
<div class="cm-in">
<svg class="cm-moon" viewBox="0 0 60 60"><circle cx="28" cy="30" r="20" fill="#D8B26A"/><circle cx="37" cy="25" r="17" fill="#FBF6F0"/>{star(46, 44, 5, "#D8B26A")}</svg>
<div class="cm-ar" lang="ar" dir="rtl" style="font-size:56px">وَدَاعُ الْأَحِبَّةِ</div>
<div class="cm-line"></div>
<div class="cm-ru">Как мы провожаем своих</div>
<div class="cm-sub">Обряды и традиции · для детей 8–12 лет</div>
<div class="cm-stage">{M.CM_arch()}<div class="cm-kids">{adam(150, right="down")}{maryam(150, left="down")}</div></div>
</div></section>''')

    b.add(f'''<h1 class="title sm">Дорогие взрослые</h1>
<div class="soft-card">
<p>В 8–12 лет дети уже понимают, что смерть необратима, и часто сами бывают на дженазе вместе со взрослыми. Они видят обряды, слышат незнакомые слова — и у них появляется много вопросов.</p>
<p>Эта книжка спокойно и бережно объясняет, <b>что происходит и зачем</b>: что предписано шариатом, а что сохраняет крымскотатарская традиция; как вести себя и как поддержать того, кто горюет.</p>
<p>Ребёнок может читать её сам, но лучше — вместе с вами, обсуждая каждую страницу. Подробности, которые могут напугать, сознательно оставлены за рамками книжки.</p></div>
{say("adam", "Мы с Зейнеб расскажем всё по порядку — спокойно и честно.", "smile", "wave", 120)}''', section=SEC)

    b.add(f'''<h1 class="title sm">Зачем об этом знать?</h1>
<div class="qcard"><div class="qc-ar" lang="ar" dir="rtl">{KULL}</div><div class="qc-ru">Каждая душа вкусит смерть.</div></div>
<div class="story"><p>Это слова из Корана. Каждый человек когда-нибудь уходит из этого мира — так устроил Аллах. Большинство людей живут долгую жизнь, а уход — это не конец, а <b>переход к Аллаху</b>.</p>
<p>Пророк Мухаммад ﷺ учил помнить об этом. Не для того, чтобы бояться, а чтобы жить с пользой: делать добро, беречь близких и ценить каждый день.</p>
<p>Когда мы знаем, как проходят обряды, нам не страшно и не странно на дженазе. И мы можем по-настоящему помочь тем, кто горюет.</p></div>''', section=SEC)

    stages = [("🌌", "Мир душ", "Аллах создал души людей."), ("🤰", "Жизнь до рождения", "Малыш растёт у мамы."),
              ("🌍", "Дунья", "Наша жизнь в этом мире — время добрых дел."), ("🌙", "Барзах", "Жизнь души после смерти до Судного дня."),
              ("🌳", "Ахират", "Вечная жизнь. Мы просим у Аллаха Рай.")]
    sh = "".join(f'<div class="stage"><span>{i}</span><b>{t}</b><p>{d}</p></div>' + ('<i>→</i>' if k < 4 else "") for k, (i, t, d) in enumerate(stages))
    b.add(f'''<h1 class="title sm">Путь человека</h1>
<p class="lead">Ислам учит, что жизнь человека не заканчивается со смертью. У души есть долгий путь:</p>
<div class="stages">{sh}</div>
<div class="soft-card"><p>Вера в жизнь после смерти — <b>Ахират</b> — одна из основ веры мусульманина. Тело остаётся на земле, а душа продолжает жить.</p>
<p>Пророк ﷺ рассказал удивительную вещь: когда верующего человека кладут в могилу, его <b>добрые дела становятся рядом и защищают его</b> — намаз, пост, садака, чтение Корана, доброта к людям.</p></div>
{say("maryam", "Значит, каждое доброе дело — это друг, который будет с нами всегда!", "open", "point", 110)}''', section=SEC)

    b.add(f'''<h1 class="title sm">Шариат и традиция</h1>
<div class="twocirc">
<div class="tc g"><b>Шариат</b><small>религия</small><p>Что обязательно: омовение, саван, дженазе-намаз, погребение, дуа за умершего. Это одинаково для мусульман всего мира.</p></div>
<div class="tc r"><b>Традиция</b><small>культура народа</small><p>Как именно мы прощаемся: наши слова, «Сув селясы», угощение эльвой и локъумом, поминальные дни.</p></div></div>
<div class="soft-card"><p>Шариат определяет, что обязательно и что дозволено. А культура сохраняет язык, песни и способы, которыми люди поддерживают друг друга <b>внутри этих границ</b>.</p>
<p>Если обычай не противоречит исламу и не выдаётся за обязательное поклонение, он может оставаться частью нашей народной памяти. В разных сёлах и семьях детали могут немного отличаться — это нормально.</p></div>''', section=SEC)

    phr = [("Когда узнаём о смерти", "«Инна лилляхи ва инна иляйхи раджиун»", "Мы принадлежим Аллаху и к Нему возвращаемся."),
           ("Когда приходим к семье", "«Эмир Аллахтан. Башынъыз сагъ олсун»", "Это произошло по повелению Аллаха. Пусть будут здравы те, кто остался."),
           ("Что отвечает семья", "«Достлар сагъ олсун»", "Пусть будут здравы друзья."),
           ("После погребения", "«Аллах рахмет эйлесин»", "Пусть Аллах смилуется над ним.")]
    ph = "".join(f'<div class="phr"><small>{w}</small><b>{p}</b><p>{t}</p></div>' for w, p, t in phr)
    b.add(f'''<h1 class="title sm">У горя есть свои слова</h1>
<p class="lead">Когда своих слов не хватает, нам помогают слова, которые говорили наши бабушки и дедушки.</p>
<div class="phrs">{ph}</div>
{task(1, "Соедини слова с ситуацией: напиши номер ситуации (1–4) в кружке.", '<div class="mini-q">' + "".join(f'<div><i>○</i>{x}</div>' for x in ["«Достлар сагъ олсун»", "«Аллах рахмет эйлесин»", "«Инна лилляхи…»", "«Башынъыз сагъ олсун»"]) + '</div>')}''', section=SEC)

    rules = [("О смерти сообщают", "Близким и знакомым обязательно говорят: так каждый может проститься и поддержать семью."),
             ("На дженазе не приглашают", "Услышал о дженазе — значит, уже приглашён. Семье не нужно никого звать."),
             ("Близкие приезжают сразу", "Не ждут особого приглашения — просто приходят и становятся рядом."),
             ("Семью кормят, а не она гостей", "Первые три дня родные и соседи приносят готовую еду, чтобы семье было легче."),
             ("Спокойная одежда", "Чёрное не обязательно — достаточно скромной, непраздничной одежды."),
             ("Горе — не для телефона", "На дженазе не фотографируют и не снимают видео. Это время уважения, а не новостей.")]
    rh = "".join(f'<div class="rule"><b>{t}</b><p>{d}</p></div>' for t, d in rules)
    b.add(f'''<h1 class="title sm">Неписаные правила</h1>
<p class="lead">Эти правила нигде не записаны, но их знают все — потому что они про заботу.</p>
<div class="rules">{rh}</div>''', section=SEC)

    s1 = [("Где проходит дженазе", "Во дворе дома, при мечети или в специальном месте — там, где есть место для омовения, молитвы и людей."),
          ("Время ожидания", "Мужчины и женщины ждут отдельно. Люди не обсуждают обычные дела — молчат, вспоминают ушедшего, делают дуа."),
          ("Последнее омовение", "Умершего бережно омывают — это последняя забота о человеке. Мужчину омывают мужчины, женщину — женщины."),
          ("«Сув селясы»", "Во время омовения у крымских татар звучит особое песнопение — его поют голосом, без музыки."),
          ("Последнее прощание", "Близкие могут войти и в последний раз побыть рядом с человеком.")]
    b.add(f'''<h1 class="title sm">Как проходит дженазе · 1</h1>
<p class="lead">Мусульмане стараются не откладывать похороны — всё совершается в тот же день или как можно скорее.</p>
{steps(s1)}''', section=SEC)

    s2 = [("Саван — кефен", "Человека заворачивают в простую белую ткань. В саване все равны — нет богатых и бедных, начальников и простых."),
          ("Наставление и вопрос", "Мулла напоминает о смерти и спрашивает: «Каким вы знали этого человека?» Люди отвечают: «Мы знали его хорошим». Ещё спрашивают о долгах — и близкие обещают их вернуть."),
          ("Дженазе-намаз", "Особая молитва за умершего. Её совершают стоя: четыре такбира, без поясных и земных поклонов. Мужчины стоят впереди."),
          ("Последний путь", "Мужчины несут табут — носилки — по несколько шагов и передают другим. Так тяжесть делят на всех."),
          ("Несколько шагов", "Женщины выходят за порог и проходят вслед несколько шагов, а потом возвращаются.")]
    b.add(f'''<h1 class="title sm">Как проходит дженазе · 2</h1>
{steps(s2, 6)}
{say("adam", "Табут несут по очереди, чтобы никто не нёс тяжесть один. Это очень мудро!", "smile", "point", 105)}''', section=SEC)

    s3 = [("Вода у порога", "Возвращаясь, люди умываются водой у порога — и только потом заходят."),
          ("Чтение «Ясин»", "Пока мужчины на кладбище, женщины вместе читают суру «Ясин» и делают дуа. Потом читают и мужчины."),
          ("Эльва и локъум", "Людей угощают эльвой и локъумом — пышками. Награду за угощение посвящают ушедшему."),
          ("Люди расходятся", "Никто не засиживается: семье нужно отдохнуть и побыть со своим горем."),
          ("Поминальные дни", "На 3-й, 7-й, 37-й, 40-й день и через год семья снова собирает людей на дуа.")]
    b.add(f'''<h1 class="title sm">После дженазе</h1>
{steps(s3, 11)}
<div class="soft-card"><p>Эти обычаи — часть крымскотатарской традиции. Они не заменяют шариат и не обязательны для каждого мусульманина, но помогают людям быть вместе.</p></div>''', section=SEC)

    b.add(f'''<h1 class="title sm">«Сув селясы» — голос прощания</h1>
<div class="story"><p>«Сув селясы» — старинное крымскотатарское песнопение. Его необычность в том, что текст звучит <b>от имени самого умершего</b>: будто человек прощается с живыми и напоминает, что этот путь однажды предстоит каждому.</p></div>
<div class="qcard verse"><p>«Теним ортая къоярлар,<br>Устюмизе сув къоярлар.<br>Бизи лютф идуб юварлар,<br>Юванлара селям олсун».</p>
<div class="qc-ru">Тело положат для омовения и омоют водой. А тем, кто делает это бережно, — приветствие мира.</div></div>
<div class="soft-card"><p>Сегодня многие уже не понимают слов, а слышат только мелодию. Поэтому так важно знать смысл — тогда песнопение снова становится посланием.</p></div>
{task(1, "Спроси у бабушки или дедушки: слышали ли они «Сув селясы»? Запиши, что они рассказали.", '<div class="lines">' + '<i></i>' * 3 + '</div>')}''', section=SEC)

    quiz = [("Свет оставляли, чтобы душа нашла дорогу.", "Нет. Свет предупреждал людей ночью не наступать на место, где было омовение."),
            ("Если хлеб нарезать иначе, случится беда.", "Нет. Способ нарезки — просто привычка, у неё нет духовных последствий."),
            ("Нож на теле защищал от злых сил.", "Нет. Раньше думали, что металл помогает сохранить тело до похорон. Это бытовая попытка, а не оберег."),
            ("Деньги под камнем — плата невидимым силам.", "Нет. Это была деликатная благодарность человеку, который потом убирал комнату.")]
    qh = "".join(f'<div class="myth"><div class="m-q"><b>Правда или нет?</b> {q}<span>☐ правда &nbsp; ☐ нет</span></div><div class="m-a">{a}</div></div>' for q, a in quiz)
    b.add(f'''<h1 class="title sm">Обычай или суеверие?</h1>
<p class="lead">Некоторые старые обычаи потом стали объяснять «мистикой». Но чаще всего это просто забытые бытовые правила.</p>
<div class="myths">{qh}</div>
<div class="soft-card"><p><b>Главная мысль:</b> обычай можно соблюдать из уважения к старшим — а можно и не соблюдать. Суеверие начинается там, где говорят: «Не сделаешь — случится беда». Уважать традицию — не значит бояться её.</p></div>''', section=SEC)

    beh = [("🤫", "Говорить тихо и спокойно"), ("🧍", "Не бегать и не играть шумно"), ("📵", "Убрать телефон"), ("👂", "Слушать старших"),
           ("🤲", "Делать дуа за ушедшего"), ("🤝", "Помогать: подать воду, принести стул")]
    bh = "".join(f'<div class="beh"><span>{i}</span>{t}</div>' for i, t in beh)
    b.add(f'''<h1 class="title sm">Если я на дженазе</h1>
<p class="lead">Дети тоже могут приходить на дженазе вместе со взрослыми. Вот как можно себя вести:</p>
<div class="behs">{bh}</div>
<div class="soft-card"><p>Если стало страшно, грустно или непонятно — это нормально. Подойди к маме или папе и скажи об этом. Можно выйти и немного побыть на свежем воздухе.</p></div>
{say("maryam", "Даже Пророк ﷺ плакал, когда умер его сын. Слёзы — это не стыдно.", "smile", "down", 105)}''', section=SEC)

    helpf = [("Что можно сказать", ["«Мне очень жаль»", "«Я рядом, если захочешь поговорить»", "«Аллах рахмет эйлесин»", "Просто обнять и посидеть рядом"]),
             ("Что лучше не говорить", ["«Не плачь»", "«Хватит грустить»", "«Я знаю, что ты чувствуешь»", "Расспрашивать о подробностях"])]
    hh = "".join(f'<div class="hf {"ok" if k == 0 else "no"}"><b>{t}</b>' + "".join(f"<p>{x}</p>" for x in xs) + '</div>' for k, (t, xs) in enumerate(helpf))
    b.add(f'''<h1 class="title sm">Как поддержать друга</h1>
<p class="lead">Если у твоего друга или одноклассника умер близкий человек, вот что поможет:</p>
<div class="hfs">{hh}</div>
<div class="soft-card"><p>Не нужно искать особые слова. Иногда лучшая поддержка — <b>просто быть рядом</b>, позвать играть, когда друг будет готов, и не обижаться, если ему пока не до игр.</p></div>''', section=SEC)

    gifts = [("🤲", "Дуа", "«Аллахумма-гфир ляху ва-рхамху» — О Аллах, прости его и помилуй."),
             ("📖", "Чтение Корана", "Мы читаем Коран и просим Аллаха передать награду ушедшему."),
             ("💝", "Садака", "Помощь бедным, угощение людей, полезное дело — от имени ушедшего."),
             ("🤝", "Вернуть долги", "Близкие возвращают долги умершего — это очень важно в исламе."),
             ("🌱", "Наши добрые дела", "Хорошие дети, которые делают дуа за родителей, — большое благо для них.")]
    gh = "".join(f'<div class="gift"><span>{i}</span><b>{t}</b><p>{d}</p></div>' for i, t, d in gifts)
    b.add(f'''<h1 class="title sm">Как мы помогаем тому, кто ушёл</h1>
<div class="gifts g5">{gh}</div>
{task(1, "Придумай одно доброе дело, которое ты сделаешь в память о близком человеке.", '<div class="lines">' + '<i></i>' * 2 + '</div>')}''', section=SEC)

    words = [("Дженазе", "прощание с умершим и молитва за него"), ("Дженазе-намаз", "особая молитва за умершего, стоя, с четырьмя такбирами"),
             ("Гусуль", "полное омовение; последнее омовение умершего"), ("Кефен", "саван — белая ткань, в которую заворачивают умершего"),
             ("Табут / салагъач", "носилки, на которых несут умершего"), ("Барзах", "жизнь души после смерти до Судного дня"),
             ("Ахират", "вечная жизнь после Судного дня"), ("Телькъин", "наставление и дуа у могилы после погребения"),
             ("«Сув селясы»", "крымскотатарское песнопение во время омовения"), ("Эльва, локъум", "угощение, награду за которое дарят умершему"),
             ("Садака", "добровольная помощь и подарок ради Аллаха"), ("Фарз-кифая", "обязанность общины: если её выполнили некоторые, она снята с остальных")]
    wh = "".join(f'<div class="w"><b>{t}</b><p>{d}</p></div>' for t, d in words)
    b.add(f'<h1 class="title sm">Маленький словарик</h1><div class="words2">{wh}</div>', section=SEC)

    b.add(f'''<h1 class="title sm">Главная мысль</h1>
<div class="bigq"><p>Обряд не возвращает нам того, кто ушёл.</p><p><b>Он возвращает нас друг другу.</b></p></div>
<div class="soft-card"><p>Обряды помогают признать, что случилось, проститься, разделить тяжесть на многих людей и сохранить добрую память. А наша вера даёт самое главное — надежду: мы принадлежим Аллаху и к Нему возвращаемся.</p></div>
<div class="pair">{adam(160, right="wave", mood="smile")}{maryam(160, left="wave", mood="smile")}</div>''', section=SEC)

    T1 = [("Что мы говорим, когда узнаём о смерти?", ["«Аллах рахмет эйлесин»", "«Инна лилляхи ва инна иляйхи раджиун»", "«Достлар сагъ олсун»"], 2),
          ("Что из этого — часть шариата?", ["Дженазе-намаз", "Угощение эльвой и локъумом", "«Сув селясы»"], 1),
          ("Что отвечает семья на слова «Башынъыз сагъ олсун»?", ["«Аминь»", "«Спасибо, что пришли»", "«Достлар сагъ олсун»"], 3),
          ("Как совершают дженазе-намаз?", ["Стоя, с четырьмя такбирами", "С поясными и земными поклонами", "Сидя"], 1),
          ("Почему в саване все равны?", ["Потому что ткань дорогая", "Нет богатых и бедных — перед Аллахом все одинаковы", "Так красивее"], 2),
          ("Зачем табут несут по очереди?", ["Чтобы быстрее дойти", "Чтобы разделить тяжесть на всех", "Так велит суеверие"], 2),
          ("Кто кормит людей в первые дни?", ["Семья умершего кормит гостей", "Родные и соседи приносят еду семье", "Никто"], 2)]
    T2 = [("На дженазе приглашают специально.", False), ("Чёрная одежда обязательна.", False),
          ("На дженазе не снимают видео и не фотографируют.", True), ("Свет оставляли, чтобы душа нашла дорогу.", False),
          ("Близкие возвращают долги умершего.", True), ("Дуа и садака помогают тому, кто ушёл.", True)]
    q1 = "".join(f'<div class="tq"><b>{n}. {q}</b><div class="to">' + "".join(f'<span>○ {o}</span>' for o in opts) + '</div></div>' for n, (q, opts, _) in enumerate(T1, 1))
    q2 = "".join(f'<div class="tf"><p>{n}. {q}</p><span>☐ верно</span><span>☐ неверно</span></div>' for n, (q, _) in enumerate(T2, 1))
    ans = "Ответы. Часть 1: " + ", ".join(f"{n} — {a}" for n, (_, _, a) in enumerate(T1, 1)) + ". Часть 2: " + ", ".join(f"{n} — {'верно' if v else 'неверно'}" for n, (_, v) in enumerate(T2, 1)) + "."
    b.add(f'''<h1 class="title sm">Проверь свои знания · 1</h1>
<p class="lead">Выбери один правильный ответ и обведи кружок.</p>
<div class="tqs">{q1}</div>''', section=SEC)
    b.add(f'''<h1 class="title sm">Проверь свои знания · 2</h1>
<p class="lead">Верно или неверно? Отметь галочкой.</p>
<div class="tfs">{q2}</div>
{task(1, "Объясни своими словами: чем шариат отличается от традиции?", '<div class="lines">' + '<i></i>' * 3 + '</div>')}
{task(2, "Как ты поддержишь друга, у которого умер близкий человек?", '<div class="lines">' + '<i></i>' * 2 + '</div>')}
<div class="answers2">{ans}</div>''', section=SEC)

    b.pages.append(f'''<section class="page about-min"><div class="am-in mt-end">
<div class="am-t">Об этой книжке</div>
<div class="am-line"></div>
<p class="mt-p">Эта книжка создана по мотивам методического материала<br><b>«Похоронный обряд у мусульман»</b><br><span class="mt-a">З. М. Баирова, психолог и теолог</span></p>
<p class="mt-p">Смыслы пособия — шариат, крымскотатарская традиция, этика и психология прощания — бережно пересказаны для детей 8–12 лет.</p>
<div class="am-line"></div>
<p class="mt-p">Для детских сердец с любовью подготовила</p>
<div class="mt-name">Эльмаза Темиркалиева</div>
<div class="mt-kids">{adam(110, right="wave")}{maryam(110, left="wave")}</div>
<div class="am-dua q" lang="ar" dir="rtl">{qsel(59, 10, "ربنا", 4)}</div>
<div class="am-dua-ru">Господь наш, прости нас и наших братьев</div>
<div class="wa"><span lang="ar" dir="rtl">وَاللَّهُ أَعْلَمُ</span>Аллах знает лучше. Если мы где-то ошиблись — это от нас, а всё верное — от Аллаха.</div>
<div class="bc-y mt-y">2026</div>
</div>{b.pnum_html(len(b.pages) + 1)}</section>''')
    E.back_cover(b, "Книжка для детей 8–12 лет о том, как мусульмане и крымские татары провожают своих: шариат и традиция, слова поддержки, обычаи и их смысл — вместе с Зейнеб и Юсуфом.", ar="وَدَاعُ الْأَحِبَّةِ")
    return b

CSS = """
.stages{display:flex;align-items:stretch;gap:1.5mm}
.stage{flex:1;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:3mm 2mm;text-align:center}
.stage span{font-size:28px}.stage b{display:block;font-size:13.5px;color:#3E5180;margin:1mm 0}.stage p{font-size:11px;line-height:1.4;color:#4A2C27}
.stages>i{align-self:center;font-style:normal;color:#C9A15B;font-weight:900}
.twocirc{display:grid;grid-template-columns:1fr 1fr;gap:6mm}
.tc{border-radius:50%;aspect-ratio:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:10mm}
.tc.g{background:#E4EDDC;border:2px solid #A8C49A}.tc.r{background:#FBEEE7;border:2px solid #E5BFAE}
.tc b{font-size:22px;color:#3E5180}.tc small{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#B8914A;font-weight:700}
.tc p{font-size:13px;line-height:1.55;color:#4A2C27;margin-top:2mm}
.phrs{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.phr{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:4mm 5mm}
.phr small{font-size:10.5px;letter-spacing:.15em;text-transform:uppercase;color:#B8914A;font-weight:700}
.phr b{display:block;font-size:15px;color:#3E5180;margin:1.5mm 0}.phr p{font-size:13px;color:#4A2C27;font-style:italic}
.mini-q{display:grid;grid-template-columns:1fr 1fr;gap:3mm;font-size:14px;font-weight:600}
.mini-q i{font-style:normal;font-size:22px;color:#5E7F4E;margin-right:2mm}
.rules{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.rule{background:#FFFDF9;border:1px solid #E6D8C6;border-top:3px solid #A8C49A;border-radius:4mm;padding:4mm 5mm}
.rule b{font-size:15px;color:#3E5180}.rule p{font-size:13.5px;line-height:1.55;color:#4A2C27;margin-top:1.5mm}
.steps{display:flex;flex-direction:column;gap:3mm}
.step{display:flex;gap:4mm;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:3.5mm 5mm;align-items:flex-start}
.step>span{flex:none;width:9mm;height:9mm;border-radius:50%;background:#5E7F4E;color:#fff;font-weight:900;display:grid;place-items:center;font-size:14px}
.step b{font-size:15px;color:#3E5180}.step p{font-size:13.5px;line-height:1.6;color:#4A2C27;margin-top:1mm}
.verse p{font-size:17px;line-height:1.8;color:#3E5180;font-style:italic;font-weight:600}
.myths{display:flex;flex-direction:column;gap:3mm}
.myth{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:3.5mm 5mm}
.m-q{font-size:14px;color:#4A2C27}.m-q b{color:#A8473B}.m-q span{display:block;margin-top:1.5mm;font-weight:700;color:#5E7F4E}
.m-a{font-size:12.5px;color:#7A5A52;margin-top:2mm;border-top:1px dashed #E6D8C6;padding-top:2mm}
.behs{display:grid;grid-template-columns:1fr 1fr;gap:3mm}
.beh{display:flex;gap:3mm;align-items:center;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:30px;padding:3.5mm 5mm;font-size:14.5px;font-weight:600}
.beh span{font-size:26px}
.hfs{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.hf{border-radius:6mm;padding:5mm}.hf.ok{background:#E4EDDC;border:1.5px solid #A8C49A}.hf.no{background:#FBEEE7;border:1.5px solid #E5BFAE}
.hf b{display:block;font-size:16px;color:#3E5180;margin-bottom:2mm}.hf p{font-size:14px;margin:1.5mm 0;color:#4A2C27}
.hf.ok p::before{content:"✓ ";color:#5E7F4E;font-weight:900}.hf.no p::before{content:"✗ ";color:#A8473B;font-weight:900}
.gifts.g5{grid-template-columns:1fr 1fr}.gifts.g5 .gift:last-child{grid-column:1/-1}
.words2{display:grid;grid-template-columns:1fr 1fr;gap:3mm}
.w{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:4mm;padding:3mm 4mm}
.w b{font-size:14.5px;color:#5E7F4E}.w p{font-size:12.5px;line-height:1.5;color:#4A2C27;margin-top:.5mm}
.qqs{display:flex;flex-direction:column;gap:3.5mm}
.qq{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:4mm;padding:3mm 5mm;display:grid;grid-template-columns:9mm 1fr;gap:1mm 3mm}
.qq span{width:8mm;height:8mm;border-radius:50%;background:#5E7F4E;color:#fff;font-weight:900;display:grid;place-items:center;font-size:13px}
.qq p{font-size:14.5px;font-weight:600;align-self:center}
.qq i{grid-column:2;border-bottom:1.5px dashed #C9D0E4;height:7mm}
.bigq{text-align:center;padding:10mm 6mm}
.tqs{display:flex;flex-direction:column;gap:2mm}
.tq{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:4mm;padding:2mm 5mm}
.tq b{font-size:14.5px;color:#3E5180}
.to{display:flex;flex-direction:column;gap:.5mm;margin-top:1mm}
.to span{font-size:13.5px;color:#4A2C27}
.tfs{display:flex;flex-direction:column;gap:2.5mm}
.tf{display:grid;grid-template-columns:1fr 26mm 28mm;align-items:center;background:#FFFDF9;border:1px solid #E6D8C6;border-radius:4mm;padding:3mm 5mm;font-size:14px}
.tf span{font-weight:700;color:#5E7F4E;font-size:13px}
.answers2{margin-top:auto;font-size:10.5px;color:#9C8478;transform:rotate(180deg);text-align:center;line-height:1.5}
.bigq p{font-size:24px;line-height:1.5;color:#5C342E}.bigq b{color:#3E5180}
"""

if __name__ == "__main__":
    b = build()
    css = "".join((ROOT / f).read_text(encoding="utf-8") for f in ["style.css", "style2.css", "style3.css"]) + F.CSS + CM.CSS + E.CSS + (ROOT / "style4.css").read_text(encoding="utf-8") + M.CSS + CSS
    html = f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Как мы провожаем своих</title><style>{css}</style></head><body>{"".join(b.pages)}</body></html>'
    (ROOT / "metodichka2.html").write_text(html, encoding="utf-8")
    print("pages", len(b.pages))
