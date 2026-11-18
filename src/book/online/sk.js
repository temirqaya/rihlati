// ---------- Раздел 3: сукун и шадда ----------
const SUK = 'ْ', SHD = 'ّ';
const VOW = ['أَ','إِ','أُ'];
const SKL = [
  {t:'Сукун', icon:'أَبْ'},
  {t:'Шадда', icon:'أَبَّ'}];
const SK_READ = [ 'بتدرسشفقكلمن'.split(''), 'بتجدرسشصطعقلمن'.split('') ];
const SK_UL0 = UL.filter(l => l !== 'ج');            // для «звуковых» вопросов
const SKUL = () => SKi===0 ? SK_UL0 : SK_UL0.filter(l => SK_READ[1].includes(l));   // только буквы, у которых есть запись
const sukS = (l, v) => VOW[v] + l + SUK;              // أَبْ
const shdS = (l, v) => 'أَ' + l + HV[v].m + SHD;      // أَبَّ  (огласовка + шадда)
const sukSnd = (l, v) => HV[v].v + TRL[l];            // «аб»
const shdSnd = (l, v) => 'а' + TRL[l] + TRL[l] + HV[v].v;   // «абба»
let SKi = 0;

function buildSk(i){
  SKi = i; got = new Set(); cur = 0; idx = i; N = 8; STEPS = [2,3,4,5,6]; CSTEP = 5;
  MODE = 'S'; KEY = 's'+i; AGAIN = () => { buildSk(i); go(0); }; NEXTH = i < SKL.length-1 ? 's-'+(i+2) : 't-1';
  const [s1, s2] = speaker(i+1);
  const hero = (who, kind) => CH[who + '_' + kind];
  const T = SKL[i];
  $('#tAr').innerHTML = g(T.icon); $('#tRu').textContent = `Сукун и шадда ${i+1} из 2 · ${T.t}`;
  const greet = i===0 ? 'Сегодня мы узнаем, как буква умеет спать!' : 'Сегодня познакомимся с буквой-двойняшкой!';
  const meet = i===0 ? `
    <div class="meet">
      <div class="letterbox skbox"><div class="skparts" id="skParts"><span class="big">${g('أَ')}</span><span class="skplus">+</span><span class="big">${g('بْ')}</span></div>
        <span class="big hbig" id="skJoin" hidden>${g('أَبْ')}</span></div>
      <div class="meetcol">
        <p class="lead" id="meetText">Видишь маленький кружок над буквой Ба? Это <b>сукун</b>. Буква с ним спит: у неё нет своего гласного звука.</p>
        <button class="btn rose" id="addDot">Приклеить к слогу</button>
        <div id="meetMore" hidden style="display:flex;flex-direction:column;gap:12px;align-items:center">
          <div class="name">Сукун <span class="arn">سُكُونٌ</span></div>
          <div class="mnemo"><span class="hsign">${SKSVG}</span><span>Кружок <b>сверху</b> — буква спит, читаем её вместе со слогом перед ней: <b>«аб»</b></span></div>
          <div class="snd">Сукун — как маленькая подушка: буква на ней спит! Читаем коротко и чётко.</div>
          <button class="btn" id="say">Скажем вместе: «аб!»</button>
        </div>
      </div>
    </div>
    <div class="side"><div class="hero sm">${hero(s1,'point')}</div><div class="bubble" id="meetBubble">Нажми на кнопку — и спящая буква приклеится к слогу.</div></div>` : `
    <div class="meet">
      <div class="letterbox skbox"><div class="skparts" id="skParts"><span class="big">${g('أَبْ')}</span><span class="skplus">+</span><span class="big">${g('بَ')}</span></div>
        <span class="big hbig" id="skJoin" hidden>${g('أَبَّ')}</span></div>
      <div class="meetcol">
        <p class="lead" id="meetText">Одна Ба спит, другая говорит «ба». А если их соединить?</p>
        <button class="btn rose" id="addDot">Соединить двойняшек</button>
        <div id="meetMore" hidden style="display:flex;flex-direction:column;gap:12px;align-items:center">
          <div class="name">Шадда <span class="arn">شَدَّةٌ</span></div>
          <div class="mnemo"><span class="hsign">${SHSVG}</span><span>Значок как маленькая «ш» — буква звучит <b>два раза</b>: <b>«абба»</b></span></div>
          <div class="snd">Шадда — буква-двойняшка: первая половина спит, вторая читается с огласовкой. Особые двойняшки <span class="arin sm">نّ</span> и <span class="arin sm">مّ</span> тянем носом на 2 счёта — это гунна.</div>
          <button class="btn" id="say">Скажем вместе: «абба!»</button>
        </div>
      </div>
    </div>
    <div class="side"><div class="hero sm">${hero(s1,'point')}</div><div class="bubble" id="meetBubble">Нажми на кнопку — и буквы станут двойняшкой.</div></div>`;
  $('#screens').innerHTML = `
  <section data-s="0">
    <div class="duo">
      <div class="hero"><div class="bubble">Ассаляму алейкум!</div>${hero(s1,'wave')}</div>
      <div class="hero"><div class="bubble">${greet}</div>${hero(s2,'wave')}</div>
    </div>
    <button class="btn" data-go="1">Бисмиллях, начинаем!</button>
  </section>
  <section data-s="1">${meet}</section>
  <section data-s="2">
    <div class="side"><div class="hero sm">${hero(s2,'book')}</div><div class="bubble">${i===0 ? 'Читаем справа налево: «аб — иб — уб». Последняя буква спит.' : 'Читаем: «абба — абби — аббу». Буква звучит два раза.'}</div></div>
    <div class="grid skread" id="hread"></div>
    <div class="row"><span class="count" id="hpageN"></span><button class="btn" id="hpageNext">Дальше</button></div>
  </section>
  <section data-s="3">
    <div class="side"><div class="hero sm">${hero(s2,'point')}</div><div class="bubble" id="hqQ"></div></div>
    <div class="cards tall" id="hq"></div>
    <div class="hint" id="hqHint"></div>
    <div class="count" id="hqN"></div>
  </section>
  <section data-s="4">
    <div class="side"><div class="hero sm">${hero(s1,'book')}</div><div class="bubble">${i===0 ? 'Обведи слог и не забудь кружок сукуна!' : 'Обведи слог: и шадду, и огласовку!'}</div></div>
    <div class="tracewrap" id="tracewrap"><canvas id="cv"></canvas></div>
    <div class="row"><div class="colors" id="colors"></div><button class="btn soft" id="clear">Стереть</button><button class="btn soft" id="newSyl">Другой слог</button><button class="btn" id="traceDone">Готово!</button></div>
  </section>
  <section data-s="5">
    <div class="row"><h2>${i===0 ? 'Найди спящую букву!' : 'Поймай двойняшку!'}</h2><span class="timer" id="timer"></span><span class="count">Поймали: <b id="ccount">0</b></span></div>
    <div class="field" id="field"><div class="overlay" id="catchStart"><p class="lead" id="catchLead"></p><button class="btn rose" id="catchGo">Старт!</button></div></div>
  </section>
  <section data-s="6">
    <h2>Быстрый взгляд</h2>
    <p class="lead">Как читается этот слог? Скажите вслух, а потом проверим.</p>
    <div class="flash tall"><span class="g" id="flash"></span></div>
    <div class="answer" id="answer"></div>
    <div class="row"><button class="btn soft" id="reveal">Проверить</button><button class="btn" id="flashNext">Следующий</button></div>
    <div class="count" id="fround"></div>
  </section>
  <section data-s="7" class="final">
    <h2>Машаллах! Ты молодец!</h2>
    <div class="stars" id="finalStars"></div>
    <div class="duo">
      <div class="hero sm"><div class="bubble">${i===0 ? 'Теперь ты знаешь сукун — спящую букву!' : 'Теперь ты знаешь шадду — букву-двойняшку!'}</div>${hero(s1,'open')}</div>
      <div class="hero sm"><div class="bubble">${i===0 ? 'Следующий урок — Шадда. До встречи, ин шаа Аллах!' : 'Скоро новые уроки, ин шаа Аллах!'}</div>${hero(s2,'wink')}</div>
    </div>
    <div class="dua">رَبِّ زِدْنِي عِلْمًا</div>
    <p class="lead">«Господи, прибавь мне знаний»</p>
    <div class="row"><button class="btn soft" id="again">Ещё раз</button>${i===0 ? '<button class="btn sage" id="nextLetter">Дальше: Шадда →</button>' : ''}<button class="btn soft" id="toMap2">На карту</button></div>
  </section>`;
  $('#path').innerHTML = Array.from({length:N},(_,k)=>(k?'<i></i>':'')+'<b></b>').join('');
  drawStars($('#stars'));
  const lettersAll = SL.slice(1).filter(l => !'وي'.includes(l));
  if(i===0){
    CLEAD = 'Лопай только шарики, где буква <b>спит</b> — с кружком сукуна';
    CDONE = 'спящие буквы';
    CPICK = () => { const l = rnd(lettersAll), hit = Math.random() < 0.5, v = Math.floor(Math.random()*3); return [hit ? sukS(l,v) : syl(l,v), hit]; };
    TR = sukS(rnd(SKUL()), Math.floor(Math.random()*3));
  } else {
    CLEAD = 'Лопай только шарики с <b>двойняшкой</b> — со значком шадды';
    CDONE = 'двойняшки';
    CPICK = () => { const l = rnd(SK_READ[1]), hit = Math.random() < 0.5, v = Math.floor(Math.random()*3); return [hit ? shdS(l,v) : sukS(l,v), hit]; };
    TR = shdS(rnd(SKUL()), Math.floor(Math.random()*3));
  }
  wire(); wireS();
}

