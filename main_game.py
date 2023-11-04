import numpy as np
import pygame as pg
import random

from fruits import *

pg.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 1000

current_fruits = []
fruit_classes = [Cherry, Strawberry, Grape, Dekopon, Orange, Apple, Pear, Peach, Pineapple, Melon, Watermelon]
#fruit_classes = [Cherry, Strawberry, Grape, Dekopon, Orange]

space_pressed = False

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Suika Game")
x, y = SCREEN_WIDTH // 2, 0

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Handle user input
    keys = pg.key.get_pressed()
    x += (keys[pg.K_RIGHT] - keys[pg.K_LEFT])
    #y += (keys[pg.K_DOWN] - keys[pg.K_UP])
    if keys[pg.K_SPACE] and not space_pressed:
        random_fruit_class = random.choice(fruit_classes)
        new_fruit = random_fruit_class(x, y)
        current_fruits.append(new_fruit)
        space_pressed = True
    if not keys[pg.K_SPACE]:
            space_pressed = False

    screen.fill((0, 0, 0))


    #Go through each fruits functions
    current_fruits.sort(key=lambda fruit: fruit.y)
    for fruit in current_fruits:     
        fruit.gravity(current_fruits)
        fruit.x = max(fruit.size, min(SCREEN_WIDTH - fruit.size, fruit.x))
        fruit.y = max(fruit.size, min(SCREEN_HEIGHT - fruit.size, fruit.y))
        fruit.draw(screen)




    pg.display.flip()


pg.quit()
