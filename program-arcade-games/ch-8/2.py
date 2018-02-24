import pygame
import random

BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
WHITE = (255, 255, 255)

pygame.init()
pygame.display.set_caption("Chapter 8.2")

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
done = False
snow_list = []

for i in range(200):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    snow_list.append([x, y])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    for flake in snow_list:
        pygame.draw.circle(screen, WHITE, flake, 2)
        flake[1] += 1
        # Snowflake moved off screen, so move back to top
        if flake[1] > 500:
            flake[0] = random.randrange(0, 700)
            flake[1] = random.randrange(-50, -10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()