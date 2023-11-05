import pygame as pg
from physics import *

size_ratio = 8
friction = 0.1
damping = 0.2
class Fruit:
    def __init__(self, pos, size, color):
        self.pos = np.array(pos)
        self.size = size
        self.color = color
        self.momentum = np.array([0, 0])
        self.mass = size*10
        self.gravity = self.mass*1
    
    def draw(self, screen):
        #Draw the fruit
        pg.draw.circle(screen, self.color, (self.pos[0], self.pos[1]), self.size)

    def move(self, height, width):
        self.pos = self.pos + self.momentum*damping
        self.momentum = self.momentum * (1-friction)
        x, y = self.pos
        #Check boundaries
        if y >= height-self.size:
            self.pos[1] = height-self.size
            self.momentum[1] = min(0, -self.momentum[1])
        if x <= self.size:
            self.pos[0] = self.size
            self.momentum[0] = max(0, -self.momentum[0])
        if x >= width-self.size:
            self.pos[0] = width-self.size
            self.momentum[0] = min(0, -self.momentum[0])
        if y <= self.size:
            self.pos[1] = self.size
            self.momentum[1] = max(0, -self.momentum[1])
    
    def distance(self, fruit):
        return np.linalg.norm(self.pos - fruit.pos)
    
    def touch(self, fruit):
        return self.distance(fruit) <= self.size + fruit.size

    def updateX(self, x):
        self.pos[0] = x

class Cherry(Fruit):
    def __init__(self, x, y):
        super().__init__([x, y], 1*size_ratio, (210, 4, 45))
        self.type = "cherry"
    
    def next(self, fruit):
        return Strawberry(abs(self.pos[0] + fruit.pos[0]) / 2, abs(self.pos[1] + fruit.pos[1]) / 2)

class Strawberry(Fruit):
    def __init__(self, x, y):
        super().__init__([x, y], 2*size_ratio, (200, 63, 73))
        self.type = "apple"
    
    def next(self, fruit):
        return Grape(abs(self.pos[0] + fruit.pos[0]) / 2, abs(self.pos[1] + fruit.pos[1]) / 2)

class Grape(Fruit):
    def __init__(self, x, y):
        super().__init__([x, y], 3*size_ratio, (111, 45, 168))
        self.type = "grape"
    
    def next(self, fruit):
        return Dekopon(abs(self.pos[0] + fruit.pos[0]) / 2, abs(self.pos[1] + fruit.pos[1]) / 2)

class Dekopon(Fruit):
    def __init__(self, x, y):
        super().__init__([x, y], 4*size_ratio, (240,152,77))
        self.type = "dekopon"
    
    def next(self, fruit):
        return Orange(abs(self.pos[0] + fruit.pos[0]) / 2, abs(self.pos[1] + fruit.pos[1]) / 2)

class Orange(Fruit):
    def __init__(self, x, y):
        super().__init__([x, y], 5*size_ratio, (240, 133, 45))
        self.type = "orange"
    
    def next(self, fruit):
        return Apple(abs(self.pos[0] + fruit.pos[0]) / 2, abs(self.pos[1] + fruit.pos[1]) / 2)

class Apple(Fruit):
    def __init__(self, x, y):
        super().__init__([x, y], 6*size_ratio, (200, 55, 47))
        self.type = "apple"
    
    def next(self, fruit):
        return Pear(abs(self.pos[0] + fruit.pos[0]) / 2, abs(self.pos[1] + fruit.pos[1]) / 2)

class Pear(Fruit):
    def __init__(self, x, y):
        super().__init__([x, y], 7*size_ratio, (82, 89, 19))
        self.type = "pear"
    
    def next(self, fruit):
        return Peach(abs(self.pos[0] + fruit.pos[0]) / 2, abs(self.pos[1] + fruit.pos[1]) / 2)

class Peach(Fruit):
    def __init__(self, x, y):
        super().__init__([x, y], 8*size_ratio, (255, 203, 164))
        self.type = "peach"
    
    def next(self, fruit):
        return Pineapple(abs(self.pos[0] + fruit.pos[0]) / 2, abs(self.pos[1] + fruit.pos[1]) / 2)

class Pineapple(Fruit):
    def __init__(self, x, y):
        super().__init__([x, y], 9*size_ratio, (255, 234, 99))
        self.type = "pineapple"
    
    def next(self, fruit):
        return Melon(abs(self.pos[0] + fruit.pos[0]) / 2, abs(self.pos[1] + fruit.pos[1]) / 2)

class Melon(Fruit):
    def __init__(self, x, y):
        super().__init__([x, y], 10*size_ratio, (187,246,150))
        self.type = "melon"
    
    def next(self, fruit):
        return Watermelon(abs(self.pos[0] + fruit.pos[0]) / 2, abs(self.pos[1] + fruit.pos[1]) / 2)


class Watermelon(Fruit):
    def __init__(self, x, y):
        super().__init__([x, y], 11*size_ratio, (0, 47, 27))
        self.type = "Watermelon"
    
    def next(self, fruit):
        return Cherry(abs(self.pos[0] + fruit.pos[0]) / 2, abs(self.pos[1] + fruit.pos[1]) / 2)


