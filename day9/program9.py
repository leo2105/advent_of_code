import numpy as np
f = open('1.txt', 'r')

lines = f.read().split('\n')

dx, dy = [0,1,0,-1], [-1,0,1,0]

def valid_coord(x, y):
    if x == len(lines[0]) or x < 0:
        return False
    if y == len(lines) or y < 0:
        return False
    return True

for i in range(len(lines)):
    for j in range(len(lines[0])):
        for k in range(4):
            x_, y_ = lines[i][j] + dx[k], lines[i][j]
            if valid_coord(x, y):
                