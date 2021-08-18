with open('mf.txt', 'w') as f:
    while True:
        s = input('Enter data: ')
        f.write(f'{s}\n')
        if not s:
            break