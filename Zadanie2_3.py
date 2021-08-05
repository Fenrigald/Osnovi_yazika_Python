md = {1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr', 5: 'may', 6: 'jun', 7: 'jul', 8: 'aug', 9: 'sen', 10: 'oct', 11: 'nov',
      12: 'dec'}
ml = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
m = int(input())
print(f'Через словарь: {md[m]}')
print(f'Через список: {ml[m-1]}')