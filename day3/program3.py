"""
import numpy as np
f = open('f.txt', 'r')

d = {'aim':0, 'depth':0, 'forward':0}

lines = f.read().split('\n')[:-1]
print(lines)
cont = 0
n = len(lines[0])
arr = np.zeros(n)

for line in lines:
    #print(line)
    for i, char in enumerate(line):
        if char == '1':
            arr[i] += 1
        else: 
            arr[i] -= 1

gamma_rate = 0
for i, a in enumerate(arr):
    bit = 1 if a > 0 else 0
    gamma_rate += (bit * (1<<(n-1-i)))

eps_rate = (1<<n)-1 - gamma_rate

print(gamma_rate * eps_rate)
"""
# ------------------

import numpy as np
f = open('test2.txt', 'r')

lines = f.read().split('\n')
n, m = len(lines), len(lines[0])
valid_arrays = np.ones(n)

for col in range(m):
    cont = 0
    for fil in range(n):
        if not valid_arrays[fil]:
            continue
        if lines[fil][col] == '1':
            cont += 1
        else:
            cont -= 1

    id_to_check = '1' if cont >= 0 else '0'
    

    for fil in range(n):
        if lines[fil][col] != id_to_check:
            valid_arrays[fil] = 0


for i, a in enumerate(valid_arrays):
    if a == 1:
        arr_num = lines[i]

bin2dec_num_1 = 0
for i in range(len(arr_num)):
    bit = 1 if int(arr_num[i]) > 0 else 0
    bin2dec_num_1 += (bit * (1<<(len(arr_num)-1-i)))


valid_arrays = np.ones(n)

for col in range(m):
    cont = 0
    for fil in range(n):
        if not valid_arrays[fil]:
            continue
        if lines[fil][col] == '1':
            cont += 1
        else:
            cont -= 1

    id_to_check = '1' if cont < 0 else '0'

    for fil in range(n):
        if lines[fil][col] != id_to_check:
            valid_arrays[fil] = 0
    
    cont1 = 0
    for fil in range(n):
        if valid_arrays[fil] == 1:
            cont1 += 1
    
    if cont1 == 1:
        break

for i, a in enumerate(valid_arrays):
    if a == 1:
        arr_num = lines[i]

bin2dec_num_2 = 0
for i in range(len(arr_num)):
    bit = 1 if int(arr_num[i]) > 0 else 0
    bin2dec_num_2 += (bit * (1<<(len(arr_num)-1-i)))

print(bin2dec_num_1*bin2dec_num_2)