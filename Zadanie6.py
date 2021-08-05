a = int(input())
b = int(input())
d = 1
while a < b:
    a *= 1.1
    d += 1
print(f'На {d}-й день спортсмен достиг результата - не менее {b} км.')