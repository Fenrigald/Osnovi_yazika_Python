import json

with open('mf.txt', 'r+', encoding='utf-8') as f:
    s = []
    pr = {}
    ap = {}
    av = 0
    prof = 0
    i = 3
    for l in f:
        n, firm, earn, dmg = l.split()
        t = int(earn) - int(dmg)
        if t >= 0:
            prof = prof + t
        else:
            i -= 1
        pr[n] = t
    s.append(pr)
    (av) = prof / i
    ap['Average profit - '] = round(av)
    s.append(ap)
    print(s)
with open('profit.json', 'a+', encoding='utf-8') as jf:
    json.dump(s, jf)