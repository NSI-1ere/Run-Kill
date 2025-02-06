from constantes import Const
from Functions.image_loader import ImageLoader
import pygame, random

class BrokenCar(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.const = Const()
        self.loader = ImageLoader()
        self.image = self.loader.load_image(self.const.chemin_repertoire + r'.\Sprites\Car\Broken_car.png', self.const.broken_car_width, self.const.broken_car_height)
        self.rect = self.image.get_rect()
        self.elems_on_screen = []  # Compteur d'update des coords des elems sur l'ecran
        self.rect.y = player.broken_car_y
        self.rect.x = player.broken_car_x

    def move(self):
        self.rect.y += self.const.scrolling_velocity

    def remove(self):
        self.kill()