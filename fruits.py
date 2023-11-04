import pygame as pg
from physics import *

size_ratio = 8
friction = 0.0
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

    def update(self):
        self.momentum *= (1-friction)
        self.x += self.momentum[0]
        self.y += self.momentum[1]

    def gravity(self, current_fruits):
        if self.y + self.size < 1000:
            no_touch = True
            for fruit in current_fruits:
                if fruit is not self:
                    collision, direction_vector, distance, momentum_vector = collision_detection(self, fruit)
                    #Touch
                    if collision:
                        
                        no_touch = False
                        self.momentum += momentum_vector
                        fruit.momentum -= momentum_vector
                        #Move fruit
                        self.x += direction_vector[0]
                        self.y += direction_vector[1]

                        #Upgrade fruits
                        if self.type == fruit.type:
                            current_fruits.append(self.next(fruit))
                            current_fruits.remove(self)
                            current_fruits.remove(fruit)

            #Gravity
            if no_touch:
                self.momentum[1] = 0.1
        self.update()
        
        


class Cherry(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 1*size_ratio, (210, 4, 45))
        self.type = "cherry"
    
    def next(self, fruit):
        return Strawberry(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2)

class Strawberry(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 2*size_ratio, (200, 63, 73))
        self.type = "apple"
    
    def next(self, fruit):
        return Grape(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2)

class Grape(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 3*size_ratio, (111, 45, 168))
        self.type = "grape"
    
    def next(self, fruit):
        return Dekopon(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2)

class Dekopon(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 4*size_ratio, (240,152,77))
        self.type = "dekopon"
    
    def next(self, fruit):
        return Orange(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2)

class Orange(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 5*size_ratio, (240, 133, 45))
        self.type = "orange"
    
    def next(self, fruit):
        return Apple(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2)

class Apple(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 6*size_ratio, (200, 55, 47))
        self.type = "apple"
    
    def next(self, fruit):
        return Pear(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2)

class Pear(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 7*size_ratio, (82, 89, 19))
        self.type = "pear"
    
    def next(self, fruit):
        return Peach(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2)

class Peach(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 8*size_ratio, (255, 203, 164))
        self.type = "peach"
    
    def next(self, fruit):
        return Pineapple(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2)

class Pineapple(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 9*size_ratio, (255, 234, 99))
        self.type = "pineapple"
    
    def next(self, fruit):
        return Melon(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2)

class Melon(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 10*size_ratio, (187,246,150))
        self.type = "melon"
    
    def next(self, fruit):
        return Watermelon(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2)


class Watermelon(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 11*size_ratio, (0, 47, 27))
        self.type = "Watermelon"
    
    def next(self, fruit):
        return Cherry(abs(self.x + fruit.x) / 2, abs(self.y + fruit.y) / 2)



