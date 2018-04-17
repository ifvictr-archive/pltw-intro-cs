import pygame
import random

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
SIZE = {"x": 700, "y": 400}

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()

        pygame.draw.rect(self.image, color, [0, 0, width, height])

    def update(self):
        self.rect.y += 1
        if self.rect.y > SIZE["y"]:
            self.reset_pos()

    def reset_pos(self):
        self.rect.x = random.randint(0, SIZE["x"])
        self.rect.y = random.randint(-300, -20)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

        pygame.draw.rect(self.image, BLUE, [0, 0, x, y])
 
    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x < 0:
            self.rect.x = 0
            bump_sound.play()
        if (self.rect.x + self.rect.width) > SIZE["x"]:
            self.rect.x = SIZE["x"] - self.rect.width
            bump_sound.play()
        if self.rect.y < 0:
            self.rect.y = 0
            bump_sound.play()
        if (self.rect.y + self.rect.height) > SIZE["y"]:
            self.rect.y = SIZE["y"] - self.rect.height
            bump_sound.play()


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SIZE["x"], SIZE["y"]))
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 30)
good_block_sound = pygame.mixer.Sound("good_block.wav")
bad_block_sound = pygame.mixer.Sound("bad_block.wav")
bump_sound = pygame.mixer.Sound("bump.wav")
done = False
score = 0
good_blocks = pygame.sprite.Group()
bad_blocks = pygame.sprite.Group()
sprites = pygame.sprite.Group()

# Populate blocks and sprites
for _ in range(100):
    block = Block(GREEN, 20, 15)
    block.rect.x = random.randint(0, SIZE["x"])
    block.rect.y = random.randint(0, SIZE["y"])

    good_blocks.add(block)
    sprites.add(block)
for _ in range(100):
    block = Block(RED, 20, 15)
    block.rect.x = random.randint(0, SIZE["x"])
    block.rect.y = random.randint(0, SIZE["y"])

    bad_blocks.add(block)
    sprites.add(block)

# Add player
player = Player(random.randint(0, SIZE["x"]), random.randint(0, SIZE["y"]))
sprites.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_speed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.change_speed(3, 0)
            elif event.key == pygame.K_UP:
                player.change_speed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.change_speed(0, 3)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_speed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.change_speed(-3, 0)
            elif event.key == pygame.K_UP:
                player.change_speed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.change_speed(0, -3)        

    screen.fill(WHITE)
    sprites.update()
    # Check collisions with good blocks
    good_blocks_hit = pygame.sprite.spritecollide(player, good_blocks, True)
    for block in good_blocks_hit:
        score += 1
        good_block_sound.play()
    # Check collisions with bad blocks
    bad_blocks_hit = pygame.sprite.spritecollide(player, bad_blocks, True)
    for block in bad_blocks_hit:
        score -= 1
        bad_block_sound.play()

    sprites.draw(screen)

    # Display score
    score_display = font.render("Score: %d" % score, False, (0, 0, 0))
    screen.blit(score_display, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()