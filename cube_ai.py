import numpy as np
import pygame as pg
import sys
import math
from math import cos, sin
from time import sleep

x_max = 1920
y_max = 1170

center = (x_max / 2, y_max / 2)

def project_3d_unto_2d(x, y, z, f):
    x3d = (f/z) * x + center[0]
    y3d = (f/z) * y + center[1]
    return x3d, y3d

def rotate_3d_point_on_x(point, angle):
    rotation_matrix_x = np.array([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    ])
    point_3d = np.array(point)
    return tuple(rotation_matrix_x @ point_3d)

def rotate_3d_point_on_y(point, angle):
    rotation_matrix_y = np.array([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ])
    point_3d = np.array(point)
    return tuple(rotation_matrix_y @ point_3d)  

def rotate_3d_point_on_z(point, angle):
    rotation_matrix_z = np.array([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])  
    point_3d = np.array(point)
    return tuple(rotation_matrix_z @ point_3d)

def cube_points(angle_x, angle_y, angle_z):
    # Scale the cube to be larger and ensure all points are in front of the camera
    scale = 25  # Reduced scale for better visibility
    cube_points = [
        (scale, scale, scale),      # Front top right
        (scale, scale, -scale),     # Back top right
        (scale, -scale, scale),     # Front bottom right
        (scale, -scale, -scale),    # Back bottom right
        (-scale, scale, scale),     # Front top left
        (-scale, scale, -scale),    # Back top left
        (-scale, -scale, scale),    # Front bottom left
        (-scale, -scale, -scale)    # Back bottom left
    ]
    projected_points = []
    for point in cube_points:
        # Apply rotations in sequence: x, then y, then z
        point = rotate_3d_point_on_x(point, angle_x)
        point = rotate_3d_point_on_y(point, angle_y)
        point = rotate_3d_point_on_z(point, angle_z)
        # Add offset to z to ensure points stay in front of camera
        x, y, z = point
        z += 200  # Add offset after rotation
        projected_points.append(project_3d_unto_2d(float(x), float(y), float(z), 1000))  # Increased focal length from 50 to 200
    return projected_points

def main():
    pg.init()
    pg.display.set_caption("My Pygame Window")
    screen = pg.display.set_mode((x_max, y_max))

    clock = pg.time.Clock()
    fps = 60

    angle_x = 0
    angle_y = 0
    angle_z = 0

    # Define the edges of the cube (pairs of vertex indices)
    edges = [
        (0, 1), (0, 2), (0, 4),  # Front face edges
        (1, 3), (1, 5),          # Back face edges
        (2, 3), (2, 6),          # Right face edges
        (3, 7),                  # Bottom back edge
        (4, 5), (4, 6),          # Left face edges
        (5, 7),                  # Top back edge
        (6, 7)                   # Bottom left edge
    ]

    while True:
        # Clear the screen
        screen.fill((0, 0, 0))
        angle_x += 0.0
        angle_y += 0.0
        angle_z += 0.01
        # Get the projected points
        points = cube_points(angle_x, angle_y, angle_z)
        
        # Draw each edge
        for edge in edges:
            pg.draw.line(screen, (255, 255, 255), points[edge[0]], points[edge[1]], 2)
        
        # Update the display
        pg.display.flip()
        clock.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
if __name__ == "__main__":
    main()  