from random import randint

ml = [randint(0, 10) for i in range(10)]
nml = [ml[n] for n in range(1,len(ml)) if ml[n] > ml[n - 1]]
print(ml)
print(nml)

#for n in range(1, len(ml)):
    #if ml[n] > ml[n - 1]:
        #print(ml[n])