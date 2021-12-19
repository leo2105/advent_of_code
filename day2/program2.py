import numpy as np
f = open('c.txt', 'r')

d = {'aim':0, 'depth':0, 'forward':0}

lines = f.read().split('\n')[:-1]
print(lines)
cont = 0
for line in lines:
    index, value = line.split(' ')
    #print(index, value)
    #d[index] += int(value)
    value = int(value)
    if index == 'down':
        d['aim'] += value
    if index == 'up':
        d['aim'] -= value
    if index == 'forward':
        d['forward'] += value
        d['depth'] += d['aim']*value
print(d)       
print(d['forward']*d['depth'])
