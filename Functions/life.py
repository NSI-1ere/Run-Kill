from constantes import Const
from Functions.image_loader import ImageLoader
import pygame

class Life(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.const = Const()
        self.loader = ImageLoader()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
