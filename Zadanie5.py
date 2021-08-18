with open('mf.txt', 'w+') as f:
    s = input('Enter numbers: ')
    f.writelines(s)
    l = s.split()
    print(sum(map(int, l)))