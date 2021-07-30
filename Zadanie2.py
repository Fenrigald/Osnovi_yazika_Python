s = int(input())
h = s // 3600
m = (s - h * 3600) // 60
s = s - h * 3600 - m * 60
print(f'{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}')