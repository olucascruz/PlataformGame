import pygame
from objectMobile import ObjectMobile 

class Player(ObjectMobile):
    def __init__(self, x, y):
        self.image = pygame.image.load("img/enemy.png")
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = x
        self.rect.y = y
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        