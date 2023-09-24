import pygame as pg
import random
# Define possible actions
# ACTIONS = [
#     "UP",
#     "DOWN",
#     "LEFT",
#     "RIGHT"
#     ]

ACTIONS = [
    pg.K_UP,
    pg.K_DOWN,
    pg.K_LEFT,
    pg.K_RIGHT,
    ]


# Initialize Q-table
Q = {}



# def initialize_q_table(Q,states, actions):
#     for state in states:
#         Q[state] = {}
#         for action in actions:
#             Q[state][action] = random.uniform(0, 0.1)
def update_q_table(Q,state, actions):
    if state not in Q:
        Q[state] = {}
        for action in actions:
            Q[state][action] = random.uniform(0, 0.1)

def get_game_state(snake, food, width, height):
    # Get the position of the snake's head
    snake_head = snake.positions[0]

    # Calculate the relative positions of food and obstacles
    food_x, food_y = food.position
    obstacles = []

    for x in range(width):
        for y in range(height):
            if (x, y) in snake.positions:
                obstacles.append((x, y))

    # Create a game state representation
    # state = {
    #     'snake_head': snake_head,
    #     'food_position': (food_x, food_y),
    #     'obstacles': obstacles,
    #     'snake_direction': snake.direction
    # }
    state = (snake_head,(food_x, food_y), tuple(obstacles),snake.direction)

    return state


def calculate_reward(snake, food, width, height):
    # Check if the snake has eaten food
    if snake.positions[0] == food.position:
        return 1000  # Positive reward for eating food
    
    # Check if the snake has collided with the wall or itself
    if (
        snake.positions[0][0] < 0
        or snake.positions[0][0] >= width
        or snake.positions[0][1] < 0
        or snake.positions[0][1] >= height
        or snake.positions[0] in snake.positions[1:]
    ):
        return -100  # Negative reward for collision
    # Default reward for moving
    return -20

def get_next_state(current_state, action):
    # Assuming that 'current_state' is a dictionary with relevant state information
    # 'action' is one of the possible actions (e.g., 'Up', 'Down', 'Left', 'Right')

    # Extract relevant information from the current state
    snake_head = current_state['snake_head']
    food_position = current_state['food_position']
    obstacles = current_state['obstacles']
    snake_direction = current_state['snake_direction']

    # Calculate the new position of the snake's head based on the action
    if action == 'Up':
        new_head = (snake_head[0], snake_head[1] - 1)
    elif action == 'Down':
        new_head = (snake_head[0], snake_head[1] + 1)
    elif action == 'Left':
        new_head = (snake_head[0] - 1, snake_head[1])
    elif action == 'Right':
        new_head = (snake_head[0] + 1, snake_head[1])

    # Create a new state representation with the updated information
    next_state = {
        'snake_head': new_head,
        'food_position': food_position,
        'obstacles': obstacles,
        'snake_direction': snake_direction  # You might also need to update the direction
    }

    return next_state


def q_learning(Q, state, actions, alpha, gamma, epsilon,snake,food,width,height):
    # Choose an action using an exploration strategy (epsilon-greedy)
    if random.uniform(0, 1) < epsilon:
        action = random.choice(actions)  # Explore
    else:
        action = max(Q[state], key=Q[state].get)  # Exploit

    # Execute the action and observe the new state and reward
    # (Code for updating the game state based on the chosen action goes here)

    # Calculate the new Q-value using the Q-learning update rule
    next_state = get_next_state(state, action)  # Implement this function
    reward = calculate_reward(snake,food,width,height)  # Implement this function
    best_next_action = max(Q[next_state], key=Q[next_state].get)
    Q[state][action] = Q[state][action] + alpha * (reward + gamma * Q[next_state][best_next_action] - Q[state][action])

    return action  # Return the chosen action
