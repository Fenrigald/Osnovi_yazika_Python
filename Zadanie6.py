#a)
from itertools import count
iter = count(int(input('Точка отсчета: ')))
for i in range(20):
    print(next(iter))

#b)
from itertools import cycle
from random import randint
ml = [randint(0, 10) for n in range(5)]
iter2 = cycle(ml)
print('List - ', ml)
print('IterList - ', end = '')
for i in range(len(ml)):
    print(next(iter2), end = ' ')