import pygame
import random

class Food:
    # def __init__(self,WIDTH,HEIGHT,SQUARE_SIZE):
    def __init__(self,n_rows,n_cols):
        # self.position = (random.randrange(0, WIDTH/SQUARE_SIZE) * SQUARE_SIZE, random.randrange(0, HEIGHT/SQUARE_SIZE) * SQUARE_SIZE)  # Initial random position
        self.position = (random.randrange(0, n_rows), random.randrange(0, n_cols))  # Initial random position
        self.is_food_on_screen = True
        # self.width = WIDTH
        self.n_rows = n_rows
        # self.height = HEIGHT
        self.n_cols = n_cols
        # self.square_size = SQUARE_SIZE

    def spawn_food(self):
        if not self.is_food_on_screen:
            self.position = (random.randrange(0, self.n_rows) , random.randrange(0, self.n_cols))  # Initial random position
            self.is_food_on_screen = True
            return self.position

    def set_food_on_screen(self, choice):
        self.is_food_on_screen = choice

    def get_eaten(self, snake):
        if snake.get_head_position() == self.position:
            snake.length += 1
            return True
        else:
            snake.positions.pop()
            return False

