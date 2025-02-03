from constantes import Const
import pygame, random

class RunningCar(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.const = Const()
        self.image = pygame.image.load(self.const.chemin_repertoire + r'.\Sprites\Car\Car.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.const.zombie_width, self.const.zombie_height))
        self.rect = self.image.get_rect()
        self.elems_on_screen = []
        self.update_counter = self.const.update_opps_frames  # Compteur d'update des coords des elems sur l'ecran
        self.rect.y = player.running_car_y
        self.rect.x = player.running_car_x

    def move(self, running):
        if running == True:
            self.rect.y += self.const.running_car_velocity
        else:
            self.rect.y += self.const.car_velocity

    def remove(self):
        self.kill()