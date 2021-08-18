with open('mf.txt', 'r') as fl:
    s = []
    p = []
    ml = fl.read().split('\n')
    for j in ml:
        j = j.split()
        if int(j[1]) < 20000:
            p.append(j[0])
        s.append(j[1])
print(f'less then 20000 - {p} "\n" Average salary - {sum(map(int, s)) / len(s)}')