import numpy as np
f = open('2.txt', 'r')

lines = f.read().split('\n')
final_int_sum = 0

for line in lines:
    dic_char = {}
    final_str = ''

    ins, outs = line.split(' | ')
    arr_strings = ins.split(' ')

    dict_aparitions = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
    dict_segments = {}
    dict_arr = {
            '1110111' : 0,
            '0010010' : 1,
            '1011101' : 2,
            '1011011' : 3,
            '0111010' : 4,
            '1101011' : 5,
            '1101111' : 6,
            '1010010' : 7,
            '1111111' : 8,
            '1111011' : 9}

    # count aparitions of each char
    for string_ in arr_strings:
        for char_ in string_:
            dict_aparitions[char_] += 1
        if len(string_) == 3:
            string_len3 = string_
        if len(string_) == 2:
            string_len2 = string_
        if len(string_) == 4:
            string_len4 = string_
        if len(string_) == 7:
            string_len7 = string_
        
    # determine seg 1
    for c in string_len3:
        if c not in string_len2:
            dict_segments[1] = c
            break

    # determine some segments: 5, 2 and 6
    for id_ in dict_aparitions:
        if dict_aparitions[id_] == 4:
            dict_segments[5] = id_
        if dict_aparitions[id_] == 6:
            dict_segments[2] = id_
        if dict_aparitions[id_] == 9:
            dict_segments[6] = id_

    # determine segment 3
    for c in string_len3:
        if c != dict_segments[1] and c != dict_segments[6]:
            dict_segments[3] = c

    # determine segment 4
    for c in string_len4:
        if c not in dict_segments.values():
            dict_segments[4] = c
    
    # determine segment 7
    for c in string_len7:
        if c not in dict_segments.values():
            dict_segments[7] = c

    for out_ in outs.split(' '):
        arr_ = ['0','0','0','0','0','0','0']
        for c in out_:
            for key in dict_segments:
                if dict_segments[key] == c:
                    arr_[key-1] = '1'
        str_ = ''.join(arr_)
        final_str += str(dict_arr[str_])

    final_int_sum += int(final_str)
print(final_int_sum)

