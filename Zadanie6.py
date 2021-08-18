s = {}
with open('mf.txt', encoding="utf-8") as f:
    for l in f:
        pr, h = l.split(':')
        prs = sum(map(int, "".join([i for i in h if i == ' ' or '9' >= i >='0']).split()))
        s[pr] = prs
    print(f'All hours - {s}')