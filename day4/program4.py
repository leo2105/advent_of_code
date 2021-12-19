import numpy as np
f = open('3.txt', 'r')

lines = f.read().split('\n')
arr_5x5 = []
balls = lines[0].split(',')

matrix = np.zeros((5,5))
for i in range(2,len(lines)):
    if i>=1 and (i-1)%6 == 0:
        arr_5x5.append(matrix)
        matrix = np.zeros((5,5))
        continue

    arr = (' '.join(lines[i].split())).split(' ')
    for j,num_char in enumerate(arr):
        matrix[(i-2)%6,j] = int(num_char)

arr_5x5.append(matrix) 
final_arr = np.array(arr_5x5)
matrix_marks = np.zeros((final_arr.shape))
arr_check_winner = np.zeros(len(final_arr))

def check_vertical():
    for n in range(len(matrix_marks)):
        for j in range(5):
            cont = np.sum(matrix_marks[n, :, j])
            suma = 0
            for a in range(5):
                for b in range(5):
                    if matrix_marks[n,a,b] == 0:
                        suma += final_arr[n,a,b] 
            if cont == 5:
                return n, int(suma)
    return -1, -1

def check_horizontal():
    for n in range(len(matrix_marks)):
        for i in range(5):
            cont = np.sum(matrix_marks[n, i, :])
            suma = 0
            for a in range(5):
                for b in range(5):
                    if matrix_marks[n,a,b] == 0:
                        suma += final_arr[n,a,b] 
            if cont == 5:
                return n, int(suma)
    return -1, -1

def search_number_and_mark(num):
    for n in range(len(matrix_marks)): 
        for i in range(5):
            for j in range(5):
                if final_arr[n,i,j] == int(num):
                    matrix_marks[n,i,j] = 1
        
def check_last_winner():
    cont, rpta = 0, -1
    for i in range(len(arr_check_winner)):
        if arr_check_winner[i] == 0:
            cont += 1
    if cont == 0:
        return True
    return False

last_winner, last_sum_, last_ball = -1, -1, -1

for val in balls:
    
    search_number_and_mark(val)
    print(val)
    print(arr_check_winner)


    nro_bingo_card_winner, sum_ = check_horizontal()
    if nro_bingo_card_winner != -1:
        if arr_check_winner[nro_bingo_card_winner] == 0:
            last_ball = val
            last_winner = nro_bingo_card_winner
            last_sum_ = sum_
        arr_check_winner[nro_bingo_card_winner] = 1


    res = check_last_winner()
    if res == True:
        #print(1, val, sum_)
        #print(int(val)*sum_)
        break

    nro_bingo_card_winner, sum_ = check_vertical()
    if nro_bingo_card_winner != -1:
        if arr_check_winner[nro_bingo_card_winner] == 0:
            last_ball = val
            last_winner = nro_bingo_card_winner
            last_sum_ = sum_
        arr_check_winner[nro_bingo_card_winner] = 1

    res = check_last_winner()
    if res == True:
        #print(2, val, sum_ )
        #print(int(val)*sum_)
        break

print(last_winner, last_sum_, last_ball)
print(last_sum_ * int(last_ball))


