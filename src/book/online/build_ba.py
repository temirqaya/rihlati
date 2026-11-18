import sys, re; sys.path.insert(0,'/home/claude/book')
import chars
def c(fn, **k):
    s = getattr(chars, fn)(w=100, **k)
    return re.sub(r' width="100"', '', s, count=1)
SV = {
 'a_wave': c('adam', right='wave'), 'm_wave': c('maryam', left='wave'),
 'a_point': c('adam', right='point', mood='open'), 'm_point': c('maryam', left='point', mood='open'),
 'a_book': c('adam', book=True), 'm_wink': c('maryam', left='wave', mood='wink'),
 'm_smile': c('maryam', left='down'), 'a_open': c('adam', right='wave', mood='open'),
}
html = open('/home/claude/book/online/ba_template.html').read()
for k, v in SV.items(): html = html.replace('{{%s}}' % k, v)
assert '{{' not in html
open('/home/claude/book/online/Urok_Ba.html', 'w').write(html)
print(len(html))
