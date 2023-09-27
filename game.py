# Example file showing a circle moving on screen
import pygame
from Snake import Snake
from Food import Food
from autonomous_move import auto_move1, manual_move
import Q_learning as ql
import json
import requests
from tinydb import TinyDB, Query
# import server


WIDTH = 1000
HEIGHT = 1000
SQUARE_SIZE = 100
N_ROWS = 10
N_COLS = 10
FPS = 5
db = TinyDB("test.json")


total_food_eaten = 0
total_frame_count = 0
food_eaten = 0
frame_count = 0
longest_run = 0
highest_score = 0
deaths = 0


def reset_game(snake, food):
    snake.length = 1
    snake.positions = [(1,1)]
    snake.direction = pygame.K_RIGHT  # Start moving up
    food.is_food_on_screen = True
    food.spawn_food()

# pygame setup
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")



clock = pygame.time.Clock()
running = True
dt = 0

snake = Snake(N_ROWS,N_COLS)
food = Food(N_ROWS,N_COLS)
food.spawn_food()

Q = {}
n_episodes = 1000  # Number of training episodes
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.2  # Initial exploration rate
epsilon_decay_factor = 0.995  # Rate at which epsilon decreases over episodes

learning_rate = 0.1
discount_factor = 0.9


# IMPLEMENTAR Q-LEARNING 
# get current state
# calucate action
# calculate next state
# update q_table
# calculate the best_next_step
# update weights
# move the

while running:
    total_frame_count += 1
    frame_count += 1
    for event in pygame.event.get():
        key = True
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and key:
            manual_move(snake,event)
            key = False
            break

    # Move the snake
    snake.move(snake.direction)

    #Eat food
    if snake.eat_food(food.position):
        food.set_food_on_screen(False)

    # Check for collisions
    # if snake.check_collision():
    #     reset_game(snake, food)
    #     deaths += 1
    #     food_eaten = 0
    #     frame_count = 0
    
    if snake.check_collision():
        # Game over logic
        flag = True
        print("Game Over! Press 'R' to restart or 'Q' to quit.")
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # reset_game(snake, food)
                        db.insert({"pos":snake.positions})
                        response = requests.post("http://127.0.0.1:5000/data",json={"snake":str(snake.positions)})
                        # response = requests.post("http://127.0.0.1:5000/data",json={"snake":"COBRINNHA"})
                        # response = requests.post("http://127.0.0.1:5000/data",json="OLA")
                        print(response.content.decode())
                        snake.length = 1
                        snake.positions = [(1,1)]
                        snake.direction = pygame.K_RIGHT  # Start moving up
                        food.is_food_on_screen = False
                        food.spawn_food()
                        flag = False
                        break
                    elif event.key == pygame.K_q:
                        running = False
                        flag = False
                        break

    # Spawn new food if it's not on the screen
    if not food.is_food_on_screen:
        food_position = food.spawn_food()
        food.set_food_on_screen(True)

    # Clear the screen
    screen.fill("black")

    snake_color = "#64646333"
    #Draw the snake
    # pygame.draw.rect(screen, (200,200,200,0), pygame.Rect(2*SQUARE_SIZE, 2*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    for segment in snake.positions:
        # pygame.draw.rect(screen, pygame.Color(255,255,255,0.2), pygame.Rect(segment[0]*SQUARE_SIZE, segment[1]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(screen, snake_color, pygame.Rect(segment[0]*SQUARE_SIZE, segment[1]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    #Draw the food
    if food.is_food_on_screen:
        pygame.draw.rect(screen, "red", pygame.Rect(food.position[0]*SQUARE_SIZE, food.position[1]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Display frame count and food eaten
    # font = pygame.font.Font(None, 36)

    # total_frame_text = font.render(f"Total Frames: {total_frame_count}", True, "green")
    # total_food_text = font.render(f"Total Food eaten: {total_food_eaten}", True, "green")
    # frame_text = font.render(f"Frames: {frame_count}", True, "green")
    # food_text = font.render(f"Food eaten: {food_eaten}", True, "green")
    # highest_score_text = font.render(f"Highest_food_eaten: {highest_score}", True, "green")
    # highest_frame_text = font.render(f"Highest frames: {longest_run}", True, "green")
    # deaths_text = font.render(f"Deaths: {deaths}", True, "green")
    
    
    # screen.blit(total_frame_text, (10, 50))    
    # screen.blit(total_food_text, (10, 10))
    # screen.blit(frame_text, (10, 90))    
    # screen.blit(food_text, (10, 130))    
    # screen.blit(highest_score_text, (10, 170))    
    # screen.blit(highest_frame_text, (10, 210))    
    # screen.blit(deaths_text, (10, 250))    

    # Update display
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(FPS)/1000

# with open('qtable.json', 'w') as json_file:
#     json.dump(Q, json_file)


pygame.quit()

