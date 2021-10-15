import pygame
from pygame.sprite import Sprite


class Tile(Sprite):

    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        pass