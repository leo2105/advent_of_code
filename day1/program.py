import numpy as np
f = open('b.txt', 'r')

lines = f.read().split('\n')
arr = []
print(lines)
cont = 0

n = 3
arr.append(0)
for i in range(len(lines)-1):
    nro = int(lines[i])
    arr.append(nro + arr[i])

a = 1000
for i in range(len(arr)-n):
    nro = arr[i+n]-arr[i]
    if nro > a:
        cont += 1
    a = nro

print(cont)
