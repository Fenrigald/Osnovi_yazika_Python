from sys import argv
def mf():
    try:
        v, s, p = map(float, argv[1:])
        i = v * s + p
        print("Зарплата:", i)
    except ValueError:
        print("Invalid input")
mf()