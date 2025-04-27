import numpy as np
import pygame as pg
import sys
import math
from math import cos, sin
from time import sleep

x_max = 1920
y_max = 1170

center = (x_max / 2, y_max / 2)

def rotate_point(x0, y0, xc, yc, angle):
    x1 = (x0 - xc) * cos(angle) - (y0 - yc) * sin(angle) + xc
    y1 = (x0 - xc) * sin(angle) + (y0 - yc) * cos(angle) + yc
    return x1, y1

def square_points(angle):
    boxp1 = rotate_point(center[0] + (100 * cos(math.pi / 4)), center[1] + (100 * sin(math.pi / 4)), center[0], center[1], angle)
    boxp2 = rotate_point(center[0] - (100 * cos(math.pi / 4)), center[1] + (100 * sin(math.pi / 4)), center[0], center[1], angle)
    boxp3 = rotate_point(center[0] - (100 * cos(math.pi / 4)), center[1] - (100 * sin(math.pi / 4)), center[0], center[1], angle)
    boxp4 = rotate_point(center[0] + (100 * cos(math.pi / 4)), center[1] - (100 * sin(math.pi / 4)), center[0], center[1], angle)

    list = []   
    list.append(boxp1)
    list.append(boxp2)
    list.append(boxp3)
    list.append(boxp4)
    return list


def main():
    pg.init()
    pg.display.set_caption("My Pygame Window")
    screen = pg.display.set_mode((x_max, y_max))
    angle = 0

    clock = pg.time.Clock()
    fps = 60

    while True:
        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the line
        pg.draw.lines(screen, (255, 255, 255), True, square_points(angle), 2)
        
        # Update the display
        pg.display.flip()
        angle += 0.01
        clock.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
print(square_points(0)) 