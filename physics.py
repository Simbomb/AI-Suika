import random
import numpy as np
import pygame as pg






def collision_detection(fruit1, fruit2):
    direction_vector = np.array([fruit1.x - fruit2.x, fruit1.y - fruit2.y], dtype='float64')
    distance = (direction_vector[0]**2 + direction_vector[1]**2) ** 0.5
    #1 length vector
    if distance != 0:
        direction_vector /= distance
                   
    collision = distance < (fruit1.size + fruit2.size)

    return collision, distance

def collision_resolution(fruit1, fruit2, distance):
    overlap = fruit1.size + fruit2.size - distance
    dx = (fruit1.x - fruit2.x) / distance
    dy = (fruit1.y - fruit2.y) / distance
    return overlap, dx, dy

def check_game_over(fruit):
    if fruit.y <= 0:
            return True
    return False