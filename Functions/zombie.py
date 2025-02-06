from constantes import Const
from Functions.image_loader import ImageLoader
import pygame

class Zombie(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.const = Const()
        self.loader = ImageLoader()
        self.image = self.loader.load_image(self.const.chemin_repertoire + r'.\Sprites\Zombie\Zombie.png', self.const.zombie_width, self.const.zombie_height)
        self.rect = self.image.get_rect()
        self.elems_on_screen = []
        self.update_counter = self.const.update_opps_frames  # Compteur d'update des coords des elems sur l'ecran
        self.rect.y = player.zombie_y
        self.rect.x = player.zombie_x

    def move(self):
        self.rect.y += self.const.zombie_velocity

    def remove(self):
        self.kill()