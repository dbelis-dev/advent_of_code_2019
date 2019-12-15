import sys
import os
import math

def main():
   filepath = './input_file'
   sum = 0

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

   with open(filepath) as fp:
       for fuel in fp:
               new_fuel = math .floor(int(fuel)/3)-2
               sum += new_fuel

   print("Sum: {}".format(sum))

if __name__ == '__main__':
   main()
