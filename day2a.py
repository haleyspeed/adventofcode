import pandas as pd
puzzle_input = [1,0,0,3,
                1,1,2,3,
                1,3,4,3,
                1,5,0,3,
                2,6,1,19,
                1,19,10,23,
                2,13,23,27,
                1,5,27,31,
                2,6,31,35,
                1,6,35,39,
                2,39,9,43,
                1,5,43,47,
                1,13,47,51,
                1,10,51,55,
                2,55,10,59,
                2,10,59,63,
                1,9,63,67,
                2,67,13,71,
                1,71,6,75,
                2,6,75,79,
                1,5,79,83,
                2,83,9,87,
                1,6,87,91,
                2,91,6,95,
                1,95,6,99,
                2,99,13,103,
                1,6,103,107,
                1,2,107,111,
                1,111,9,0,
                99,
                2,14,0,0]

codes = [1,12,2,3,
         1,1,2,3,
         1,3,4,3,
         1,5,0,3,
         2,6,1,19,
         1,19,10,23,
         2,13,23,27,
         1,5,27,31,
         2,6,31,35,
         1,6,35,39,
         2,39,9,43,
         1,5,43,47,
         1,13,47,51,
         1,10,51,55,
         2,55,10,59,
         2,10,59,63,
         1,9,63,67,
         2,67,13,71,
         1,71,6,75,
         2,6,75,79,
         1,5,79,83,
         2,83,9,87,
         1,6,87,91,
         2,91,6,95,
         1,95,6,99,
         2,99,13,103,
         1,6,103,107,
         1,2,107,111,
         1,111,9,0,
         99,2,14,0,
         0]

def get_pos(codes):
    i = 0
    while i < len(codes)-3:
        pos0 = codes[i] 
        pos1 = codes[i+1] 
        pos2 = codes[i+2] 
        pos3 = codes[i+3] 
        if pos0 == 1:
            codes[pos3] = codes[pos1] + codes[pos2] 
        if pos0 == 2:
            codes[pos3] = codes[pos1] * codes[pos2]
        if pos0 == 99:
            i == len(codes)
        else:
            pass
        i = i + 4
    return (codes)

new_codes = get_pos(codes)
print(new_codes[0])
