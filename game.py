from platform import platform
import pygame
import config
from level import Level
from plataform import Plataform
from player import Player
from enemy import Enemy



class Game:
    
    def __init__(self):
        pygame.init()
        self.game_screen = pygame.display.set_mode((config.SCREEN_WIDTH,config.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.player = Player(175, 300)
        self.enemy = Enemy(300, 500)
        self.level = Level(self.game_screen, config.map_data)
        
    
    def input(self):
        keys  = pygame.key.get_pressed()

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
        self.level.setup_level(config.map_data)

        for object in self.level.object_list:
            if self.player.collide(object):
                if self.player.rect.y < object.rect.y:
                    if (self.player.rect.bottom - object.rect.top) < 10 and self.player.direction.y > 0 :
                        self.player.direction.y = 0
                        self.player.rect.bottom = object.rect.top
                elif self.player.rect.y > object.rect.y:
                    if (self.player.rect.top - object.rect.bottom) < 10 and self.player.direction.y < 0 :
                            self.player.direction.y = 0
                            self.player.rect.top = object.rect.bottom

                    
                




                        
               

    def draw(self):
        self.player.draw(self.game_screen)

        for line in range(0, 16):
            vertical_line = pygame.draw.line(self.game_screen, config.WHITE, 
            (0 , line * config.quadrant_size), 
            (config.SCREEN_WIDTH, line * config.quadrant_size))

            horizontal_line = pygame.draw.line(self.game_screen, config.WHITE, 
            (line * config.quadrant_size, 0), 
            (line * config.quadrant_size, config.SCREEN_HEIGHT))

        self.level.draw()

    def game_loop(self):
        while self.run:
            self.clock.tick(60)
            self.input()
            
               
            self.game_screen.fill("BLACK")
            
            self.draw()
            self.player.update()
            self.process()
            pygame.display.update()


game = Game()
game.game_loop()