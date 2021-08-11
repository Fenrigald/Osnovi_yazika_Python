def sm():
    r = 0
    while True:
        ml = input().split()
        for i in ml:
            if i == '!':
                return r
            r += int(i)
        print(f"Сумма чисел: {r}. Нажмите'!' для выхода")
print(sm())