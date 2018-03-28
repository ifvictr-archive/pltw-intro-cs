import pygame
import random

BLACK = (0, 0, 0)
SIZE = {"x": 700, "y": 500}

class Shape():
    def __init__(self):
        self.width = random.randint(20, 70)
        self.height = random.randint(20, 70)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_width = random.randint(0, 5)
        self.x = random.randint(0, SIZE["x"] - self.width)
        self.y = random.randint(0, SIZE["y"] - self.height)
        self.change_x = random.randint(-3, 3)
        self.change_y = random.randint(-3, 3)

    def check_bounds(self):
        if self.x <= 0 or (self.x + self.width) >= SIZE["x"]:
            self.change_x *= -1
        if self.y <= 0 or (self.y + self.height) >= SIZE["y"]:
            self.change_y *= -1

    def move(self):
        self.check_bounds()
        self.x += self.change_x
        self.y += self.change_y


class Ellipse(Shape):
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.width, self.height], self.border_width)


class Rectangle(Shape):
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height], self.border_width)


class Triangle(Shape):
    def __init__(self):
        super().__init__()
        # TODO: Find better attribute names
        self.extra_width = random.randint(-20, 20)
        self.extra_height = random.randint(-20, 20)

    def check_bounds(self):
        vertices = self.get_vertices()
        x_list = [vertex[0] for vertex in vertices]
        y_list = [vertex[1] for vertex in vertices]
        if min(x_list) <= 0 or max(x_list) >= SIZE["x"]:
            self.change_x *= -1
        if min(y_list) <= 0 or max(y_list) >= SIZE["y"]:
            self.change_y *= -1

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.get_vertices(), self.border_width)

    def get_vertices(self):
        return [
            [self.x, self.y],
            [self.x - self.width + self.extra_width, self.y + self.height + self.extra_height],
            [self.x + self.width + self.extra_width, self.y + self.height - self.extra_height]
        ]


pygame.init()

screen = pygame.display.set_mode((SIZE["x"], SIZE["y"]))
clock = pygame.time.Clock()
done = False
shapes = []

for _ in range(20):
    shapes.append(Ellipse())
for _ in range(20):
    shapes.append(Rectangle())
for _ in range(20):
    shapes.append(Triangle())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    for shape in shapes:
        shape.move()
        shape.draw(screen)

    pygame.display.flip()
    clock.tick(60)