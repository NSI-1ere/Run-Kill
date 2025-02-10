import pygame as pg
from Functions.csv_manager import CSVManager
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
        self.csv_manager = CSVManager()
        self.button_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Store\Buy_Button.png', self.const.buy_button_width, self.const.buy_button_height)
        self.button_image_rect = self.button_image.get_rect()
        self.product_1_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Store\Product_1.png', self.const.attribute_width, self.const.attribute_height)
        self.product_2_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Store\Product_2.png', self.const.attribute_width, self.const.attribute_height)
        self.product_3_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Store\Product_3.png', self.const.attribute_width, self.const.attribute_height)
        self.proct_1_cost = 20
        self.proct_2_cost = 50
        self.proct_3_cost = 100
        self.costs = [self.proct_1_cost, self.proct_2_cost, self.proct_3_cost]
        self.product_1_image_rect = self.product_1_image.get_rect()
        self.product_2_image_rect = self.product_2_image.get_rect()
        self.product_3_image_rect = self.product_3_image.get_rect()
        self.product_rect_list = [self.product_1_image_rect, self.product_2_image_rect, self.product_3_image_rect]
        self.button_x, self.button_y = 50, 150
        self.font = pg.font.Font(self.const.chemin_repertoire + r".\Assets\Fonts\PixelOperator8.ttf", 40)

    def run(self, launcher):
        self.button_x, self.button_y = 50, 150
        self.products = pg.sprite.Group()
        self.products.add(Attribute(self.product_1_image, 50, 50))
        self.products.add(Attribute(self.product_2_image, 150, 50))
        self.products.add(Attribute(self.product_3_image, 250, 50))
        self.rect_list = []
        for i in self.products:
            button = Attribute(self.button_image, self.button_x, self.button_y)
            self.products.add(button)
            self.rect_list.append(button.rect)
            self.button_x += 100
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
                            if f'Product_{self.rect_list.index(i) + 1}' in self.csv_manager.fetch_save_file()[1]:
                                self.const.SCREEN.blit(self.font.render("Already in inventory",True,(255,0,0)), (i.x, i.y))
                            else:
                                self.record_purchase(self.rect_list.index(i), self.costs[self.rect_list.index(i)], i)
                            self.rect_list.remove(i)
                        
                if running == False:
                    pg.mixer.music.stop()

            self.draw()
            pg.display.flip()   

    def record_purchase(self, product_index, cost, i):
        product_name = f'Product_{product_index + 1}'
        xp, inventory = self.csv_manager.fetch_save_file()
        
        if product_name not in inventory and xp >= cost:
            print(cost)
            xp -=cost
            print(xp)
            inventory.append(product_name)
            self.csv_manager.update_save_file(new_xp=xp, new_inventory=inventory)
            self.const.update_inventory()
            self.const.SCREEN.blit(self.font.render("Bought.",True,(255,0,0)), (i.x, i.y + self.const.shop_text_offset_y))
        elif xp < cost:
            self.const.SCREEN.blit(self.font.render("Not enough XP.",True,(255,0,0)), (i.x, i.y + self.const.shop_text_offset_y))

    def draw(self):
        self.products.draw(self.const.SCREEN)