import pygame as pg
import csv
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
        self.button_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Store\Buy_Button.png', self.const.buy_button_width, self.const.buy_button_height)
        self.button_image_rect = self.button_image.get_rect()
        self.product_1_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Store\Product_1.png', self.const.attribute_width, self.const.attribute_height)
        self.product_2_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Store\Product_2.png', self.const.attribute_width, self.const.attribute_height)
        self.button_x, self.button_y = 50, 150
        self.font = pg.font.Font(None, 160)

    def run(self, launcher):
        self.button_x, self.button_y = 50, 150
        self.products = pg.sprite.Group()
        self.products.add(Attribute(self.product_1_image, 50, 50))
        self.products.add(Attribute(self.product_2_image, 150, 50))
        self.rect_list = []
        for i in self.products:
            button = Attribute(self.button_image, self.button_x, self.button_y)
            self.products.add(button)
            self.rect_list.append(button.rect)
            self.button_x += 100
            print(self.rect_list)
        running = True
        self.const.SCREEN.fill((0, 0, 0))
        self.const.SCREEN.blit(launcher.game.background, (0, 0))
        pg.mixer.init()
        pg.mixer.music.load(self.const.chemin_repertoire + r'.\Assets\Soundtrack\ShopLoop.mp3')
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play(-1)

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.mixer.music.stop()
                        launcher.run()
                        running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in self.rect_list:
                        if i.collidepoint(event.pos):
                            self.const.SCREEN.blit(self.font.render("Bought",True,(0,0,0)), (i.x, i.y))
                            self.record_purchase(self.rect_list.index(i))
                            self.rect_list.remove(i)
                        
                if running == False:
                    pg.mixer.music.stop()

            self.draw()
            pg.display.flip()   

    def record_purchase(self, product_index):
        product_name = f'Product_{product_index + 1}'
        purchases = {}

        # Lire le fichier CSV existant et charger les données dans un dictionnaire
        try:
            with open('purchases.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        purchases[row[0]] = int(row[1])
        except FileNotFoundError:
            # Si le fichier n'existe pas, ignorer cette étape
            pass

        # Mettre à jour ou ajouter l'achat
        if product_name in purchases:
            purchases[product_name] += 1
        else:
            purchases[product_name] = 1

        # Écrire les données mises à jour dans le fichier CSV
        with open('purchases.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for product, count in purchases.items():
                writer.writerow([product, count])

    def draw(self):
        self.products.draw(self.const.SCREEN)