function wireS(){
  const join = $('#skJoin');
  $('#addDot').onclick = () => { sfx('magic'); $('#skParts').hidden = true; join.hidden = false; bounceEl(join); $('#addDot').hidden = true; $('#meetMore').hidden = false;
    $('#meetText').innerHTML = SKi===0 ? 'Вот так! Спящая буква приклеилась:' : 'Вот так! Получилась двойняшка:'; $('#meetBubble').textContent = 'Нажми на слог, он подпрыгнет!'; };
  join.onclick = () => bounceEl(join);
  $('#say').onclick = () => { bounceEl(join); say(SKi===0 ? sukS('ب',0) : shdS('ب',0)); $('#meetBubble').textContent = SKi===0 ? '«аб»! Машаллах!' : '«абба»! Машаллах, как красиво!'; confetti(40); };
  $('#hpageNext').onclick = () => { if(hpage < skPages()-1){ hpage++; drawSkRead(); } else { award(2); go(3); } };
  $('#newSyl').onclick = () => { const v = Math.floor(Math.random()*3), l = rnd(SKUL()); TR = SKi===0 ? sukS(l,v) : shdS(l,v); sizeCanvas(); };
  $('#reveal').onclick = () => { const [l,v] = hseq[fr]; $('#answer').textContent = '«' + (SKi===0 ? sukSnd(l,v) : shdSnd(l,v)) + '»'; say(SKi===0 ? sukS(l,v) : shdS(l,v)); };
  $('#flashNext').onclick = () => { if(fr < hseq.length-1){ fr++; showSkFlash(); } else { award(6); go(7); } };
}

