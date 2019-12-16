import sys
import os
import array

def main():
    filepath = './input_file'
    #filepath = './sample_1'
    orbit_list = {}

    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            tup = [0 for j in range(2)]
            i = 0
            for value in line.split(')'):
                tup[i] = value.rstrip()
                i += 1
            orbit_list[tup[1]] = tup[0]

    you_arr = []
    san_arr = []
    sum_count = 0
    key = 'YOU'
    current = key
    count = 0
    while True:
        orbiting = orbit_list[current]
        current = orbiting
        count += 1
        if orbiting == 'COM':
            break
        you_arr.append(orbiting)
    sum_count += count

    sum_count = 0
    key = 'SAN'
    current = key
    count = 0
    while True:
        orbiting = orbit_list[current]
        current = orbiting
        count += 1
        if orbiting == 'COM':
            break
        san_arr.append(orbiting)
    sum_count += count

    common = find_common(you_arr, san_arr)

    final_arr = []
    key = 'YOU'
    current = key
    while True:
        orbiting = orbit_list[current]
        current = orbiting
        final_arr.append(orbiting)
        if orbiting == common:
            break

    key = 'SAN'
    current = key
    while True:
        orbiting = orbit_list[current]
        current = orbiting
        if orbiting == common:
            break
        final_arr.append(orbiting)

    print('Transitions: {}'.format(len(final_arr) -1))

def find_common(you_arr, san_arr):
    for i in you_arr:
        for j in san_arr:
            if i == j:
                print('Found common: {}'.format( i ))
                return i

if __name__ == '__main__':
    main()
