import math
import config
import pygame


class ObjectGame(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.transform.scale(img, (config.quadrant_size, config.quadrant_size))
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def collide(self, object_game):
    
        collision_x = (math.fabs(self.rect.x - object_game.rect.x) * 2) < (self.width + object_game.width)
        collision_y = ((math.fabs(self.rect.y - object_game.rect.y) * 2) < (self.height + object_game.height))

        return collision_x and collision_y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