const skPages = () => Math.ceil(SK_READ[SKi].length / 3);
function drawSkRead(){
  const part = SK_READ[SKi].slice(hpage*3, hpage*3+3);
  const f = SKi===0 ? sukS : shdS;
  $('#hread').innerHTML = part.map(l => [0,1,2].map(v => `<button class="tile${(window.VOICE||{})[f(l,v)]?' hasv':''}" data-t="${f(l,v)}">${g(f(l,v))}</button>`).join('')).join('');
  $$('#hread .tile').forEach(t => t.onclick = () => { bounceEl(t); say(t.dataset.t); });
  $('#hpageN').textContent = `${hpage+1} из ${skPages()}`;
  $('#hpageNext').textContent = hpage < skPages()-1 ? 'Дальше' : 'Прочитали!';
}

function drawSkQuiz(){
  const h = $('#hqHint'); if(!h || MODE !== 'S') return; h.textContent = '';
  $('#hqN').textContent = `Вопрос ${Math.min(hround+1,5)} из 5`;
  if(hround < 2){
    const l = rnd(SK_READ[SKi]), v = Math.floor(Math.random()*3);
    const opts = SKi===0 ? [[sukS(l,v),1],[syl(l,v),0],[syl(l,(v+1)%3),0]] : [[shdS(l,v),1],[sukS(l,v),0],[syl(l,v),0]];
    $('#hqQ').innerHTML = SKi===0 ? 'Где <b>спит</b> буква? Найди слог с сукуном.' : 'Где <b>двойняшка</b>? Найди слог с шаддой.';
    $('#hq').innerHTML = shuffle(opts).map(([t,ok]) => `<button class="card" data-ok="${ok}">${g(t)}</button>`).join('');
    $$('#hq .card').forEach(c => c.onclick = () => skAnswer(c, c.dataset.ok === '1', SKi===0 ? 'Тут нет кружка сукуна. Попробуй ещё!' : 'Тут нет значка шадды. Попробуй ещё!'));
  } else {
    const l = rnd(SKUL()), t = Math.floor(Math.random()*3), f = SKi===0 ? sukS : shdS, sn = SKi===0 ? sukSnd : shdSnd;
    $('#hqQ').innerHTML = `Какой слог читается <b>«${sn(l,t)}»</b>?`;
    $('#hq').innerHTML = shuffle([0,1,2]).map(v => `<button class="card" data-v="${v}" data-l="${l}">${g(f(l,v))}</button>`).join('');
    $$('#hq .card').forEach(c => c.onclick = () => skAnswer(c, +c.dataset.v === t, `Это «${sn(l,+c.dataset.v)}». Попробуй ещё!`));
  }
}
function skAnswer(c, ok, wrong){
  const h = $('#hqHint');
  if(ok){ sfx('ok'); c.classList.add('ok'); h.style.color = 'var(--sage)'; h.textContent = 'Правильно! Машаллах!'; setTimeout(() => say(c.textContent.trim()), 250);
    hround++; if(hround >= 5){ award(3); $('#hqN').textContent = 'Все 5 вопросов!'; } else setTimeout(drawSkQuiz, 1500); }
  else { shakeEl(c); h.style.color = 'var(--rose)'; h.textContent = wrong; }
}

