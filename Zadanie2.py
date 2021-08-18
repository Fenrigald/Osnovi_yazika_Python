with open('mf.txt', 'r') as f:
    ml = f.readlines()
    print(f'Strings - {len(ml)}')
    for w in range(len(ml)):
        nl = ml[w].split()
        print(f'In {w + 1}st string {len(nl)} words')