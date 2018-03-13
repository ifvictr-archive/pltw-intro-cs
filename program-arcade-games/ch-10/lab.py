import math
import pygame
import random

def draw_computer(screen, x, y):
    # Bezel
    pygame.draw.rect(screen, LIGHT_GRAY, [x, y, 100, 80])
    # Screen
    pygame.draw.rect(screen, BLACK, [x + 10, y + 10, 80, 60])
    # Middle thing
    pygame.draw.rect(screen, GRAY, [x + 30, y + 80, 40, 10])
    # Foot
    pygame.draw.rect(screen, LIGHT_GRAY, [x + 10, y + 90, 80, 10])
    # Lines of code
    for i in range(0, 10):
        pygame.draw.line(screen, random.choice(COLORS), [x + 15, y + 15 + (i * 5)], [x + 15 + random.randint(10, 50), y + 15 + (i * 5)], 2)

def draw_spider(screen, x, y):
    # Body
    pygame.draw.circle(screen, BLACK, [x, y], 40)
    # Left legs
    for i in range(-35, 11, 15):
        pygame.draw.arc(screen, BLACK, [x - 60, y + i, 50, 50], 0, math.pi, 5)
    # Right legs
    for i in range(-35, 11, 15):
        pygame.draw.arc(screen, BLACK, [x + 10, y + i, 50, 50], 0, math.pi, 5)
    # Left eye
    pygame.draw.circle(screen, WHITE, [x - 20, y + 10], 10)
    pygame.draw.circle(screen, BLACK, [x - 20, y + 10], 5)
    # Right eye
    pygame.draw.circle(screen, WHITE, [x + 20, y + 10], 10)
    pygame.draw.circle(screen, BLACK, [x + 20, y + 10], 5)
    # Mouth
    pygame.draw.arc(screen, WHITE, [x - 25, y - 15, 50, 50], 5 * math.pi / 4, 7 * math.pi / 4, 5)

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
LIGHT_GRAY = (211, 211, 211)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
COLORS = (
    BLUE,
    GREEN,
    RED,
    WHITE
)
SIZE = {"x": 400, "y": 500}

pygame.init()

screen = pygame.display.set_mode((SIZE["x"], SIZE["y"]))
clock = pygame.time.Clock()
done = False
computer_x = 300
computer_y = 300
spider_x = 100
spider_y = 100
x_speed = 0
y_speed = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            spider_x = event.pos[0]
            spider_y = event.pos[1]
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    screen.fill(WHITE)

    # Only allow movement if inside window
    next_x = computer_x + x_speed
    next_y = computer_y + y_speed    
    if next_x >= 0 and next_x <= SIZE["x"] - 100:
        computer_x = next_x
    if next_y >= 0 and next_y <= SIZE["y"] - 100:
        computer_y = next_y
    draw_computer(screen, computer_x, computer_y)

    draw_spider(screen, spider_x, spider_y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()