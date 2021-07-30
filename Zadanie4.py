c = int(input())
s = c % 10
while c > 1:
    c = c // 10
    if c % 10 > s:
        s = c % 10
print(s)
