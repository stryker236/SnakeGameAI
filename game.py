# Example file showing a circle moving on screen
import pygame
from Snake import Snake
from Food import Food
from autonomous_move import auto_move1, manual_move

def reset_game(snake, food):
    snake.length =  1
    snake.positions = [(100, 40)]
    snake.direction = pygame.K_RIGHT  # Start moving up
    # snake.grow = False
    food.is_food_on_screen = False
    food.spawn_food()

# pygame setup
pygame.init()
WIDTH = 1200
HEIGHT = 1000
SQUARE_SIZE = 20
food_eaten = 0
frame_count = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")



clock = pygame.time.Clock()
running = True
dt = 0

snake = Snake(WIDTH,HEIGHT,SQUARE_SIZE)
food = Food(WIDTH,HEIGHT,SQUARE_SIZE)
food.spawn_food()



    
while running:
    frame_count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        #     manual_move(snake,event)
             
    # snake.direction = auto_move1(snake,food.position)
    # Move the snake
    snake.move(snake.direction)


    # Check if the snake has eaten the food
    if snake.eat_food(food.position):
        food_eaten += 1
        food.set_food_on_screen(False)

    if snake.check_collision():
        # Game over logic
        print("Game Over! Press 'R' to restart or 'Q' to quit.")
        aux = True
        while aux:
            # print("devia ficar aqui preso2")
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_r:
                        reset_game(snake, food)
                        # snake = Snake(WIDTH,HEIGHT,SQUARE_SIZE)
                        aux = False
                        break
                    elif event.key == pygame.K_q:
                        running = False
                        aux = False
                        break
    # # Check for collisions
    # if snake.check_collision():
    #     running = False

    print("Snake head:",snake.positions)
    print("Snake len:",snake.length)


    # Spawn new food if it's not on the screen
    if not food.is_food_on_screen:
        food_position = food.spawn_food()
        food.set_food_on_screen(True)

    # Clear the screen
    screen.fill("black")

    
    #Draw the snake
    for segment in snake.positions:
        pygame.draw.rect(screen, "white", pygame.Rect(segment[0], segment[1], SQUARE_SIZE, SQUARE_SIZE))
    #Draw the food
    # if food.is_food_on_screen:
    pygame.draw.rect(screen, "red", pygame.Rect(food.position[0], food.position[1], SQUARE_SIZE, SQUARE_SIZE))

    # Display frame count and food eaten
    font = pygame.font.Font(None, 36)
    frame_text = font.render(f"Frames: {frame_count}", True, "white")
    food_text = font.render(f"Food eaten: {food_eaten}", True, "white")
    screen.blit(frame_text, (10, 10))
    screen.blit(food_text, (10, 50))    

    # Update display
    # pygame.display.update()
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.da
    dt = clock.tick(30)/1000


pygame.quit()

