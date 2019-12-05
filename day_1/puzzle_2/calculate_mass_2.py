import sys
import os
import math

def main():
   filepath = './input_file'
   sum = 0
   new_fuel = 0

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

   with open(filepath) as fp:
       for fuel in fp:
           while int(fuel) > 0:
               new_fuel = math .floor(int(fuel)/3)-2
               if new_fuel < 0:
                    break
               sum += new_fuel
               print('Fuel: {} - Sum: {}'.format(new_fuel, sum))
               fuel = new_fuel

   print("Sum: {}".format(sum))

if __name__ == '__main__':
   main()
