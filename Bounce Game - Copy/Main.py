import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

WIDTH, HEIGHT = 700, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce By @Ibrahim Faisal")

# Define the colors directly as global variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
orange = (255, 165, 0)
pink = (255, 192, 203)
gray = (128, 128, 128)
light_blue = (135, 206, 250)
dark_green = (0, 100, 0)

colors_list = [
    black,
    white,
    red,
    green,
    blue,
    yellow,
    purple,
    orange,
    pink,
    gray,
    light_blue,
    dark_green,
]

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)


class Ball(object):
    def __init__(self, x, y) -> None:
        self.colors = colors_list
        self.brown = (165, 42, 42)
        self.x = x
        self.y = y
        self.vel_x = random.choice([8, -8])
        self.vel_y = random.choice([8, -8])
        self.main_vel = 10
        self.color = random.choice(self.colors)  # Assign a random color to each ball

    def draw(self):
        pygame.draw.circle(SCREEN, self.color, (self.x, self.y), 20, 0)

        self.x += self.vel_x
        self.y += self.vel_y

    def move(self):
        if self.y < 0 + 20 or self.y > 600 - 20:
            self.vel_y = -self.vel_y

        if self.x < 0 + 20 or self.x > 700 - 20:
            self.vel_x = -self.vel_x


text = "Click!"
text_x = WIDTH - 125
text_y = 55


balls = []


def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    SCREEN.blit(text_surface, (x, y))


click = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    SCREEN.fill((255, 255, 255))
    Button = pygame.draw.rect(
        SCREEN, (255, 0, 0), (WIDTH - 140, 40, 120, 60), border_radius=20
    )

    if event.type == MOUSEBUTTONDOWN and not click:
        pos = pygame.mouse.get_pos()
        if Button.collidepoint(pos):
            ball = Ball(WIDTH // 2, 45)
            balls.append(ball)
            click = True

    if event.type == MOUSEBUTTONUP:
        click = False

    display_text(text, (0, 0, 0), text_x, text_y)

    for i in balls:
        i.move()
        i.draw()

    pygame.display.update()
    clock.tick(60)
