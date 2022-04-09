import config
import pygame
from objectGame import ObjectGame
from objectMobile import ObjectMobile


class Block(ObjectGame):
    def __init__(self):
        super().__init__(config.image_square)

