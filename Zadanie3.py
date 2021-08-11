def mf(a1, a2, a3):
    ml = [a1, a2, a3]
    ml.remove(min(ml))
    return sum(ml)
print(mf(1, 2, 3))