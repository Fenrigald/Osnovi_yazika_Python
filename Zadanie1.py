def thu(a, b):
    try:
        a = int(a)
        b = int(b)
        return a / b
    except ZeroDivisionError:
        return 'Try again'
print(thu(4,0))