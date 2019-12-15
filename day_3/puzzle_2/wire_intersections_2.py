import sys
import os
import array

def main():
    filepath = './input_file'
    #filepath = './sample_2'
    max_x = 15000
    max_y = 15000
    #port_array = [[0 for i in range(20000)] for j in range(20000)]
    port_array = [[0 for i in range(max_x)] for j in range(max_y)]
    inter_array = [[[0 for i in range(max_x)] for j in range(max_y)] for s in range(3)]

    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

    current_point = 1
    min_x = 0
    min_y = 0
    sum = 10000
    min_steps = 10000
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            print('==Line==')
            step_counter = 0
            current_x = 0
            current_y = 0
            incr_x = 1
            incr_y = 1
            steps_x = 0
            steps_y = 0
            for value in line.split(','):
                command = value[0]
                offset = int(value[1:])
                #print('Command: {} | Offset: {}'.format(command, offset))
                if command == 'R' or command == 'L':
                    if command == 'R':
                        incr_x = 1
                    else:
                        incr_x = -1
                    for x in range(current_x + (1 * incr_x), current_x + (offset + 1) * incr_x, incr_x):
                        step_counter += 1
                        if port_array[current_y][x] == 0:
                            port_array[current_y][x] = current_point
                        if port_array[current_y][x] > 0 and port_array[current_y][x] != current_point:
                            port_array[current_y][x] += current_point
                            min_x = x
                            min_y = current_y
                            if abs(min_x) + abs(min_y) < sum:
                                if abs(min_x) + abs(min_y) != 0:
                                    sum = abs(min_x) + abs(min_y)
                        if inter_array[current_point - 1][current_y][x] == 0:
                            inter_array[current_point - 1][current_y][x] += step_counter
                        #print('Y: {} | X: {} | step_counter: {}'.format(current_y, x, step_counter))
                    current_x += offset * incr_x
                    # for row in inter_array[current_point - 1]:
                    #     print(row)
                    # print()
                    #step_counter += abs(current_x)
                if command == 'U' or command == 'D':
                    if command == 'U':
                        incr_y = 1
                    else:
                        incr_y = -1
                    for y in range(current_y + (1 * incr_y), current_y + (offset + 1) * incr_y, incr_y):
                        step_counter += 1
                        if port_array[y][current_x] == 0:
                            port_array[y][current_x] = current_point
                        if port_array[y][current_x] > 0 and port_array[y][current_x] != current_point:
                            port_array[y][current_x] += current_point
                            min_x = current_x
                            min_y = y
                            if abs(min_x) + abs(min_y) < sum:
                                if abs(min_x) + abs(min_y) != 0:
                                    sum = abs(min_x) + abs(min_y)
                        if inter_array[current_point - 1][y][current_x] == 0:
                            inter_array[current_point - 1][y][current_x] += step_counter
                        #print('Y: {} | X: {} | step_counter: {}'.format(y, current_x, step_counter))
                    current_y += offset * incr_y
                    # for row in inter_array[current_point - 1]:
                    #     print(row)
                    # print()
                    #step_counter += abs(current_y)

            current_point += 1
        for y in range(max_y):
            for x in range(max_x):
                inter_array[2][y][x] = inter_array[0][y][x] + inter_array[1][y][x]
        # for arr in range(3):
        #     for row in inter_array[arr]:
        #         pprint(row)
        #     print()
        for y in range(max_y):
            for x in range(max_x):
                if port_array[y][x] == 3:
                    if min_steps > inter_array[2][y][x]:
                        min_steps = inter_array[2][y][x]
                        print('{},{} : {}'.format(x, y, min_steps))
        # for row in port_array:
        #     print(row)
        port_array[0][0] = 0
        #print('Manhattan Sum: {}'.format(sum))
        #position = index_2d(port_array, 3)
        #print('Position: {}'.format(position))


def index_2d(data, search):
    for i, e in enumerate(data):
        try:
            return i, e.index(search)
        except ValueError:
            pass
    raise ValueError("{} is not in list".format(repr(search)))

if __name__ == '__main__':
   main()
