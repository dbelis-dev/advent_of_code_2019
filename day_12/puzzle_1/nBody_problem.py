import sys
import os
import array
import pygame.math as math

# pos_A = math.Vector3(-1,0,2)
# pos_B = math.Vector3(2,-10,-7)
# pos_C = math.Vector3(4,-8,8)
# pos_D = math.Vector3(3,5,-1)
pos_A = math.Vector3(-1,-4,0)
pos_B = math.Vector3(4,7,-1)
pos_C = math.Vector3(-14,-10,9)
pos_D = math.Vector3(1,2,17)
moon_position = []
moon_position.append(pos_A)
moon_position.append(pos_B)
moon_position.append(pos_C)
moon_position.append(pos_D)
vel_A = math.Vector3(0,0,0)
vel_B = math.Vector3(0,0,0)
vel_C = math.Vector3(0,0,0)
vel_D = math.Vector3(0,0,0)
moon_velocity = []
moon_velocity.append(vel_A)
moon_velocity.append(vel_B)
moon_velocity.append(vel_C)
moon_velocity.append(vel_D)

for count in range(1000):
    start_a = 0
    for a in range (start_a, len(moon_position)):
        position_A = moon_position[a]
        start_b = a + 1
        for b in range(start_b, len(moon_position)):
            position_B = moon_position[b]

            if position_A.x < position_B.x:
                gravity_Ax = 1
                gravity_Bx = -1
            else:
                gravity_Ax = -1
                gravity_Bx = 1

            if position_A.y < position_B.y:
                gravity_Ay = 1
                gravity_By = -1
            else:
                gravity_Ay = -1
                gravity_By = 1

            if position_A.z < position_B.z:
                gravity_Az = 1
                gravity_Bz = -1
            else:
                gravity_Az = -1
                gravity_Bz = 1

            if position_A.x == position_B.x:
                gravity_Ax = 0
                gravity_Bx = 0
            if position_A.y == position_B.y:
                gravity_Ay = 0
                gravity_By = 0
            if position_A.z == position_B.z:
                gravity_Az = 0
                gravity_Bz = 0

            vel_A = math.Vector3(gravity_Ax, gravity_Ay, gravity_Az)
            vel_B = math.Vector3(gravity_Bx, gravity_By, gravity_Bz)
            moon_velocity[a] += vel_A
            moon_velocity[b] += vel_B
    for i in range(len(moon_position)):
        moon_position[i] += moon_velocity[i]

mul = 0
for i in range( len(moon_position) ):
    pos = moon_position[i]
    sum_pos = abs(pos.x) + abs(pos.y) + abs(pos.z)
    vel = moon_velocity[i]
    sum_vel = abs(vel.x) + abs(vel.y) + abs(vel.z)
    mul += sum_pos * sum_vel
    print('Total Energy: {}'.format(int(mul)))
