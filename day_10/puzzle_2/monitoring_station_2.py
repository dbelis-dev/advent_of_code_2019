import sys
import os
import array
import math
import pygame as pg
from pygame.math import Vector2

def main():
    filepath = './input_file'
    cols = 20
    rows = 20
    asteroid_array = [[0 for i in range(cols)] for j in range(rows)]
    sum = 0
    x_laser = 8
    y_laser = 16
    laser = Vector2(x_laser, y_laser)
    counter = 0
    global max_asteroid
    target_asteroid = 200

    read_array_in(filepath, cols, asteroid_array)
    print('No of asteroids: {}'.format(max_asteroid))
    asteroid_array[y_laser][x_laser] = 'O'

    for arr in asteroid_array:
        print(arr)

    for i in range(2):
        angle_dist = dict()
        for y_a in range(rows):
            for x_a in range(cols):
                if asteroid_array[y_a][x_a] == '#':
                    asteroid = Vector2(x_a, y_a)
                    radius, angle = (laser - asteroid).as_polar()
                    norm_angle = 0
                    if angle > 0 and angle < 90:
                        norm_angle = round(angle + 270, 2)
                    elif angle >= 90:
                        norm_angle = round(angle - 90, 2)
                    else:
                        norm_angle = round(angle + 270, 2)
                    if angle_dist.get(norm_angle):
                        ## check distance
                        if angle_dist[norm_angle][0] > radius:
                            angle_dist[norm_angle] = [ radius, x_a, y_a ]

                    else:
                        ## add to list
                        angle_dist[norm_angle] = [ radius, x_a, y_a ]
        for angle_shot in sorted(angle_dist.keys()):
             x_shot = angle_dist[angle_shot][1]
             y_shot = angle_dist[angle_shot][2]
             counter += 1
             asteroid_array[y_shot][x_shot] = counter

        for arr in asteroid_array:
            print(arr)
    for y in range(rows):
        for x in range(cols):
            if asteroid_array[y][x] == target_asteroid:
                print ('{} asteroid at {},{}'.format(target_asteroid, x, y))

def read_array_in(filepath, cols, asteroid_array):
    row = 0;
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            fill_array(cols, row, line, asteroid_array)
            row += 1

def fill_array(cols, row, line, asteroid_array):
    global max_asteroid
    #print('Cols: {} | Row: {} | Line: {}'.format(cols, row, line))
    for col in range(cols):
        char_in = line[col]
        if char_in == '\n':
            print("End of line")
            return
        if char_in == '#':
            max_asteroid += 1
        asteroid_array[row][col] = char_in

if __name__ == '__main__':
    max_asteroid = 0
    main()
