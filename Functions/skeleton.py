from constantes import Const
from Functions.image_loader import ImageLoader
import pygame

class Skeleton(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.const = Const()
        self.loader = ImageLoader()
        self.image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Skeleton\Standing.png', self.const.skeleton_width, self.const.skeleton_height)
        self.rect = self.image.get_rect()
        self.elems_on_screen = []
        self.update_counter = self.const.update_opps_frames  # Compteur d'update des coords des elems sur l'ecran
        self.rect.y = player.skeleton_y
        self.rect.x = player.skeleton_x

    def move(self):
        self.rect.y += self.const.skeleton_velocity

    def remove(self):
        self.kill()