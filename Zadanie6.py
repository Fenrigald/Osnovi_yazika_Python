def int_f():
    sr = input().split()
    for j in sr:
        for i in j:
            if 65 <= ord(i) <= 90:
                print('Поменьше!')
                break
        print(j.title(), end = ' ')
int_f()