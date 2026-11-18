#!/usr/bin/env python3
"""«Мой Рамадан» — детский дневник на 30 дней с Зейнеб и Юсуфом."""
import lib
from lib import *
import cover_min as CM, extras as E, fancy as F, metod as M

SEC = ("رَمَضَانِي", "Мой Рамадан", ("#4B3A8C", "#E3DDF3"))
FRAG = qsel(2, 185, "شهر", 6)

lib.KIDNOTES = [
    ("maryam", "Рамадан — месяц добрых дел. Каждое доброе дело — звёздочка!"),
    ("adam", "Устал поститься? Это нормально. Аллах видит твоё старание."),
    ("maryam", "Не забудь сказать дуа перед ифтаром — оно принимается!"),
    ("adam", "Прочитай сегодня хотя бы одну суру — это месяц Корана!"),
]

DEEDS = ["Помочь маме приготовить ифтар", "Сказать «Ассаляму алейкум» всем дома", "Угостить соседей", "Положить монетку в копилку садака",
         "Позвонить бабушке и дедушке", "Убрать свои игрушки без напоминания", "Покормить птиц", "Нарисовать открытку для друга",
         "Прочитать суру «аль-Ихлас» 3 раза", "Помочь накрыть на стол", "Сказать маме «Я тебя люблю»", "Подарить игрушку тому, кому она нужнее",
         "Выучить новое дуа", "Не спорить и не обижаться весь день", "Полить цветы", "Принести воды папе", "Помолиться за всех мусульман",
         "Помочь младшему брату или сестре", "Сделать тасбих после намаза", "Улыбнуться каждому — это тоже садака", "Сказать спасибо тому, кто помог",
         "Помочь в уборке дома", "Отнести еду тому, кто болеет", "Сказать правду, даже если трудно", "Вспомнить и рассказать историю пророка",
         "Сделать дуа за родителей", "Прочитать «аль-Фатиху» с мамой или папой", "Простить того, кто обидел", "Приготовить подарки к празднику", "Поблагодарить Аллаха за этот месяц"]
DUAS = [("سُبْحَانَ اللَّهِ", "Субхана-ллах"), ("الْحَمْدُ لِلَّهِ", "Аль-хамду лиллях"), ("اللَّهُ أَكْبَرُ", "Аллаху акбар"), ("أَسْتَغْفِرُ اللَّهَ", "Астагфируллах"),
        ("لَا إِلَهَ إِلَّا اللَّهُ", "Ля иляха илля-ллах"), ("رَبِّ زِدْنِي عِلْمًا", "Рабби зидни ильма")]

def day_block(n):
    deed = DEEDS[n - 1]
    ar, tr = DUAS[(n - 1) % len(DUAS)]
    special = '<span class="rd-sp">✨ одна из последних 10 ночей</span>' if n >= 21 else ""
    prayers = "".join(f'<span class="rd-p"><i></i>{p}</span>' for p in ["Фаджр", "Зухр", "Аср", "Магриб", "Иша"])
    moon = '<svg viewBox="0 0 40 40" class="rd-moon"><circle cx="18" cy="20" r="14" fill="#F7D774"/><circle cx="25" cy="16" r="12" fill="#FFFDF9"/></svg>'
    return f'''<div class="rd">
<div class="rd-h">{moon}<b>День {n}</b>{special}<span class="rd-date">дата: ______</span></div>
<div class="rd-row"><span class="rd-l">Мой пост</span><span class="rd-o">☐ весь день</span><span class="rd-o">☐ полдня</span><span class="rd-o">☐ до обеда</span></div>
<div class="rd-row"><span class="rd-l">Намазы</span>{prayers}</div>
<div class="rd-row"><span class="rd-l">Доброе дело</span><span class="rd-deed">☐ {deed}</span></div>
<div class="rd-row"><span class="rd-l">Зикр дня</span><span class="rd-ar" lang="ar" dir="rtl">{ar}</span><span class="rd-tr">{tr} — 10 раз ☐</span></div>
<div class="rd-row"><span class="rd-l">Коран</span><span class="rd-line">я прочитал(-а): ____________________</span></div>
<div class="rd-row"><span class="rd-l">Благодарю Аллаха</span><span class="rd-line">за ______________________________</span><span class="rd-mood">😊 🙂 😐</span></div>
</div>'''

