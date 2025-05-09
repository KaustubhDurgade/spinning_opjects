import numpy as np
import pygame as pg
import sys
import math
from math import cos, sin
from time import sleep

x_max = 1920
y_max = 1170

center = (x_max / 2, y_max / 2)

scale = 10  # Reduced scale for better visibility
z_modifier =  0  # Adjusted z modifier for better visibility
points = [
    (scale, scale, scale),
    (scale, scale, -scale),
    (scale, -scale, scale),
    (scale, -scale, -scale),
    (-scale, scale, scale),
    (-scale, scale, -scale),
    (-scale, -scale, scale),
    (-scale, -scale, -scale)
    ]

def project_3d_unto_2d(x, y, z, f):
    f += 1000
    z+=100
    x3d = (f / z) * x + center[0]
    y3d = (f / z) * y + center[1]
    return x3d, y3d

def rotate_around_x(x, y, z, angle):
    rotation_matrix_x = np.array([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    ])
    point_3d = np.array([x, y, z])
    return tuple(rotation_matrix_x @ point_3d)
def rotate_around_y(x, y, z, angle):
    rotation_matrix_y = np.array([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ])
    point_3d = np.array([x, y, z])
    return tuple(rotation_matrix_y @ point_3d)
def rotate_around_z(x, y, z, angle):
    rotation_matrix_z = np.array([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])
    point_3d = np.array([x, y, z])
    return tuple(rotation_matrix_z @ point_3d)

def rotate_points(points, angle_x, angle_y, angle_z):
    rotated_points = []
    for point in points:
        x, y, z = point
        x, y, z = rotate_around_x(x, y, z, angle_x)
        x, y, z = rotate_around_y(x, y, z, angle_y)
        x, y, z = rotate_around_z(x, y, z, angle_z)
        rotated_points.append((x, y, z))
    return rotated_points

def cube_points(three_d_points):
    projected_points = []
    for point in three_d_points:
        x, y, z = point
        projected_point = project_3d_unto_2d(x, y, z, 100)
        projected_points.append(projected_point)
    return projected_points


def main():
    pg.init()
    pg.display.set_caption("My Pygame Window")
    screen = pg.display.set_mode((x_max, y_max))
    anglex = 0
    angley = 0
    anglez = 0

    clock = pg.time.Clock()
    fps = 60

    while True:
        anglex += 0.01
        angley += 0.0
        anglez += 0.0

        list = cube_points(rotate_points(points, anglex, angley, anglez))
        face_1 = [list[0], list[2], list[6], list[4]]
        face_2 = [list[1], list[3], list[7], list[5]]
        face_3 = [list[0], list[1], list[3], list[2]]
        face_4 = [list[4], list[5], list[7], list[6]]
        face_5 = [list[0], list[1], list[5], list[4]]
        face_6 = [list[2], list[3], list[7], list[6]]
        # Clear the screen
        screen.fill((0, 0, 0))

        font = pg.font.Font('freesansbold.ttf', 32)

        # Draw the line
        pg.draw.polygon(screen, (127, 0, 255), face_1)
        pg.draw.polygon(screen, (0, 0, 255), face_2)
        pg.draw.polygon(screen, (0, 255, 0), face_3)
        pg.draw.polygon(screen, (255, 255, 0), face_4)
        pg.draw.polygon(screen, (255, 127, 0), face_5)
        pg.draw.polygon(screen, (255, 0, 0), face_1)
        
        # Update the display
        pg.display.flip()
        clock.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
#print (cube_ponts(points))
if __name__ == "__main__":
    main()