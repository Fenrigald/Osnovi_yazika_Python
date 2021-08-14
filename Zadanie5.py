from functools import reduce
def pr(l1, l2):
    return l1 * l2
ml = [n for n in range(100, 1001, 2)]
print(f'List - {ml}\nResult - {reduce(pr, ml)}')