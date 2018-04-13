import pygame
import random

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
SIZE = {"x": 700, "y": 400}

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        pygame.draw.rect(self.image, color, [0, 0, width, height])

    def update(self):
        self.rect.y += 1
        if self.rect.y > SIZE["y"]:
            self.reset_pos()

    def reset_pos(self):
        self.rect.x = random.randint(0, SIZE["x"])
        self.rect.y = random.randint(-300, -20)


pygame.init()

screen = pygame.display.set_mode([700, 400])
clock = pygame.time.Clock()
done = False
score = 0
blocks = pygame.sprite.Group()
sprites = pygame.sprite.Group()

# Populate blocks and sprites
for _ in range(50):
    block = Block(BLACK, 20, 15)
    block.rect.x = random.randint(0, SIZE["x"])
    block.rect.y = random.randint(0, SIZE["y"])

    blocks.add(block)
    sprites.add(block)

player = Block(RED, 20, 15)
sprites.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    mouse_pos = pygame.mouse.get_pos()
    player.rect.x = mouse_pos[0]
    player.rect.y = mouse_pos[1]

    blocks.update()

    blocks_hit = pygame.sprite.spritecollide(player, blocks, True)
    for block in blocks_hit:
        score += 1
        print(score)

    sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()