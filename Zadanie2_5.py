ml = [7, 5, 3, 3, 2]
c = int(input())
for i, n in enumerate(ml):
    if c == n:
        ml.insert(i, c)
        break
print(ml)
