import pygame
from constantes import Const

class Attack(pygame.sprite.Sprite):
    def init(self):
        super().__init__()
        self.const = Const()
        self.velocity = 5
        self.image = pygame.image.load(self.const.chemin_repertoire + r'\Sprites\Attack.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()