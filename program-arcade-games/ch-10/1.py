import pygame

def draw_stick_figure(screen, x, y):
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)
    # Head
    pygame.draw.ellipse(screen, GREEN, [1 + x, y, 10, 10], 0)

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
SIZE = {"x": 400, "y": 500}

pygame.init()
pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((SIZE["x"], SIZE["y"]))
clock = pygame.time.Clock()
done = False
x = 10
y = 10
x_speed = 0
y_speed = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
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

    next_x = x + x_speed
    next_y = y + y_speed

    # Only allow movement if inside window
    if next_x >= 0 and (next_x + 17) <= SIZE["x"]:
        x = next_x
    if next_y >= 0 and (next_y + 27) <= SIZE["y"]:
        y = next_y
    draw_stick_figure(screen, next_x, next_y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()