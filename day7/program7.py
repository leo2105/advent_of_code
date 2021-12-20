import numpy as np
f = open('2.txt', 'r')

lines = f.read().split('\n')
arr = list(lines[0].split(','))
arr = [int(x) for x in arr]
inf, sup = min(arr), max(arr)

min_val, min_ = -1, 1e10
for a in range(inf, sup+1):
    suma = 0
    for b in arr:
        diff = abs(b-a)
        suma += int((diff*(diff+1))/2)
    if suma < min_:
        min_ = suma
        min_val = a
print(min_val, min_)


