def iter(n):
    s = 1
    for i in range(n+1):
        yield s
        s *= i + 1
for l in iter(int(input('input n!: '))):
    print(l)