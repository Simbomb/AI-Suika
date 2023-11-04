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
    

    relative_vel = fruit1.momentum - fruit2.momentum
    relative_vel = np.dot(direction_vector, relative_vel) * -1
    momentum_vector = direction_vector * relative_vel

    return collision, direction_vector, distance, momentum_vector

