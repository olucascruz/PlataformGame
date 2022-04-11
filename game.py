import pygame
import config
from level import Level
from player import Player


class Game:

    def __init__(self):
        pygame.init()
        self.game_screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.player = Player(375, 0)
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.level = Level()
        self.main_menu = True
        self.reset = False
        self.start = config.image_start
        self.start_react = self.start.get_rect()

    def input(self):
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if 517 > mouse_pos[0] > 383 and \
                270 > mouse_pos[1] > 170:
            if pygame.mouse.get_pressed()[0]:
                self.main_menu = False

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
                if event.key == pygame.K_f:
                    if not self.player.is_attack:
                        self.player.attack(True)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    if self.player.is_attack:
                        self.player.attack(False)

    def process(self):
        # win
        if len(self.level.enemy_list) < 1:
            self.main_menu = True

        # reset game
        if not self.player_group:
            self.level.object_list.empty()
            self.level.enemy_list.empty()
            self.level.map_data = config.map_data
            self.level.setup_level()
            self.player.rect.x = config.SCREEN_WIDTH // 2 - 75
            self.player.rect.y = 0
            self.player_group.add(self.player)
            self.player.life = 3

        self.level.update()

        # check collision with limit screen
        if self.player.rect.bottom > config.SCREEN_HEIGHT:
            self.player.rect.x = config.SCREEN_WIDTH / 2
            self.player.rect.y = 0
            self.player.life -= 1

        if self.player.rect.left < 0:
            self.player.rect.left = 0

        if self.player.rect.right > config.SCREEN_WIDTH:
            self.player.rect.right = config.SCREEN_WIDTH

        for enemy in self.level.enemy_list:
            if enemy.rect.bottom > config.SCREEN_HEIGHT:
                enemy.rect.x = config.SCREEN_WIDTH / 2
                enemy.rect.y = 0

            if enemy.rect.left < 0:
                enemy.rect.left = 0
                enemy.reverse()

            if enemy.rect.right > config.SCREEN_WIDTH:
                enemy.rect.right = config.SCREEN_WIDTH
                enemy.reverse()

            # logic player attack
            if self.player.is_attack:
                if self.player.current_direction == "right":
                    if -75 < enemy.rect.left - self.player.rect.right < 40 and \
                            enemy.rect.top == self.player.rect.top:
                        enemy.kill()
                else:
                    if -75 < enemy.rect.right - self.player.rect.left < 40 and \
                            enemy.rect.top == self.player.rect.top:
                        enemy.kill()

            # effect collision with enemy
            if enemy.collide(self.player) and enemy.rect.top - self.player.rect.top < 10:
                self.player.life -= 1
                self.player.move("jump")
                if self.player.current_direction == 'left':
                    self.player.current_direction = 'right'
                    self.player.rect.x += 40
                if self.player.current_direction == 'right':
                    self.player.rect.x -= 40

            # collision enemy with boxes
            for sprite in self.level.object_list:
                if enemy.collide(sprite):
                    if -75 < enemy.rect.left - sprite.rect.right < 40 and \
                            enemy.rect.top == sprite.rect.top:
                        enemy.reverse()
                    if -75 < enemy.rect.right - sprite.rect.left < 40 and \
                            enemy.rect.top == sprite.rect.top:
                        enemy.reverse()

                    if enemy.rect.y < sprite.rect.y:
                        if (enemy.rect.bottom - sprite.rect.top) < 10 and enemy.direction.y > 0:
                            enemy.direction.y = 0
                            enemy.rect.y = sprite.rect.y - sprite.rect.height / 2 - enemy.height / 2

                    elif enemy.rect.y > sprite.rect.y:
                        if (enemy.rect.top - sprite.rect.bottom) < 10 and enemy.direction.y < 0:
                            enemy.direction.y = 0
                            enemy.rect.y = sprite.rect.y + sprite.rect.height / 2 + enemy.height / 2 + 1

        # logic collision player with boxes
        for sprite in self.level.object_list:
            if self.player.collide(sprite):
                # check if player not above sprite or below sprite
                if sprite.rect.y - 10 > self.player.rect.y \
                        - self.player.height / 2 > sprite.rect.y - sprite.rect.height:

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

                # logic player dead
                if self.player.life < 1:
                    self.player.kill()

    def draw(self):
        if self.main_menu:
            start_scale = pygame.transform.scale(self.start, (config.quadrant_size * 2, config.quadrant_size * 2))
            self.start_react = start_scale.get_rect()
            self.game_screen.blit(start_scale, (config.SCREEN_WIDTH // 2 - 75, config.SCREEN_HEIGHT // 2 - 150))
        else:
            if self.player.life > 0:
                num = self.player.life
            else:
                num = 1
            heart = pygame.image.load(f'img/heart_{num}.png')
            heart = pygame.transform.scale(heart, (config.quadrant_size * 2, config.quadrant_size / 2))
            self.game_screen.blit(config.image_background_transformed, (0, 0))
            self.level.object_list.draw(self.game_screen)
            self.level.enemy_list.draw(self.game_screen)
            self.player_group.draw(self.game_screen)
            if self.player_group:
                self.game_screen.blit(heart, (config.SCREEN_WIDTH // 2 - 75, 5))

    def game_loop(self):
        while self.run:
            self.input()
            self.game_screen.fill("BLACK")
            self.process()
            self.draw()
            self.level.enemy_list.update()
            self.player.update()
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)
