import pygame as pg
from constantes import Const
from Functions.image_loader import ImageLoader

class Attribute(pg.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Store():
    def __init__(self):
        self.const = Const()
        self.loader = ImageLoader()
        self.product_1_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Store\Product_1.png', self.const.attribute_width, self.const.attribute_height)
        self.product_2_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Store\Product_2.png', self.const.attribute_width, self.const.attribute_height)

    def run(self, launcher):
        self.products = pg.sprite.Group()
        self.products.add(Attribute(self.product_1_image, self.const.screen_width / 2 - self.const.attribute_width / 2, self.const.screen_height / 2 - self.const.attribute_height / 2))
        self.products.add(Attribute(self.product_2_image, self.const.screen_width / 2 - self.const.attribute_width / 2, self.const.screen_height / 2 - self.const.attribute_height / 2))
        running = True
        self.const.SCREEN.fill((0, 0, 0))
        self.const.SCREEN.blit(launcher.game.background, (0, 0))
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        launcher.run()
                        running = False

            self.draw()
            pg.display.flip()


    def draw(self):
        self.products.draw(self.const.SCREEN)