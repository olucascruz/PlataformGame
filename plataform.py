import config
from objectGame import ObjectGame


class Block(ObjectGame):
    def __init__(self):
        super().__init__(config.image_square)
