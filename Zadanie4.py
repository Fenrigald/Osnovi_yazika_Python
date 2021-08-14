from random import randint

ml = [randint(0, 10) for i in range(30)]
nml = [n for n in ml if ml.count(n) == 1]
print('list: ', ml)
print('Nonrepeatable elems: ', nml)