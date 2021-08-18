n = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
mt = []
with open('mf.txt', 'r+') as f:
    with open('mnf.txt', 'r+') as nf:
        l = f.readlines()
        for i in l:
            i = i.split(' ', 1)
            mt.append(n[i[0]] + ' ' + i[1])
        nf.writelines(mt)
