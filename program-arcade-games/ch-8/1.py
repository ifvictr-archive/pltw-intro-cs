import pygame

AQUA = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.display.set_caption("Chapter 8.1")

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
done = False
# Starting position
rect_x = 50
rect_y = 50
# Rectangle's velocity
rect_change_x = 5
rect_change_y = 5

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, (rect_x, rect_y, 50, 50))
    pygame.draw.rect(screen, AQUA, (rect_x + 5, rect_y + 5, 40, 40))
    rect_x += rect_change_x
    rect_y += rect_change_y

    # Bounce off edges
    if rect_x < 0 or rect_x > 650:
        rect_change_x *= -1
    if rect_y < 0 or rect_y > 450:
        rect_change_y *= -1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()