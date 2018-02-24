import math
import pygame
import random

BLACK = (0, 0, 0)
BLUE = (37, 109, 123)
GRAY = (162, 168, 174)
GREEN = (113, 148, 90)
RED = (193,68,14)
WHITE = (255, 255, 255)
YELLOW = (253, 184, 19)

COLORS = [
    BLUE,
    GREEN,
    RED,
    YELLOW
]
SIZE = {"x": 1400, "y": 1000}

pygame.init()
pygame.display.set_caption("Chapter 8 Lab")

screen = pygame.display.set_mode((SIZE["x"], SIZE["y"]))
clock = pygame.time.Clock()
done = False
planets = []
stars = []

# Generate planets
for _ in range(20):
    # Planet
    planet = {
        # TODO: Prevent overlaps
        "x": random.randrange(0, SIZE["x"]),
        "y": random.randrange(0, SIZE["x"]),
        "color": random.choice(COLORS),
        "size": random.randrange(5, 40)
    }
    # Optional moon
    planet["moon"] = {
        "offset_x": (-1 if random.randrange(0, 2) == 0 else 1) * planet["size"] + random.randrange(-10, 10),
        "offset_y": (-1 if random.randrange(0, 2) == 0 else 1) * planet["size"] + random.randrange(-10, 10),
        "size": math.ceil(planet["size"] / 4)
    } if random.randrange(0, 10) == 0 else {}
    planets.append(planet)

# Generate stars
for _ in range(100):
    star = {
        "x": random.randrange(SIZE["x"] * -0.25, SIZE["x"] * 1.25),
        "y": random.randrange(SIZE["y"] * -0.25, SIZE["y"] * 1.25),
        "size": 2
    }
    stars.append(star)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            change_by = event.rel
        elif event.type == pygame.QUIT:
            done = True        

    screen.fill(BLACK)

    for star in stars:
        pygame.draw.circle(screen, WHITE, (star["x"], star["y"]), star["size"])
        star["x"] -= int(change_by[0] / 5)
        star["y"] -= int(change_by[1] / 5)
        if random.randrange(0, 100) < 1:
            star["size"] = 3 if star["size"] == 2 else 2
    for planet in planets:
        planet["x"] += int(change_by[0] / 5)
        planet["y"] += int(change_by[1] / 5)
        pygame.draw.circle(screen, planet["color"], (planet["x"], planet["y"]), planet["size"])
        # Draw moon if planet has one
        moon = planet["moon"]
        if moon:
            pygame.draw.circle(screen, GRAY, (planet["x"] + moon["offset_x"], planet["y"] + moon["offset_y"]), moon["size"])

    # Reset so objects stop moving after user stops moving mouse
    change_by = (0, 0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()