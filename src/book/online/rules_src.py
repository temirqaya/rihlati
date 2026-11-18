import json
A=lambda s:f'<span class="ar">{s}</span>'
# (title ru,ct,tr), arabic, (desc ru,ct,tr)
R=[
 (('Фатха','Фатха','Fetha'),'بَ',('Чёрточка сверху — звук «а»: ба','Устюнде чызыкъ — «а» сеси: ба','Üstte çizgi — «a» sesi: ba')),
 (('Касра','Касра','Kesra'),'بِ',('Чёрточка снизу — звук «и»: би','Тюбюнде чызыкъ — «и» сеси: би','Altta çizgi — «i» sesi: bi')),
 (('Дамма','Дамма','Damme'),'بُ',('Маленький вав сверху — звук «у»: бу','Устюнде кичкене вав — «у» сеси: бу','Üstte küçük vav — «u» sesi: bu')),
 (('Сукун','Сукун','Cezm'),'أَبْ',('Кружок: буква спит, без огласовки — аб','Тёгеречик: ариф юкълай, харекесиз — аб','Halka: harf uyur, harekesiz — ab')),
 (('Шадда','Шедде','Şedde'),'أَبَّ',('Буква-двойняшка — абба','Эгиз ариф — абба','İkiz harf — abba')),
 (('Танвин','Танвин','Tenvin'),'بًا بٍ بٌ',('Двойная огласовка — бан, бин, бун','Эки хареке — бан, бин, бун','Çift hareke — ban, bin, bun')),
 (('Мадд','Медд','Med'),'بَا بِي بُو',(f'{A("ا و ي")} тянут звук на 2 счёта',f'{A("ا و ي")} сесни 2 хареке узаталар',f'{A("ا و ي")} sesi 2 hareke uzatır')),
 (('Формы буквы','Арифнинъ шекиллери','Harfin şekilleri'),'ب بـ ـبـ ـب',('отдельно · в начале · в середине · в конце','айры · башында · ортасында · сонъунда','tek başına · başta · ortada · sonda')),
 (('Одиночки','Янъгъызлар','Yalnızlar'),'ا د ذ ر ز و',('Не соединяются со следующей буквой','Сонъраки арифнен бирлешмейлер','Sonraki harfle birleşmezler')),
 (('Солнечные буквы','Кунеш арифлери','Şemsî harfler'),'الشَّمْسُ',('Лям прячется, буква удваивается','Лям сакълана, ариф экилене','Lam saklanır, harf ikizlenir')),
 (('Лунные буквы','Ай арифлери','Kamerî harfler'),'الْقَمَرُ',('Лям видно и слышно','Лям корюне ве эшитиле','Lam görünür ve duyulur')),
 (('Калькаля','Къалкъале','Kalkale'),'ق ط ب ج د',('С сукуном буква подпрыгивает, как мячик','Сукуннен ариф топчыкъ киби сычрай','Cezmli harf top gibi zıplar')),
 (('Толстые буквы','Къалын арифлер','Kalın harfler'),'خ ص ض غ ط ق ظ',('Звучат «полным ртом»','«Толу агъызнен» эшитилелер','«Dolu ağızla» okunur')),
 (('Гунна','Гунна','Gunne'),'نّ مّ',('Тянем носом на 2 счёта','Бурундан 2 хареке узатамыз','Burundan 2 hareke uzatırız')),
 (('Нун с сукуном','Сукунлы нун','Cezmli nun'),'نْ',(
   f'<div class="rw"><b>Изхар</b>{A("ء ه ع ح غ خ")}</div><div class="rw"><b>Идгам</b>{A("ي ر م ل و ن")}</div><div class="rw"><b>Икляб</b>{A("ب")}</div><div class="rw"><b>Ихфа</b><span>остальные 15</span></div>',
   f'<div class="rw"><b>Изхар</b>{A("ء ه ع ح غ خ")}</div><div class="rw"><b>Идгъам</b>{A("ي ر م ل و ن")}</div><div class="rw"><b>Икъляб</b>{A("ب")}</div><div class="rw"><b>Ихфа</b><span>къалгъан 15</span></div>',
   f'<div class="rw"><b>İzhar</b>{A("ء ه ع ح غ خ")}</div><div class="rw"><b>İdgam</b>{A("ي ر م ل و ن")}</div><div class="rw"><b>İklâb</b>{A("ب")}</div><div class="rw"><b>İhfâ</b><span>kalan 15</span></div>')),
 (('Мим с сукуном','Сукунлы мим','Cezmli mim'),'مْ',(
   f'<div class="rw"><b>Ихфа губной</b>{A("ب")}</div><div class="rw"><b>Идгам</b>{A("م")}</div><div class="rw"><b>Изхар губной</b><span>остальные</span></div>',
   f'<div class="rw"><b>Дудакъ ихфасы</b>{A("ب")}</div><div class="rw"><b>Идгъам</b>{A("م")}</div><div class="rw"><b>Дудакъ изхары</b><span>къалгъанлары</span></div>',
   f'<div class="rw"><b>İhfâ-i şefevî</b>{A("ب")}</div><div class="rw"><b>İdgam</b>{A("م")}</div><div class="rw"><b>İzhar-ı şefevî</b><span>diğerleri</span></div>')),
 (('Длинный мадд','Узун медд','Uzun med'),'آ',(
   '<div class="rw"><b>Естественный</b><span>2 счёта</span></div><div class="rw"><b>Слитный</b><span>4–5 счётов</span></div><div class="rw"><b>Обязательный</b><span>6 счётов</span></div>',
   '<div class="rw"><b>Табиий</b><span>2 хареке</span></div><div class="rw"><b>Муттасыл</b><span>4–5 хареке</span></div><div class="rw"><b>Лязим</b><span>6 хареке</span></div>',
   '<div class="rw"><b>Tabiî</b><span>2 hareke</span></div><div class="rw"><b>Muttasıl</b><span>4–5 hareke</span></div><div class="rw"><b>Lâzım</b><span>6 hareke</span></div>')),
]
out={}
for li,lang in enumerate(['ru','ct','tr']):
    out[lang]=json.dumps([[t[li],a,d[li]] for t,a,d in R],ensure_ascii=False)
json.dump(out,open('/home/claude/book/online/rules_js.json','w'),ensure_ascii=False)
print(out['ct'][:300])
