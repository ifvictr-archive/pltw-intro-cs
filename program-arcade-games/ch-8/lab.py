import math
import pygame
import random

BLACK = (0, 0, 0)
BLUE = (37, 109, 123)
COMET_BLUE = (204, 255, 255)
GRAY = (162, 168, 174)
GREEN = (113, 148, 90)
LIGHT_VIOLET = (217, 221, 244)
ORANGE = (255, 102, 0)
RED = (193, 68, 14)
URANUS_BLUE = (209, 231, 231)
WHITE = (255, 255, 255)
YELLOW = (253, 184, 19)

COLORS = [
    BLUE,
    GREEN,
    LIGHT_VIOLET,
    ORANGE,
    RED,
    URANUS_BLUE,
    YELLOW
]
SIZE = {"x": 1400, "y": 1000}

pygame.init()
pygame.display.set_caption("Chapter 8 Lab")

screen = pygame.display.set_mode(SIZE.values())
clock = pygame.time.Clock()
done = False
stars = []
planets = []
comets = []

# Generate stars
for _ in range(100):
    star = {
        "x": random.randint(SIZE["x"] * -0.25, SIZE["x"] * 1.25),
        "y": random.randint(SIZE["y"] * -0.25, SIZE["y"] * 1.25),
        "size": 2
    }
    stars.append(star)

# Generate planets
for i in range(20):
    # Planet
    planet = {
        "x": (i * 75) - 50,
        "y": random.randint(0, SIZE["x"]),
        "color": random.choice(COLORS),
        "size": random.randint(5, 40)
    }
    # Optional moon
    planet["moon"] = {
        "offset_x": (-1 if random.randint(0, 2) == 0 else 1) * planet["size"] + random.randint(-10, 10),
        "offset_y": (-1 if random.randint(0, 2) == 0 else 1) * planet["size"] + random.randint(-10, 10),
        "size": math.ceil(planet["size"] / 4)
    } if random.randint(0, 10) == 0 else {}
    planets.append(planet)

# Generate comets
for i in range(random.randint(1, 5)):
    comet = {
        "x": random.randint(0, SIZE["x"]),
        "y": random.randint((i + 1) * -100, 0),
        "velocity_x": random.randint(-20, 20),
        "velocity_y": random.randint(5, 20),
        "size": random.randint(3, 8)
    }
    comets.append(comet)

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
        if random.randint(0, 100) < 1:
            star["size"] = 3 if star["size"] == 2 else 2
    for planet in planets:
        planet["x"] += int(change_by[0] / 5) - 1
        planet["y"] += int(change_by[1] / 5)
        pygame.draw.circle(screen, planet["color"], (planet["x"], planet["y"]), planet["size"])
        # Draw moon if planet has one
        moon = planet["moon"]
        if moon:
            pygame.draw.circle(screen, GRAY, (planet["x"] + moon["offset_x"], planet["y"] + moon["offset_y"]), moon["size"])
        # Cycle planet from right side if off-screen
        if planet["x"] < int(SIZE["x"] * -0.25):
            planet["x"] = int(SIZE["x"] * 1.25)
    for comet in comets:
        # Comet's tail
        for i in range(comet["size"]):
            pygame.draw.circle(
                screen,
                COMET_BLUE,
                (comet["x"] - math.ceil(comet["velocity_x"] / 2) * i, comet["y"] - math.ceil(comet["velocity_y"] / 2) * i),
                comet["size"] - i
            )
        comet["x"] += comet["velocity_x"]
        comet["y"] += comet["velocity_y"]
        # Move comet if no longer on-screen
        if comet["x"] < 0 or comet["x"] > SIZE["x"] or comet["y"] > SIZE["y"]:
            comet["x"] = random.randint(0, SIZE["x"])
            comet["y"] = random.randint(-1000, -500)     
            comet["velocity_x"] = random.randint(-20, 20)
            comet["velocity_y"] = random.randint(5, 10)    

    # Reset so objects stop moving after user stops moving mouse
    change_by = (0, 0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()