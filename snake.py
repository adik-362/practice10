import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
BLOCK = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Snake settings
snake = [(100, 100)]
direction = (BLOCK, 0)

# Food
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, BLOCK)
        y = random.randrange(0, HEIGHT, BLOCK)
        if (x, y) not in snake:
            return (x, y)

food = generate_food()

# Game variables
score = 0
level = 1
speed = 10

font = pygame.font.SysFont(None, 30)

def draw_text():
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

running = True
while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, BLOCK):
                direction = (0, -BLOCK)
            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK):
                direction = (0, BLOCK)
            elif event.key == pygame.K_LEFT and direction != (BLOCK, 0):
                direction = (-BLOCK, 0)
            elif event.key == pygame.K_RIGHT and direction != (-BLOCK, 0):
                direction = (BLOCK, 0)

    # Move snake
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    new_head = (head_x, head_y)

    # ❗ 1. Border collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over: hit wall")
        running = False

    # ❗ Self collision
    if new_head in snake:
        print("Game Over: hit itself")
        running = False

    snake.insert(0, new_head)

    # ❗ 2. Eating food
    if new_head == food:
        score += 1
        food = generate_food()

        # ❗ 3. Levels
        if score % 3 == 0:
            level += 1
            speed += 2   # ❗ 4. Increase speed

    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK, BLOCK))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))

    # ❗ 5. Draw score and level
    draw_text()

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()