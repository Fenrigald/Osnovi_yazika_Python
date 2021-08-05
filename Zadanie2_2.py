ml = list(input())
k = 0
for i in range(1,len(ml),2):
    ml[i-1], ml[i] = ml[i], ml[i-1]
print(ml)