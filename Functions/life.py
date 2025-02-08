from constantes import Const
from Functions.image_loader import ImageLoader
import pygame

class LifeSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Life():
    def __init__(self, player):
        self.const = Const()
        self.loader = ImageLoader()

        player.all_hearts.empty()

        draw_pos = self.const.screen_width - 50 - (self.const.heart_width * 3 + self.const.heart_offset * 3)
        full_heart_count = player.hp_counter
        broken_heart_count = 3 - player.hp_counter

        full_heart_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Sprites\Life\Heart.png', self.const.heart_width, self.const.heart_height)
        broken_heart_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Sprites\Life\BrokenHeart.png', self.const.broken_heart_width, self.const.heart_height)

        for _ in range(full_heart_count):
            heart = LifeSprite(full_heart_image, draw_pos, self.const.heart_y)
            player.all_hearts.add(heart)
            draw_pos += self.const.heart_width + self.const.heart_offset

        for _ in range(broken_heart_count):
            broken_heart = LifeSprite(broken_heart_image, draw_pos, self.const.heart_y)
            player.all_hearts.add(broken_heart)
            draw_pos += self.const.heart_width + self.const.heart_offset
