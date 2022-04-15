import pygame
import config
from level import Level
from player import Player
from enemy import Enemy
from block import Block


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

        # reset game
        if not self.player_group:
            self.level.object_list.empty()
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

        # logic player dead
        if self.player.life < 1:
            self.player.kill()

        if not self.main_menu:
            self.level.update()
            self.player.update()

            for sprite in self.level.object_list:
                if type(sprite) == Block:
                    block = sprite

                    # check collision
                    if self.player.collide(block):

                        # checks if the player is neither above nor below
                        if block.rect.top < self.player.rect.centery < block.rect.bottom:

                            # checks if the player collided from the right
                            if block.rect.centerx > self.player.rect.right >= block.rect.left - 10:
                                self.player.rect.right = block.rect.left
                                self.player.direction.x = 0

                            # checks if the player collided from the left
                            elif block.rect.centerx < self.player.rect.left <= block.rect.right + 10:
                                self.player.rect.left = block.rect.right
                                self.player.direction.x = 0

                        # checks if the player collided from above
                        if block.rect.centery > self.player.rect.bottom >= block.rect.top and \
                                self.player.rect.right - 10 > block.rect.left and \
                                self.player.rect.left + 10 < block.rect.right:  # consider the smaller player
                            self.player.rect.bottom = block.rect.top
                            if self.player.direction.y > 0:
                                self.player.direction.y = 0

                        # checks if the player collided from below
                        if block.rect.centery < self.player.rect.top <= block.rect.bottom:
                            self.player.rect.top = block.rect.bottom
                            if self.player.direction.y < 0:
                                self.player.direction.y = 0

                if type(sprite) == Enemy:
                    enemy = sprite
                    enemy.update()

                    if self.player.collide(enemy):
                        self.player.move('jump')
                        self.player.life -= 1
                        if self.player.current_direction == "right":
                            self.player.rect.x -= 10
                        if self.player.current_direction == "left":
                            self.player.rect.x += 10

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

                    for sprite_2 in self.level.object_list:
                        if type(sprite_2) == Block:
                            block = sprite_2
                            if enemy.collide(block):
                                # checks if the enemy is neither above nor below
                                if block.rect.top < enemy.rect.centery < block.rect.bottom:

                                    # checks if the enemy collided from the right
                                    if block.rect.centerx > enemy.rect.right >= block.rect.left - 10:
                                        enemy.rect.right = block.rect.left
                                        enemy.reverse()

                                    # checks if the enemy collided from the left
                                    elif block.rect.centerx < enemy.rect.left <= block.rect.right + 10:
                                        enemy.rect.left = block.rect.right
                                        enemy.reverse()

                                # checks if the enemy collided from above
                                if block.rect.centery > enemy.rect.bottom >= block.rect.top:
                                    enemy.rect.bottom = block.rect.top
                                    if enemy.direction.y > 0:
                                        enemy.direction.y = 0

                                # checks if the enemy crashed from below
                                if block.rect.centery < enemy.rect.top <= block.rect.bottom:
                                    enemy.rect.top = block.rect.bottom
                                    if enemy.direction.y < 0:
                                        enemy.direction.y = 0

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
            self.player_group.draw(self.game_screen)
            if self.player_group:
                self.game_screen.blit(heart, (config.SCREEN_WIDTH // 2 - 75, 5))

    def game_loop(self):
        while self.run:
            self.input()
            self.game_screen.fill("BLACK")
            self.process()
            self.draw()
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)
