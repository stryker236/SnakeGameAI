import pygame
def manual_move(snake,event):
    if (event.key == pygame.K_UP or event.key == pygame.K_w) and snake.direction != pygame.K_DOWN:
        snake.direction = pygame.K_UP
    elif (event.key == pygame.K_DOWN or event.key == ord("s")) and snake.direction != pygame.K_UP:
        snake.direction = pygame.K_DOWN
    elif (event.key == pygame.K_LEFT or event.key == ord("a")) and snake.direction != pygame.K_RIGHT:
        snake.direction = pygame.K_LEFT
    elif (event.key == pygame.K_RIGHT or event.key == ord("d")) and snake.direction != pygame.K_LEFT:
        snake.direction = pygame.K_RIGHT

def auto_move1(snake, food_position):
    head_x, head_y = snake.get_head_position()
    food_x, food_y = food_position

    # Calculate horizontal and vertical distances to food
    dx = food_x - head_x
    dy = food_y - head_y

    # Determine the direction to move
    if abs(dx) > abs(dy):
        if dx > 0 and snake.direction != pygame.K_LEFT:
            return pygame.K_RIGHT
        elif dx < 0 and snake.direction != pygame.K_RIGHT:
            return pygame.K_LEFT
    else:
        if dy > 0 and snake.direction != pygame.K_UP:
            return pygame.K_DOWN
        elif dy < 0 and snake.direction != pygame.K_DOWN:
            return pygame.K_UP

    # If no valid direction found, keep moving in the current direction
    return snake.direction


