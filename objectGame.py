import math
import config
import pygame


class ObjectGame(pygame.sprite.Sprite):
    def collide(self, object_game):
    
        collision_x =(math.fabs(self.rect.x - object_game.rect.x) * 2) < (self.width + object_game.width)
        collision_y =((math.fabs(self.rect.y - object_game.rect.y) * 2) < (self.height + object_game.height))

        return(collision_x and collision_y)


    
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

        #test 
        if self.rect.bottom > config.SCREEN_HEIGHT:
            self.rect.bottom = config.SCREEN_HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > config.SCREEN_WIDTH:
            self.rect.right = config.SCREEN_WIDTH

        