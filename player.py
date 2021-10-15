import pygame
from pygame.sprite import Sprite
from settings import Settings
import random


class Player:

    def __init__(self, color, speed, score, x, y, width, height,):
        super().__init__()
        self.color = color
        self.speed = speed
        self.score = score

        self.settings = Settings()

        self.rect = pygame.Rect(x, y, width, height)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)

    def update(self, time, moving_right, moving_left):

        if moving_right:
            self.rect.x += self.speed * time
            #print(self.speed * time)
        if moving_left:
            self.rect.x -= self.speed * time
            #print(self.speed * time)

        if self.rect.x + self.rect.width < 0:
            self.rect.x = self.settings.width
        if self.rect.x > self.settings.width:
            self.rect.x = -self.rect.width


