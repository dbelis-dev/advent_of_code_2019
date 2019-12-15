import sys
import os
import array

def main():
    filepath = './input_file'
    #filepath = './sample_1'
    cols = 25
    rows = 6
    layers = 100
    pixel_array = [[[0 for i in range(cols)] for j in range(rows)] for l in range(layers)]

    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

    with open(filepath, 'r') as fp:
        fill_array(layers, cols, rows, fp, pixel_array)



    image_array = [[2 for i in range(cols)] for j in range(rows)]
    for row in range(rows):
        for col in range(cols):
            for layer in range(layers):
                print('Col: {} | Row: {} | Layer: {} | Pixel: {} | Image: {}'.format(col, row, layer, pixel_array[layer][row][col], image_array[row][col]))
                if pixel_array[layer][row][col] < image_array[row][col]:
                    print(pixel_array[layer][row][col])
                    image_array[row][col] = pixel_array[layer][row][col]
                    print('+Col: {} | Row: {} | Layer: {} | Pixel: {} | Image: {}'.format(col, row, layer, pixel_array[layer][row][col], image_array[row][col]))
                    break

    for line in image_array:
        print(line)
    # min_layer = layers + 1
    # min = cols * rows + 1
    # for layer in range(layers):
    #     zero_counter = 0
    #     for row in range(rows):
    #         for col in range(cols):
    #             if pixel_array[layer][row][col] == 0:
    #                 # count 0s
    #                 zero_counter += 1
    #     print('0s in layer: {} = {}'.format(layer,zero_counter))
    #     if zero_counter < min:
    #         min = zero_counter
    #         min_layer = layer
    # print('Layer with min 0s: {} {}'.format(min_layer, min))
    #
    # one_counter = 0
    # two_counter = 0
    # for row in range(rows):
    #     for col in range(cols):
    #         if pixel_array[min_layer][row][col] == 1:
    #             # count 1s
    #             one_counter += 1
    #         if pixel_array[min_layer][row][col] == 2:
    #             # count 2s
    #             two_counter += 1
    # print('Ones: {} | Twos: {} | Mul: {}'.format(one_counter,two_counter,one_counter*two_counter))

def fill_array(layers, cols, rows, fp, pixel_array):
    while True:
        for layer in range(layers):
            for row in range(rows):
                for col in range(cols):
                    char_in = fp.read(1)
                    if char_in == '\n':
                        print("End of file")
                        return
                    pixel_array[layer][row][col] = int(char_in)


if __name__ == '__main__':
   main()
