import pygame
from constantes import Const

class Attack(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.const = Const()
        self.velocity = 5
        self.image = pygame.image.load(self.const.chemin_repertoire + r'\Assets\Attack\Attack.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = player.x + 25
        self.rect.y = player.y

    def remove(self):
        self.kill()

    def move(self):
        self.rect.y -= self.velocity