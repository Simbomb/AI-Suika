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
DELAY = 20
random_fruit_class = random.choice(fruit_classes)
new_fruit = random_fruit_class(x, y)
running = True
while running:
    pg.time.delay(DELAY)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Handle user input
    keys = pg.key.get_pressed()
    x += (keys[pg.K_RIGHT] - keys[pg.K_LEFT])*DELAY
    #y += (keys[pg.K_DOWN] - keys[pg.K_UP])
    if keys[pg.K_SPACE] and not space_pressed:
        current_fruits.append(new_fruit)
        random_fruit_class = random.choice(fruit_classes)
        new_fruit = random_fruit_class(x, y)
        space_pressed = True
    if not keys[pg.K_SPACE]:
            space_pressed = False

    screen.fill((0, 0, 0))
    new_fruit.updateX(x)
    new_fruit.draw(screen)

    for fruit in current_fruits:
        fruit.move(SCREEN_HEIGHT, SCREEN_WIDTH) 
        fruit.draw(screen)

    handle_collision(current_fruits)
    #handle_overlap(current_fruits)

    pg.display.flip()


pg.quit()
