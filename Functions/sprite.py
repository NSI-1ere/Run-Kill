import pygame
from constantes import Const
from Functions.image_loader import ImageLoader

# Classe Joueur
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.const = Const()

        self.loader = ImageLoader()
        self.chemin_repertoire = self.const.chemin_repertoire

        # Charger toutes les images du joueur
        self.spritesheet = self.loader.load_image(self.const.skin,96, 774)
        self.image_1 = self.get_image(0,0)
        self.image_2 = self.get_image(0,129)
        self.image_3 = self.get_image(0,258)
        self.image_4 = self.get_image(0,387)
        self.image_5 = self.get_image(0,516)
        self.image_6 = self.get_image(0,645)
        self.image_1.set_colorkey((0,0,0))
        self.image_2.set_colorkey((0,0,0))
        self.image_3.set_colorkey((0,0,0))
        self.image_4.set_colorkey((0,0,0))
        self.image_5.set_colorkey((0,0,0))
        self.image_6.set_colorkey((0,0,0))
        # Charger une image pour le joueur
        self.image = self.image_1
        self.image.set_colorkey((0,0,0))
        self.next_frame = 0
        # Obtenir le rectangle de l'image
        self.rect = self.image.get_rect()

    def set_center(self, player_x, player_y):
        # Initialiser la position du joueur
        self.rect.center = (player_x, player_y)

    def get_image(self, x, y):
        image = pygame.Surface([95,129])
        image.blit(self.spritesheet, (0, 0), (x, y, 95, 129))
        return image

    def active_sprite(self, touches, player_x, player_y):
        # Déplacement basé sur les touches pressées
        self.rect.y = player_y
        self.rect.x = player_x
        if self.next_frame == 5:
            if self.image == self.image_1:
                self.image = self.image_3
                self.next_frame = 0
            elif self.image == self.image_2:
                self.image = self.image_3
                self.next_frame = 0
            elif self.image == self.image_3:
                self.image = self.image_4
                self.next_frame = 0
            elif self.image == self.image_4:
                self.image = self.image_5
                self.next_frame = 0
            elif self.image == self.image_5:
                self.image = self.image_6
                self.next_frame = 0
            elif self.image == self.image_6:
                self.image = self.image_3
                self.next_frame = 0
        else:
            self.next_frame += 1
        

        if touches[pygame.K_a] or touches[pygame.K_SPACE]:
            self.image = self.image_2
            self.next_frame = 5

        """if touches[pygame.K_LEFT]:
            if self.image_path != self.image_left:
                self.image_path = self.image_left
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (width, height))
        if touches[pygame.K_RIGHT]:
            if self.image_path != self.image_right:
                self.image_path = self.image_right
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (width, height))"""