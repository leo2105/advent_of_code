import numpy as np
from numpy.matrixlib.defmatrix import matrix
f = open('2.txt', 'r')

lines = f.read().split('\n')
arr = list(lines[0].split(','))



for i in range(len(arr)):
    arr[i] = int(arr[i])
print(arr)

nro_days = 256
for i in range(nro_days):
    print(i)
    arr_aux = arr
    for j in range(len(arr_aux)):
        if arr[j] == 0:
            arr[j] = 6
            arr.append(8)
        else:
            arr[j] -= 1
    #print(arr)

print(len(arr))
    