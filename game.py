import pygame
import config
from level import Level
from player import Player
from enemy import Enemy


class Game:

    def __init__(self):
        pygame.init()
        self.game_screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.player = Player(375, 0)
        self.level = Level(self.game_screen, config.map_data)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.player.move("left")
        elif keys[pygame.K_d]:
            self.player.move("right")
        else:
            self.player.move("clear")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.move("jump")

    def process(self):
        if self.player.rect.bottom > config.SCREEN_HEIGHT:
            self.player.rect.x = config.SCREEN_WIDTH/2
            self.player.rect.y = 0

        if self.player.rect.left < 0:
            self.player.rect.left = 0
        if self.player.rect.right > config.SCREEN_WIDTH:
            self.player.rect.right = config.SCREEN_WIDTH

        for enemy in self.level.enemy_list:
            for sprite in self.level.object_list:
                if enemy.collide(sprite):
                    if enemy.rect.y < sprite.rect.y:
                        if (enemy.rect.bottom - sprite.rect.top) < 10 and enemy.direction.y > 0:
                            enemy.direction.y = 0
                            enemy.rect.y = sprite.rect.y - sprite.rect.height / 2 - enemy.height / 2

                    elif enemy.rect.y > sprite.rect.y:
                        if (enemy.rect.top - sprite.rect.bottom) < 10 and enemy.direction.y < 0:
                            enemy.direction.y = 0
                            enemy.rect.y = sprite.rect.y + sprite.rect.height / 2 + enemy.height / 2 + 1

        for sprite in self.level.object_list:
            if self.player.collide(sprite):
                # check if player not above sprite or below sprite
                if sprite.rect.y - 5 > self.player.rect.y - self.player.height / 2 > sprite.rect.y - sprite.rect.height:
                    if self.player.rect.x < sprite.rect.x - sprite.rect.width / 2 and self.player.direction.x > 0:
                        self.player.rect.x = sprite.rect.x - sprite.rect.width / 2 - self.player.width / 2
                        self.player.direction.x = 0
                    elif self.player.rect.x > sprite.rect.x - sprite.rect.width / 2 and self.player.direction.x < 0:
                        self.player.rect.x = sprite.rect.x + sprite.rect.width / 2 + self.player.width / 2
                        self.player.direction.x = 0

                if self.player.rect.y < sprite.rect.y:
                    if (self.player.rect.bottom - sprite.rect.top) < 10 and self.player.direction.y > 0:
                        self.player.direction.y = 0
                        self.player.rect.y = sprite.rect.y - sprite.rect.height / 2 - self.player.height / 2

                elif self.player.rect.y > sprite.rect.y:
                    if (self.player.rect.top - sprite.rect.bottom) < 10 and self.player.direction.y < 0:
                        self.player.direction.y = 0
                        self.player.rect.y = sprite.rect.y + sprite.rect.height / 2 + self.player.height / 2 + 1

    def draw(self):
        self.game_screen.blit(config.image_background_transformed, (0, 0))
        for line in range(0, 16):
            vertical_line = pygame.draw.line(self.game_screen, config.WHITE,
                                             (0, line * config.quadrant_size),
                                             (config.SCREEN_WIDTH, line * config.quadrant_size))

            horizontal_line = pygame.draw.line(self.game_screen, config.WHITE,
                                               (line * config.quadrant_size, 0),
                                               (line * config.quadrant_size, config.SCREEN_HEIGHT))

        self.level.draw()
        self.player.draw(self.game_screen)

    def game_loop(self):
        while self.run:
            self.input()

            self.game_screen.fill("BLACK")
            self.process()
            self.draw()
            self.player.update()
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)


game = Game()
game.game_loop()
