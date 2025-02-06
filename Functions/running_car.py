from constantes import Const
from Functions.image_loader import ImageLoader
import pygame

class RunningCar(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.const = Const()
        self.loader = ImageLoader()
        self.image = self.loader.load_image(self.const.chemin_repertoire + r'.\Sprites\Car\Car.png', self.const.running_car_width, self.const.running_car_height)
        self.rect = self.image.get_rect()
        self.elems_on_screen = []
        self.update_counter = self.const.update_opps_frames  # Compteur d'update des coords des elems sur l'ecran
        self.rect.y = player.running_car_y
        self.rect.x = player.running_car_x

    def move(self, running):
        if running == True:
            self.rect.y += self.const.running_car_velocity
        else:
            self.rect.y += self.const.scrolling_velocity

    def remove(self):
        self.kill()