import numpy as np
import pygame as pg
import random
from fruits import *

pg.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
random.seed(2)
DELAY = 1
clock = pg.time.Clock()
cooldown_timer = -1000
score = 0
current_fruits = []
lost = False
#fruit_classes = [Cherry, Strawberry, Grape, Dekopon, Orange, Apple, Pear, Peach, Pineapple, Melon, Watermelon]
fruit_classes = [Cherry, Cherry, Cherry, Strawberry, Strawberry, Strawberry, Grape, Grape, Dekopon, Orange]
#fruit_distribution = [0.3, 0.3, 0.2, 0.1, 0.1]

space_pressed = False

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Suika Game")
x, y = SCREEN_WIDTH // 2, 0
random_fruit_class = random.choice(fruit_classes)
new_fruit = random_fruit_class(x, y)
running = True
while running:
    pg.time.delay(DELAY)
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        else:
            if keys[pg.K_r]:
                current_fruits = []
                cooldown_timer = -1000
                score = 0
                random_fruit_class = random.choice(fruit_classes)
                new_fruit = random_fruit_class(x, y)
                random.seed(2)
                lost = False
            elif keys[pg.K_ESCAPE]:
                running = False
    screen.fill((0, 0, 0))
    if not lost:
        # Handle user input
        x += (keys[pg.K_RIGHT] - keys[pg.K_LEFT])/ 2
        #y += (keys[pg.K_DOWN] - keys[pg.K_UP])
        if keys[pg.K_SPACE] and not space_pressed and pg.time.get_ticks() - cooldown_timer > 1000:
            current_fruits.append(new_fruit)
            #random_fruit_class = np.random.choice(fruit_classes, p=fruit_distribution)
            random_fruit_class = random.choice(fruit_classes)
            new_fruit = random_fruit_class(x, y)
            cooldown_timer = pg.time.get_ticks()

            space_pressed = True

        if not keys[pg.K_SPACE]:
                space_pressed = False
        new_fruit.updateX(x)

        new_fruit.draw(screen)
        #Go through each fruits functions
        current_fruits.sort(key=lambda fruit: fruit.y)
        for fruit in current_fruits:
            score += fruit.gravity(current_fruits)
            fruit.boundary(SCREEN_HEIGHT, SCREEN_WIDTH)
            lost = check_game_over(fruit)
            fruit.draw(screen)
        
        #Draw score
        font = pg.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))

    if lost:
        font = pg.font.Font(None, 36)
        game_over_text_lines = [
            "GAME OVER",
            f"Your Score is: {score}",
            "restart by pressing R",
            "quit game by pressing ESCAPE"
        ]
        for i, line in enumerate(game_over_text_lines):
            line_text = font.render(line, True, (255, 255, 255))
            screen.blit(line_text, (SCREEN_WIDTH / 2 - line_text.get_width() / 2, SCREEN_HEIGHT / 2 - line_text.get_height() / 2 + i * line_text.get_height()))
        pg.display.update()


    pg.display.flip()


pg.quit()
