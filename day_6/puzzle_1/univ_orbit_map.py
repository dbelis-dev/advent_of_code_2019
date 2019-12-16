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

    sum_count = 0
    for key in orbit_list.keys():
        if key == 'COM':
            continue
        current = key
        count = 0
        while True:
            orbiting = orbit_list[current]
            current = orbiting
            count += 1
            if orbiting == 'COM':
                break
        #print('{} orbits from {} -> COM'.format(count, key))
        sum_count += count

    print('Max Orbits: {}'.format(sum_count))

if __name__ == '__main__':
    main()
