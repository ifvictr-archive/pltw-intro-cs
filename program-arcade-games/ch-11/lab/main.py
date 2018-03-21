import math
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SIZE = {"x": 800, "y": 500}

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

pygame.init()

screen = pygame.display.set_mode((SIZE["x"], SIZE["y"]))
clock = pygame.time.Clock()
done = False
bg_img = pygame.image.load("bg.png").convert()
in_dark_sound = pygame.mixer.Sound("in-dark.ogg")
on_wood_sound = pygame.mixer.Sound("on-wood.ogg")
spider = {
    "x": random.randint(50, SIZE["x"]),
    "y": random.randint(50, SIZE["y"])
}
move_x = 0
move_y = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # Move based on keypress
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move_x = -5
    if keys[pygame.K_RIGHT]:
        move_x = 5
    if keys[pygame.K_UP]:
        move_y = -5
    if keys[pygame.K_DOWN]:
        move_y = 5
    # Draw spider
    screen.blit(bg_img, (0, 0))
    spider["x"] += move_x
    spider["y"] += move_y
    if spider["x"] < 0 or spider["x"] > SIZE["x"]:
        spider["x"] -= move_x
    if spider["y"] < 0 or spider["y"] > SIZE["y"]:
        spider["y"] -= move_y
    # Play sound in certain area
    if spider["x"] > 280 and spider["x"] < 620 and spider["y"] > 147 and spider["y"] < 447:
        in_dark_sound.play()
    else:
        on_wood_sound.play()
    draw_spider(screen, spider["x"], spider["y"])
    # Reset so it doesn't keep moving
    move_x = 0
    move_y = 0
    pygame.display.flip()
    clock.tick(60)