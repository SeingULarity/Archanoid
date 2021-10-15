import random

import pygame
from pygame.sprite import Sprite
from settings import Settings
from player import Player
from circle import Circle
from tile import Tile


class Game:

    def __init__(self):
        pygame.init()
        super().__init__()
        self.settings = Settings()
        self.main_surface = self.settings.main_surface
        self.clock = pygame.time.Clock()

        self.player = Player((255, 0, 0), self.settings.p_speed, self.settings.p_score, 250, 755, 100, 20)
        self.circles = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

        for x in range(0, self.settings.width, 80):
            for y in range(0, self.settings.height - 400, 20):
                self.tiles.add(Tile((132, 15, 60), x, y, 30, 10))
        print(self.tiles)

        self.is_running = False

        self.moving_right = False
        self.moving_left = False

        self.collition_with_tile = False
        self.collition_with_player = False

    def run(self):
        self.is_running = True
        while self.is_running:
            self.handle_events()
            self.draw()
            self.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            self.handle_keydown_events(event)
            self.handle_keyup_events(event)

    def handle_keydown_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.stop()
            if event.key == pygame.K_LEFT:
                self.moving_left = True
            if event.key == pygame.K_RIGHT:
                self.moving_right = True
            if event.key == pygame.K_SPACE:
                ball = Circle((255, 25, 45), random.randint(self.player.rect.left, self.player.rect.right), self.player.rect.top - 40, 10)
                self.circles.add(ball)




    def handle_keyup_events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.moving_left = False
            if event.key == pygame.K_RIGHT:
                self.moving_right = False

    def draw(self):
        self.main_surface.fill((255, 255, 255))
        self.player.draw(self.main_surface)
        for ball in self.circles:
            ball.draw(self.main_surface)
        for tile in self.tiles:
            tile.draw(self.main_surface)

    def update(self):
        time = self.clock.tick(self.settings.fps)

        self.player.update(time, self.moving_right, self.moving_left)
        for ball in self.circles:
            ball.update(time)
        self.check_collition()
        #self.change_direction_ball()
        pygame.display.set_caption(f"Score: {self.settings.p_score}")
        pygame.display.update()

    def check_collition(self):
        for tile in self.tiles:
            for circle in self.circles:
                if tile.rect.colliderect(circle.rect):
                    circle.update_vector()
                    tile.remove(self.tiles)
                    self.settings.p_score += 1

        for circle in self.circles:
            #
            point = circle.rect.x + circle.radius * 2, circle.rect.y + circle.radius * 2

            if self.player.rect.colliderect(circle.rect):
                print(f"Poins: {point}      Distance_y: {self.player.rect}      {self.collition_with_player}")
                circle.update_vector()

            if point[1] >= self.settings.height:
                circle.remove(self.circles)
                #circle.update_vector()




    def stop(self):
        self.is_running = False


if __name__ == '__main__':
    game = Game()
    game.run()