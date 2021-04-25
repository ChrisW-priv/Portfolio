arr = [1, 1, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
range_x = 4
range_y = 5
length = 3


diagonals_tl_br = [[range_x*(y-step)+x+step for step in range(length)]
                   for y in range(length-1, range_y) for x in range(range_x-length+1)]

diagonals_bl_tr = [[range_x*(y-step)+x-step for step in range(length)]
                   for y in range(length-1, range_y) for x in range(length-1, range_x)]

rows = [[x + y*range_x + step for step in range(length)]
        for y in range(range_y) for x in range(range_x-length+1)]

columns = [[x+range_x*(y+step) for step in range(length)]
           for y in range(range_y-length+1) for x in range(range_x)]

print(len(diagonals_tl_br), diagonals_tl_br)
print(len(diagonals_bl_tr), diagonals_bl_tr)
print(len(rows), rows)
print(len(columns), columns)
