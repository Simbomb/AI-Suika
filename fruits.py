import pygame as pg
from physics import *

friction = 0.1
gravity = 0.001
class Fruit:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.momentum = np.array([0, 0], dtype='float64')
    
    def draw(self, screen):
        #Draw the fruit
        pg.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def updateX(self, x):
        self.x = x

    def boundary(self, height, width):
        if self.y >= height-self.size:
            self.y = height-self.size
        if self.x <= self.size:
            self.x = self.size
            self.momentum[0] = max(0, -0.5*self.momentum[0])
        if self.x >= width-self.size:
            self.x = width-self.size
            self.momentum[0] = min(0, -0.5*self.momentum[0])
    
    def update(self):
        self.momentum[1] += gravity
        self.x += self.momentum[0]
        self.y += self.momentum[1]

    def gravity(self, current_fruits):
        score = 0
        for fruit in current_fruits:
            if fruit is not self:
                collision, distance = collision_detection(self, fruit)
                #Touch
                if collision:
                    overlap, dx, dy = collision_resolution(self, fruit, distance)
                    self.x += dx * overlap + 0.5
                    self.y += dy * overlap / 2
                    fruit.x -= dx * overlap + 0.5
                    fruit.y -= dy * overlap / 2
                    self.momentum[1] = 0
                    fruit.momentum[1] = 0
                    self.momentum[0] *= 1
                    fruit.momentum[0] *= 1
                    #Upgrade fruits
                    if self.type == fruit.type:
                        next_fruit, score_add = self.next(fruit)
                        current_fruits.append(next_fruit)
                        current_fruits.remove(self)
                        current_fruits.remove(fruit)
                        score += score_add

        self.update()
        return score
        


class Cherry(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 15, (210, 4, 45))
        self.type = "cherry"
    
    def next(self, fruit):
        return Strawberry(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2), 2

class Strawberry(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 22, (200, 63, 73))
        self.type = "apple"
    
    def next(self, fruit):
        return Grape(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2), 4

class Grape(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 32, (111, 45, 168))
        self.type = "grape"
    
    def next(self, fruit):
        return Dekopon(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2), 6

class Dekopon(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 45, (240,152,77))
        self.type = "dekopon"
    
    def next(self, fruit):
        return Orange(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2), 8

class Orange(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 58, (240, 133, 45))
        self.type = "orange"
    
    def next(self, fruit):
        return Apple(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2), 10

class Apple(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 70, (200, 55, 47))
        self.type = "apple"
    
    def next(self, fruit):
        return Pear(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2), 12

class Pear(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 85, (82, 89, 19))
        self.type = "pear"
    
    def next(self, fruit):
        return Peach(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2), 14

class Peach(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 102, (255, 203, 164))
        self.type = "peach"
    
    def next(self, fruit):
        return Pineapple(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2), 16

class Pineapple(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 115, (255, 234, 99))
        self.type = "pineapple"
    
    def next(self, fruit):
        return Melon(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2), 18

class Melon(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 135, (187,246,150))
        self.type = "melon"
    
    def next(self, fruit):
        return Watermelon(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2), 20


class Watermelon(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 150, (0, 47, 27))
        self.type = "Watermelon"
    
    def next(self, fruit):
        return Cherry(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2), 22



