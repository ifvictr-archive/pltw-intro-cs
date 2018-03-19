import pygame

BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Chapter 11")
pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
done = False
# Load images
bg_img = pygame.image.load("bg.png").convert()
player_img = pygame.image.load("player.png").convert()
player_img.set_colorkey(BLACK)
# Load sounds
click_sound = pygame.mixer.Sound("laser.ogg")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()

    screen.blit(bg_img, (0, 0))
    player_pos = pygame.mouse.get_pos()
    screen.blit(player_img, player_pos)

    pygame.display.flip()
    clock.tick(60)