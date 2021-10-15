import pygame
import random
from settings import Settings
from pygame.sprite import Sprite


class Circle(Sprite):

    def __init__(self, color, x, y, radius):
        super().__init__()
        self.radius = radius
        self.color = color
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)

        self.settings = Settings()

        self.vector = pygame.Vector2(1, 1)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)

    def update(self, time):
        self.vector = self.vector.normalize()

        self.rect.x += self.settings.b_speed * time * self.vector.x
        self.rect.y -= self.settings.b_speed * time * self.vector.y

        if self.rect.x >= self.settings.width - self.rect.width:
            self.vector.x = -self.vector.x

        if self.rect.x <= 0:
            self.vector.x = -self.vector.x

    def update_vector(self):
        self.vector.y = -self.vector.y
        #print(self.vector.y)


