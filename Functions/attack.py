import pygame
from constantes import Const

class Attack(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.const = Const()
        self.velocity = 5
        self.image = pygame.image.load(self.const.chemin_repertoire + r'\Assets\Attack\Attack.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.const.attack_width, self.const.attack_height))
        self.rect = self.image.get_rect()
        self.rect.x = self.const.lane_positions[player.current_lane-1] - self.const.attack_width/2
        self.rect.y = player.y

    def remove(self):
        self.kill()

    def move(self):
        self.rect.y -= self.velocity