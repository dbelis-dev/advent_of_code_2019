import sys
import os
import math
import array
from random import randint
import copy

def main():
    filepath = './input_file'
    orig_array = array.array('i',[])
    input_array = array.array('i',[])

    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

    with open(filepath, 'r') as fp:
       for value in fp.read().split(','):
           orig_array.append(int(value))
    input_array = copy.copy(orig_array)

    target = 19690720
    while input_array[0] != target:
        input_array = copy.copy(orig_array)
        noun = randint(0,99)
        verb = randint(0,99)
        input_array[1] = noun
        input_array[2] = verb
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

    print("Verb: {} | Noun: {} | Answer: {}".format(noun, verb, 100 * noun + verb))

if __name__ == '__main__':
   main()
