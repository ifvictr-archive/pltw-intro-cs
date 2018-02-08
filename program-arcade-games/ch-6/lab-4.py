import pygame

BLACK = [0, 0, 0]
GREEN = [0, 0xff, 0]
done = False

pygame.init()
pygame.display.set_caption("Lab #4")

screen = pygame.display.set_mode([700, 500])
screen.fill(BLACK)

clock = pygame.time.Clock()

while not done:
    # Listen for program close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Draw rectangles
    for y in range(0, 500, 5):
        for x in range(0, 700, 5):
            pygame.draw.rect(screen, GREEN, [x, y, 3, 3])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()