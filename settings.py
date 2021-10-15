import pygame


class Settings:

    def __init__(self):
        pygame.init()
        self.width = 600
        self.height = 800
        self.main_surface = pygame.display.set_mode((self.width, self.height))
        self.fps = 60

        #player settings

        self.p_speed = 1
        self.p_score = 0

        #ball settings

        self.b_speed = 0.3
