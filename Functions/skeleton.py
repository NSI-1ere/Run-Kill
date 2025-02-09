from constantes import Const
from Functions.image_loader import ImageLoader
import pygame

class Skeleton(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.const = Const()
        self.loader = ImageLoader()
        self.elems_on_screen = []
        self.update_counter = self.const.update_opps_frames  # Compteur d'update des coords des elems sur l'ecran

        # Charger toutes les images du skelette
        self.next_frame = 5
        self.image_1 = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Skeleton\Standing.png', self.const.skeleton_width, self.const.skeleton_height)
        self.image_2 = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Skeleton\Running 1.png', self.const.skeleton_width, self.const.skeleton_height)
        self.image_3 = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Skeleton\Running 2.png', self.const.skeleton_width, self.const.skeleton_height)
        
        #Obtenir le rectangle de l'image
        self.image = self.image_1
        self.rect = self.image.get_rect()
        self.rect.y = player.skeleton_y
        self.rect.x = player.skeleton_x

    def move(self):
        self.rect.y += self.const.skeleton_velocity
        if self.next_frame == 5:
            if self.image == self.image_1:
                self.image = self.image_2
            elif self.image == self.image_2:
                self.image = self.image_3
            else:
                self.image = self.image_2
            self.next_frame = 0
        else:
            self.next_frame += 1

    def remove(self):
        self.kill()