function showSkFlash(){ const [l,v] = hseq[fr], t = SKi===0 ? sukS(l,v) : shdS(l,v);
  $('#flash').textContent = t; $('#flash').style.transform = `translateY(${sh(t)})`; $('#answer').textContent = '';
  $('#fround').textContent = `${fr+1} из ${hseq.length}`; $('#flashNext').textContent = fr===hseq.length-1 ? 'Закончить' : 'Следующий'; bounceEl($('#flash').parentNode); }

function enterS(i){
  if(i===1){ $('#skParts').hidden = false; $('#skJoin').hidden = true; $('#addDot').hidden = false; $('#meetMore').hidden = true; }
  if(i===2){ hpage = 0; drawSkRead(); }
  if(i===3){ hround = 0; drawSkQuiz(); }
  if(i===6){ hseq = shuffle(Array.from({length:6}, () => [rnd(SKUL()), Math.floor(Math.random()*3)])); fr = 0; showSkFlash(); }
}

const SKSVG = '<svg viewBox="0 0 60 70" aria-hidden="true"><rect x="14" y="26" width="32" height="26" rx="8" fill="#EDE3D3"/><circle cx="30" cy="12" r="7" fill="none" stroke="#D9998A" stroke-width="5"/></svg>';
const SHSVG = '<svg viewBox="0 0 60 70" aria-hidden="true"><rect x="14" y="26" width="32" height="26" rx="8" fill="#EDE3D3"/><path d="M16 8 q2 10 8 8 q3 -1 4 -8 q1 9 7 8 q4 -1 5 -8" stroke="#D9998A" stroke-width="4.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
