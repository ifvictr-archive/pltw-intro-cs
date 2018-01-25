import pygame

RED = [0xee, 0x06, 0x06]
WHITE = [0xee, 0xee, 0xee]

pygame.init()

# Window stuff
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("Supreme")

# Supreme's red background
screen = pygame.display.set_mode([400, 100])
screen.fill(RED)

# Text overlaying the background
font = pygame.font.Font("futura.ttf", 64)
text = font.render("Supreme", True, WHITE)
screen.blit(text, [60, 10])

pygame.display.flip()
pygame.time.delay(10000)