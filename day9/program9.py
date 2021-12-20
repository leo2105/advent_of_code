import numpy as np
f = open('2.txt', 'r')

lines = f.read().split('\n')

dx, dy = [0,1,0,-1], [-1,0,1,0]
arr_i, arr_j = [], []
suma = 0

def valid_coord(x, y):
    if x == len(lines[0]) or x < 0:
        return False
    if y == len(lines) or y < 0:
        return False
    return True

for i in range(len(lines)):
    for j in range(len(lines[0])):
        flag = True
        for k in range(4):
            j_, i_ = j + dx[k], i + dy[k]
            if not valid_coord(j_, i_):
                continue
            if lines[i][j] >= lines[i_][j_]:
                flag = False
        if flag:
            #arr_i.append(i)
            #arr_j.append(j)
            suma += (int(lines[i][j])+1)

print(suma)
#print(arr_i, arr_j)