import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
pygame.display.set_icon(pygame.image.load("/Users/lingthang/randomPrograms/Snake/images/snake.png"))

# Define colors
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the initial positions
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_body = [list(snake_pos[0]), list(snake_pos[1]), list(snake_pos[2])]
snake_speed = 10

food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
food = pygame.Surface((10, 10))
food.fill(red)

direction = 'RIGHT'
change_to = direction

# Game over flag
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'

    # Validate the direction change
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Update the positions of the snake's body segments
    for i in range(len(snake_pos) - 1, 0, -1):
        snake_pos[i] = list(snake_pos[i - 1])

    # Update the snake position
    if direction == 'RIGHT':
        snake_pos[0][0] += snake_speed
    elif direction == 'LEFT':
        snake_pos[0][0] -= snake_speed
    elif direction == 'UP':
        snake_pos[0][1] -= snake_speed
    elif direction == 'DOWN':
        snake_pos[0][1] += snake_speed

    # Check for game over conditions
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= width or snake_pos[0][1] < 0 or snake_pos[0][1] >= height:
        game_over = True

    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over = True

    if game_over:
        break

    # Check if snake has eaten the food
    if snake_pos[0] == food_pos:
        snake_pos.append(list(snake_pos[-1]))
        food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
    # Update the screen
    screen.fill(black)
    for pos in snake_pos:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    screen.blit(food, food_pos)
    pygame.display.flip()

    # Set the game speed
    clock.tick(15)

if game_over:
    print("Game Over!")
    print("Your Score: ", len(snake_pos)-3)


# Quit the game
pygame.quit()

