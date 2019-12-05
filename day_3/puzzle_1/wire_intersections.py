import sys
import os
import array

def main():
    filepath = './input_file'
    #filepath = './sample_2'
    #port_array = [[0 for i in range(10)] for j in range(10)]
    port_array = [[0 for i in range(20000)] for j in range(20000)]

    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

    current_point = 1
    min_x = 0
    min_y = 0
    sum = 10000
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            print('==Line==')
            current_x = 0
            current_y = 0
            incr_x = 1
            incr_y = 1
            for value in line.split(','):
                command = value[0]
                offset = int(value[1:])
                #print('Command: {} | Offset: {}'.format(command, offset))
                if command == 'R' or command == 'L':
                    if command == 'R':
                        incr_x = 1
                    else:
                        incr_x = -1
                    for x in range(current_x, current_x + (offset + 1) * incr_x, incr_x):
                        if port_array[current_y][x] == 0:
                            port_array[current_y][x] = current_point
                        if port_array[current_y][x] > 0 and port_array[current_y][x] != current_point:
                            port_array[current_y][x] += current_point
                            min_x = x
                            min_y = current_y
                            if abs(min_x) + abs(min_y) < sum:
                                if abs(min_x) + abs(min_y) != 0:
                                    sum = abs(min_x) + abs(min_y)
                            #print('Found: {},{} = {}'.format(min_x,min_y,abs(min_x) + abs(min_y)))
                        #print('Y: {} | X: {}'.format(current_y, x))
                    current_x += offset * incr_x
                if command == 'U' or command == 'D':
                    if command == 'U':
                        incr_y = 1
                    else:
                        incr_y = -1
                    for y in range(current_y, current_y + (offset + 1) * incr_y, incr_y):
                        if port_array[y][current_x] == 0:
                            port_array[y][current_x] = current_point
                        if port_array[y][current_x] > 0 and port_array[y][current_x] != current_point:
                            port_array[y][current_x] += current_point
                            min_x = current_x
                            min_y = y
                            if abs(min_x) + abs(min_y) < sum:
                                if abs(min_x) + abs(min_y) != 0:
                                    sum = abs(min_x) + abs(min_y)
                            #print('Found: {},{} = {}'.format(min_x,min_y,abs(min_x) + abs(min_y)))
                        #print('Y: {} | X: {}'.format(y, current_x))
                    current_y += offset * incr_y
            current_point += 1
        #for row in port_array:
        #    print(row)
        port_array[0][0] = 0
        print('Manhattan Sum: {}'.format(sum))
        position = index_2d(port_array, 3)
        print('Position: {}'.format(position))

def index_2d(data, search):
    for i, e in enumerate(data):
        try:
            return i, e.index(search)
        except ValueError:
            pass
    raise ValueError("{} is not in list".format(repr(search)))

if __name__ == '__main__':
   main()
