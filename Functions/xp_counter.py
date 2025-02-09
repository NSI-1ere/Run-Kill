import pygame
from constantes import Const
from Functions.image_loader import ImageLoader

class XPCounter(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.const = Const()
        self.loader = ImageLoader()
        self.font = pygame.font.Font(self.const.chemin_repertoire + r'.\Assets\Fonts\PixelOperator-Bold.ttf', 50)
        self.player = player

        self.image = pygame.Surface((self.const.skull_width + 50, self.const.skull_height), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))

        skull_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Skeleton\Skull.png', self.const.skull_width, self.const.skull_height)
        self.image.blit(skull_image, (0, 0))

        xp_text = self.font.render(f"{self.player.xp_counter}", True, (255, 0, 0))

        text_x = self.const.skull_width + 10
        text_y = (self.const.skull_height - xp_text.get_height()) // 2

        self.image.blit(xp_text, (text_x, text_y))

        self.rect = self.image.get_rect()
        self.rect.x = self.const.skull_x
        self.rect.y = self.const.skull_y
