import numpy as np
from numpy.matrixlib.defmatrix import matrix
f = open('3.txt', 'r')

lines = f.read().split('\n')

x1_arr, x2_arr, y1_arr, y2_arr = [], [], [], []

for line in lines:
    a, _, b = line.split(' ')
    print(line)
    x1, y1 = int(a.split(',')[0]), int(a.split(',')[1])
    x2, y2 = int(b.split(',')[0]), int(b.split(',')[1])
    
    x1_arr.append(x1)
    y1_arr.append(y1)
    x2_arr.append(x2)
    y2_arr.append(y2)



# find max
N = 0
N = max(x1_arr)
N = max(N, max(x2_arr))
N = max(N, max(y1_arr))
N = max(N, max(y2_arr))

matrix_marks = np.zeros((N+1,N+1))
for i in range(len(x1_arr)):
    x1, y1, x2, y2 = x1_arr[i], y1_arr[i], x2_arr[i], y2_arr[i]
    

    if x1 == x2:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for i in range(y1,y2+1):
            matrix_marks[i, x1] += 1
    elif y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for i in range(x1,x2+1):
            matrix_marks[y1, i] += 1
    else:
        print(x1, x2, y1, y2)
        const_1 , const_2 = 1, 1
        if x1 > x2:
            const_1 = -1
        if y1 > y2:
            const_2 = -1
        for i in range(abs(x2-x1)+1):
            matrix_marks[y1+const_2*i, x1+const_1*i] += 1

print(matrix_marks)
        
cont  = 0
for i in range(N+1):
    for j in range(N+1):
        if matrix_marks[i, j] > 1:
            cont += 1

print(cont)