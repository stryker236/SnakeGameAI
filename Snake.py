import pygame

class Snake:
    def __init__(self,WIDTH,HEIGHT,SQUARE_SIZE):
        self.length = 1  # Initial length of the snake
        self.positions = [(SQUARE_SIZE,SQUARE_SIZE)]  # Initial position of the snake's head
        self.direction = pygame.K_RIGHT  # Initial direction (right)
        self.window_width = WIDTH
        self.window_height = HEIGHT
        self.square_size = SQUARE_SIZE

    def get_head_position(self):
        return self.positions[0]

    def move(self, direction):
        cur = self.get_head_position()
        x, y = cur

        if direction == pygame.K_UP:
            new = (x, y - self.square_size)
        elif direction == pygame.K_DOWN:
            new = (x, y + self.square_size)
        elif direction == pygame.K_LEFT:
            new = (x - self.square_size, y)
        elif direction == pygame.K_RIGHT:
            new = (x + self.square_size, y)

        self.positions.insert(0, new)

    def eat_food(self, food_position):
        # print("eat food function")
        # print(self.get_head_position())
        # print(food_position)
        # print()
        if self.get_head_position() == food_position:
            self.length += 1
            return True
        else:
            self.positions.pop()
            return False

    #collion with the walls or with himself
    def check_collision(self):
        head = self.get_head_position()
        if (
            head[0] >= self.window_width
            or head[0] < 0
            or head[1] >= self.window_height
            or head[1] < 0
            or head in self.positions[1:]
        ):
            return True
        else:
            return False