def build():
    b = Book()
    b.pages.append(f'''<section class="page cover-min">
<div class="cm-frame"></div>
<div class="cm-in">
<svg class="cm-moon" viewBox="0 0 60 60"><circle cx="28" cy="30" r="20" fill="#D8B26A"/><circle cx="37" cy="25" r="17" fill="#FBF6F0"/>{star(46, 44, 5, "#D8B26A")}</svg>
<div class="cm-ar" lang="ar" dir="rtl">رَمَضَانِي</div>
<div class="cm-line"></div>
<div class="cm-ru">Мой Рамадан</div>
<div class="cm-sub">Дневник на 30 дней</div>
<div class="cm-stage">{M.CM_arch()}<div class="cm-kids">{adam(150, right="wave", mood="open")}{maryam(150, left="wave", mood="open")}</div></div>
<div class="cover-name rm-name">Этот дневник ведёт: <span></span></div>
</div></section>''')

    b.add(f'''<h1 class="title sm">Дорогие взрослые</h1>
<div class="soft-card">
<p>Пост становится обязательным, когда ребёнок достигает зрелости. Но приучать к нему можно и раньше — понемногу и с радостью. Малыши могут поститься «до обеда» или «полдня», а постарше — пробовать целый день, если чувствуют себя хорошо.</p>
<p>В этом дневнике на каждый день есть маленькие задания: пост, намазы, доброе дело, зикр, Коран и благодарность. Не нужно выполнять всё — важно, чтобы ребёнок почувствовал, что Рамадан — <b>особый, тёплый и радостный месяц</b>.</p>
<p>Заполняйте дневник вместе вечером, перед сном. Хвалите за каждую галочку.</p></div>
{M.say("maryam", "Мы с Юсуфом будем поститься и делать добрые дела вместе с тобой!", "open", "wave", 120)}''', section=SEC)

    b.add(f'''<h1 class="title sm">Что такое Рамадан?</h1>
<div class="qcard"><div class="qc-ar" lang="ar" dir="rtl">{FRAG}</div><div class="qc-ru">Месяц Рамадан — тот, в котором был ниспослан Коран.</div></div>
<div class="facts">
<div class="fact"><span>🌙</span><p><b>Рамадан</b> — девятый месяц исламского календаря. Он начинается, когда на небе появляется новый месяц.</p></div>
<div class="fact"><span>🌅</span><p><b>Сухур</b> — еда перед рассветом. Пророк ﷺ говорил, что в сухуре есть баракат.</p></div>
<div class="fact"><span>🍽</span><p><b>Пост</b> — от рассвета до заката мусульмане не едят и не пьют, а ещё стараются не ссориться и говорить только хорошее.</p></div>
<div class="fact"><span>🌇</span><p><b>Ифтар</b> — разговение на закате. Начинаем с финика или воды, как Пророк ﷺ.</p></div>
<div class="fact"><span>✨</span><p><b>Ляйлят аль-Кадр</b> — Ночь могущества, лучше тысячи месяцев. Её ищут в последние 10 ночей.</p></div>
<div class="fact"><span>🎉</span><p><b>Ораза байрам</b> — праздник после Рамадана. Мы радуемся, поздравляем друг друга и дарим подарки.</p></div></div>''', section=SEC)

    b.add(f'''<h1 class="title sm">Дуа для Рамадана</h1>
<div class="nt-lab">Когда разговляемся (ифтар)</div>
{_txt("ذَهَبَ الظَّمَأُ، وَابْتَلَّتِ الْعُرُوقُ، وَثَبَتَ الْأَجْرُ إِنْ شَاءَ اللَّهُ", "Захаба-з-зама’у, ва-бталляти-ль-‘урук, ва сабата-ль-аджру ин ша-аллах", "Ушла жажда, увлажнились жилы, и награда уже записана, если пожелает Аллах.")}
{_txt("اللَّهُمَّ لَكَ صُمْتُ، وَبِكَ آمَنْتُ، وَعَلَى رِزْقِكَ أَفْطَرْتُ", "Аллахумма ляка сумту, ва бика аманту, ва ‘аля ризкыка афтарту", "О Аллах, ради Тебя я постился, в Тебя уверовал и Твоим пропитанием разговляюсь.")}
<div class="nt-lab">В последние 10 ночей</div>
{_txt("اللَّهُمَّ إِنَّكَ عَفُوٌّ تُحِبُّ الْعَفْوَ فَاعْفُ عَنِّي", "Аллахумма иннака ‘афуввун тухиббу-ль-‘афва фа‘фу ‘анни", "О Аллах, Ты Прощающий, Ты любишь прощать — прости же меня.")}''', section=SEC)

    moons = "".join(f'<div class="mn"><svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="16" fill="#fff" stroke="#D8B26A" stroke-width="1.5"/></svg><b>{i}</b></div>' for i in range(1, 31))
    b.add(f'''<h1 class="title sm">Мои 30 лун</h1>
<p class="lead">Каждый вечер закрашивай луну этого дня жёлтым. Когда все 30 лун засияют — наступит праздник!</p>
<div class="mns">{moons}</div>
<div class="pair">{adam(140, right="point", mood="smile")}{maryam(140, left="wave", mood="open")}</div>''', section=SEC)

    for p in range(15):
        b.add(f'''<h1 class="title sm">Дни {p*2+1}–{p*2+2}</h1>{day_block(p*2+1)}{day_block(p*2+2)}''', section=SEC, cls="nokn")

    sq = " ".join(f'{ayah(97, v)} <span class="aend">۝{ar_num(v)}</span>' for v in range(1, 6))
    b.add(f'''<h1 class="title sm">Ночь могущества</h1>
<div class="surah"><div class="s-head"><span lang="ar" dir="rtl">سُورَةُ الْقَدْر</span></div><div class="basm" lang="ar" dir="rtl">{ayah(1, 1)}</div><div class="s-text" lang="ar" dir="rtl">{sq}</div></div>
<div class="mean"><b>О чём эта сура?</b> Аллах ниспослал Коран в Ночь могущества. Эта ночь лучше тысячи месяцев: в неё спускаются ангелы, и до самого рассвета в ней мир и покой.</div>
<div class="soft-card"><p>В последние 10 ночей Рамадана постарайся сделать побольше добра: почитать Коран, сделать дуа, дать садака, помолиться вместе с семьёй.</p></div>''', section=SEC, cls="qpage")

    b.add(f'''<h1 class="title sm">Ораза байрам!</h1>
<div class="facts">
<div class="fact"><span>💝</span><p><b>Садака аль-фитр</b> — до праздничного намаза семья даёт садака, чтобы праздник был и у тех, кому трудно.</p></div>
<div class="fact"><span>🕌</span><p><b>Праздничный намаз</b> — утром мужчины и мальчики идут в мечеть на байрам-намаз.</p></div>
<div class="fact"><span>👗</span><p><b>Нарядная одежда</b> — надеваем лучшее, умываемся, а перед намазом можно съесть что-нибудь сладкое.</p></div>
<div class="fact"><span>🤗</span><p><b>Поздравляем</b> родных и соседей, ходим в гости к бабушкам и дедушкам, дарим подарки.</p></div></div>
<div class="qcard"><div class="qc-tr" style="font-size:20px">«Байрамынъыз мубарек олсун!»</div><div class="qc-ru">Пусть ваш праздник будет благословенным!</div></div>
{task(1, "Нарисуй, как твоя семья встречает Ораза байрам.", '<div class="draw-box sm"></div>')}''', section=SEC)

    b.add(f'''<h1 class="title sm">Мой Рамадан: итоги</h1>
<div class="sum">
<div><b>Я постился(-ась)</b><span>____ дней</span></div><div><b>Я выучил(-а) дуа</b><span>____</span></div>
<div><b>Добрых дел</b><span>____</span></div><div><b>Я прочитал(-а) Коран</b><span>__________</span></div></div>
<div class="lines memo-l"><b>Больше всего мне понравилось…</b><i></i><i></i><b>В следующем Рамадане я хочу…</b><i></i><i></i></div>
<div class="cert"><svg viewBox="0 0 60 60" width="60">{star(30, 32, 26, "#F2C14E", stroke="#fff")}</svg><p>Машаллах! Ты провёл(-а) целый Рамадан вместе с Зейнеб и Юсуфом. Пусть Аллах примет твой пост и твои добрые дела!</p></div>''', section=SEC)

    b.pages.append(f'''<section class="page about-min"><div class="am-in mt-end">
<div class="am-t">Мой Рамадан</div>
<div class="am-line"></div>
<p class="mt-p">Пусть каждый Рамадан приближает маленькое сердце к Аллаху, а добрые дела этого месяца станут привычкой на весь год.</p>
<div class="mt-kids">{adam(110, right="wave")}{maryam(110, left="wave")}</div>
<p class="mt-p" style="font-size:13px">Подготовила</p>
<div class="mt-name">Эльмаза Темиркалиева</div>
<div class="wa"><span lang="ar" dir="rtl">وَاللَّهُ أَعْلَمُ</span>Аллах знает лучше. Если мы где-то ошиблись — это от нас, а всё верное — от Аллаха.</div>
<div class="bc-y mt-y">2026</div></div></section>''')
    E.back_cover(b, "Детский дневник на 30 дней Рамадана: пост, намазы, добрые дела, зикр и благодарность — каждый день вместе с Зейнеб и Юсуфом.", ar="رَمَضَانِي")
    return b

