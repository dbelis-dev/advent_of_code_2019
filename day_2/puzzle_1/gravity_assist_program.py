import sys
import os
import math
import array

def main():
    filepath = './input_file'
    #filepath = './sample'
    input_array = array.array('i',[])

    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

    with open(filepath, 'r') as fp:
       for value in fp.read().split(','):
           input_array.append(int(value))

    i = 0
    step = 4
    while i < len(input_array):
        opcode = input_array[i]
        if opcode == 1:
                sum = input_array[input_array[i+1]] + input_array[input_array[i+2]]
                input_array[input_array[i+3]] = sum
        if opcode == 2:
                mul = input_array[input_array[i+1]] * input_array[input_array[i+2]]
                input_array[input_array[i+3]] = mul
        if opcode == 99:
                break
        i += step

    print("Array: {}".format(input_array))

if __name__ == '__main__':
   main()
