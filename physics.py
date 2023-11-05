import random
import numpy as np
import pygame as pg


class Collision:
    def __init__(self, fruit1, fruit2):
        self.fruit1 = fruit1
        self.fruit2 = fruit2
    
    def __eq__(self, coll):
        return (self.fruit1 == coll.fruit1 and self.fruit2 == coll.fruit2) or (self.fruit1 == coll.fruit2 and self.fruit2 == coll.fruit1)


def handle_collision(current_fruits):
    self_collisions = []

    for fruit1 in current_fruits:
        for fruit2 in current_fruits:
            coll = Collision(fruit1, fruit2)
            touch = fruit1.touch(fruit2)
            if fruit1 != fruit2 and touch and not coll in self_collisions:
                self_collisions.append(coll)
            elif not touch:
                fruit1.momentum[1] += 1
    
    for coll in self_collisions:
        fruit1 = coll.fruit1
        fruit2 = coll.fruit2
        diff = fruit2.pos - fruit1.pos
        vel = diff/np.linalg.norm(diff)
        midpoint = (fruit1.size + fruit2.size - fruit2.distance(fruit1))/2
        fruit1.pos = fruit1.pos + midpoint * vel
        fruit2.pos = fruit2.pos + midpoint * vel

        theta_angle = np.arctan2(-diff[1], diff[0])
        rotation = np.array([[np.cos(theta_angle), -np.sin(theta_angle)],
                             [np.sin(theta_angle), np.cos(theta_angle)]])
        fruit1.momentum = np.matmul(rotation, fruit1.momentum)*0
        fruit2.momentum = np.matmul(rotation, fruit2.momentum)

        mass = fruit1.mass + fruit2.mass

        energy1 = ((fruit1.mass - fruit2.mass)*fruit1.momentum[0] + 2*fruit2.mass*fruit2.momentum[0])/mass
        energy2 = ((fruit2.mass - fruit1.mass)*fruit2.momentum[0] + 2*fruit1.mass*fruit1.momentum[0])/mass
        fruit1.momentum[0] = energy1
        fruit2.momentum[0] = energy2

        transposed_rotation = np.transpose(rotation)
        fruit1.momentum = np.matmul(transposed_rotation, fruit1.momentum)
        fruit2.momentum = np.matmul(transposed_rotation, fruit2.momentum)
        self_collisions.remove(coll)

        del coll

def handle_overlap(current_fruits):
    for fruit1 in current_fruits:
        for fruit2 in current_fruits:
            if fruit1 != fruit2:
                diff = fruit1.pos - fruit2.pos
                normal = diff / np.linalg.norm(diff)
                overlap = (fruit1.size + fruit2.size - fruit1.distance(fruit2)) / 2
                if overlap > 0:
                    fruit1.pos -= overlap*normal
                    fruit2.pos += overlap*normal


    
    
