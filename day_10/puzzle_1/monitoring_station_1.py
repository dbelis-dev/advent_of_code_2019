import sys
import os
import array
import copy
import math

def main():
    filepath = './input_file'
    cols = 20
    rows = 20
    asteroid_array = [[0 for i in range(cols)] for j in range(rows)]
    sum = 0

    read_array_in(filepath, cols, asteroid_array)
    sec_array = [[0 for i in range(cols)] for j in range(rows)]

    for row in range(rows):
        for col in range(cols):
            x_a = col
            y_a = row
            if asteroid_array[y_a][x_a] == '#':
                process_lines(cols, rows, x_a, y_a, filepath, asteroid_array, sec_array)
    max = 0
    for row in range(rows):
        for col in range(cols):
            if max < sec_array[row][col]:
                max = sec_array[row][col]
                print("Max: {} at {},{}".format(max, col, row))


def process_lines(cols, rows, x_a, y_a, filepath, asteroid_array, sec_array):
    m = 0
    b = 0
    sum = 0
    slope_dict = dict()
    for row in range(rows):
        for col in range(cols):
            if asteroid_array[row][col] == '#':
                if row == y_a and col == x_a:
                    continue
                else:
                    if x_a == col:
                        m = 0
                        x_c_pol = 0
                    else:
                        m = (row - y_a) / (col - x_a)
                        x_c_pol = abs(col - x_a) / (col - x_a)
                    if y_a == row:
                        y_c_pol = 0
                    else:
                        y_c_pol = abs(row - y_a) / (row - y_a)
                    b = y_a - (m * x_a)
                    d = math.sqrt( pow((y_a - row), 2) + pow((x_a - col), 2) )
                    if slope_dict.get(m):
                        x_2 = slope_dict[m][1]
                        y_2 = slope_dict[m][2]
                        x_pol = slope_dict[m][3]
                        y_pol = slope_dict[m][4]
                        ## check if same polarity
                        if x_pol == x_c_pol and x_pol == x_c_pol:
                            ## check for distance
                            d_2 = slope_dict[m][0]
                            if d_2 > d:
                                slope_dict[m] = [ d, col, row, x_c_pol, y_c_pol  ]
                        else:
                            ## add
                            slope_dict[m] = [ d, col, row, x_c_pol, y_c_pol  ]
                            sum += 1
                    else:
                        ## add
                        slope_dict[m] = [ d, col, row, x_c_pol, y_c_pol  ]
                        sum += 1
        sec_array[y_a][x_a] = sum

def read_array_in(filepath, cols, asteroid_array):
    row = 0;
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            fill_array(cols, row, line, asteroid_array)
            row += 1

def fill_array(cols, row, line, asteroid_array):
    #print('Cols: {} | Row: {} | Line: {}'.format(cols, row, line))
    for col in range(cols):
        char_in = line[col]
        if char_in == '\n':
            print("End of line")
            return
        asteroid_array[row][col] = char_in

if __name__ == '__main__':
    main()
