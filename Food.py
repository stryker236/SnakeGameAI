import pygame
import random

class Food:
    def __init__(self,WIDTH,HEIGHT,SQUARE_SIZE):
        self.position = (random.randrange(0, WIDTH/SQUARE_SIZE) * SQUARE_SIZE, random.randrange(0, HEIGHT/SQUARE_SIZE) * SQUARE_SIZE)  # Initial random position
        self.is_food_on_screen = True
        self.width = WIDTH
        self.height = HEIGHT
        self.square_size = SQUARE_SIZE

    def spawn_food(self):
        if not self.is_food_on_screen:
            self.position = (random.randrange(1, self.width/self.square_size) * self.square_size, random.randrange(1, self.height/self.square_size) * self.square_size)  # Initial random position
            self.is_food_on_screen = True
            return self.position

    def set_food_on_screen(self, choice):
        self.is_food_on_screen = choice