def _txt(ar, tr, ru):
    return (f'<div class="nt-card"><div class="nt-ar" lang="ar" dir="rtl" style="font-size:27px">{ar}</div>'
            f'<div class="nt-tr">{tr}</div><div class="nt-ru">{ru}</div></div>')

CSS = """
.rm-name{position:static!important;width:150mm;margin-top:2mm}
.nt-card{background:#FFFDF9;border:1.2px solid #DCC08A;border-radius:6mm;padding:4mm 7mm;text-align:center;display:flex;flex-direction:column;gap:2mm}
.nt-ar{font-family:"Amiri";font-weight:700;line-height:1.9;color:#2E1A16}
.nt-tr{font-size:13.5px;font-weight:700;color:#4B3A8C;line-height:1.55}
.nt-ru{font-size:12.5px;font-style:italic;color:#5C342E;line-height:1.55}
.nt-lab{font-weight:800;font-size:14px;color:#5C342E}
.mns{display:grid;grid-template-columns:repeat(6,1fr);gap:3mm 4mm}
.mn{position:relative;text-align:center}.mn svg{width:100%;height:auto}
.mn b{position:absolute;inset:0;display:grid;place-items:center;font-weight:900;font-size:15px;color:#B8914A}
.rd{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:4mm 6mm;display:flex;flex-direction:column;justify-content:space-between;flex:1}
.rd-h{display:flex;align-items:center;gap:3mm;border-bottom:1px dashed #E6D8C6;padding-bottom:1.5mm}
.rd-moon{width:11mm;height:11mm}.rd-h b{font-size:21px;color:#4B3A8C}
.rd-sp{font-size:11px;font-weight:800;color:#B8914A;background:#F5E8CC;border-radius:20px;padding:.5mm 3mm}
.rd-date{margin-left:auto;font-size:13.5px;color:#7A5A52}
.rd-row{display:flex;align-items:center;gap:4mm;flex-wrap:wrap;font-size:15px;color:#4A2C27;border-bottom:1px dotted #EFE4D9;padding-bottom:2mm}
.rd-l{width:32mm;font-weight:800;font-size:13.5px;color:#7A5A52;flex:none}
.rd-o{font-weight:600}
.rd-p{display:inline-flex;align-items:center;gap:1.5mm;font-size:13.5px;font-weight:600}
.rd-p i{width:6mm;height:6mm;border-radius:50%;border:1.5px solid #8C6BB8}
.rd-deed{font-weight:700;color:#5E7F4E}
.rd-ar{font-family:"Amiri";font-weight:700;font-size:26px;color:#3E5180;line-height:1.4}
.rd-tr{font-size:14px;color:#5C342E}
.rd-line{flex:1;color:#9C8478}
.rd-mood{font-size:20px;letter-spacing:2mm}
.sum{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.sum div{background:#FFFDF9;border:1px solid #E6D8C6;border-radius:5mm;padding:4mm 5mm}
.sum b{display:block;font-size:14px;color:#4B3A8C}.sum span{font-size:18px;color:#7A5A52}
.cert{display:flex;gap:4mm;align-items:center;background:#F5E8CC;border:1.2px solid #D8B26A;border-radius:6mm;padding:4mm 6mm;margin-top:auto}
.cert p{font-size:14.5px;line-height:1.6;color:#4A2C27;font-weight:600}
"""

if __name__ == "__main__":
    b = build()
    css = "".join((ROOT / f).read_text(encoding="utf-8") for f in ["style.css", "style2.css", "style3.css"]) + F.CSS + CM.CSS + E.CSS + (ROOT / "style4.css").read_text(encoding="utf-8") + M.CSS + CSS
    (ROOT / "ramadan.html").write_text(f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Мой Рамадан</title><style>{css}</style></head><body>{"".join(b.pages)}</body></html>', encoding="utf-8")
    print("pages", len(b.pages))
