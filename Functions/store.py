import pygame as pg
import time
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
        self.costs = [20, 50, 100]
        self.product_rect_list = [self.product_1_image.get_rect(), self.product_2_image.get_rect(), self.product_3_image.get_rect()]
        self.attribute_pos_x = 50
        self.button_x, self.button_y = 50, 150
        self.font_size = 50
        self.font = pg.font.Font(self.const.chemin_repertoire + r".\Assets\Fonts\PixelOperator8.ttf", self.font_size)
        self.messages = []

        text_surface_already_inv = self.font.render("Already in inventory.", True, (255, 0, 0))
        text_surface_bought = self.font.render("Bought.", True, (255, 0, 0))
        text_surface_bought_reload = self.font.render("Bought. Please reload the game to apply changes.", True, (255, 0, 0))
        text_surface_not_enough_xp = self.font.render("Not enough XP.", True, (255, 0, 0))

        self.text_size_already_inv = text_surface_already_inv.get_width()
        self.text_size_bought = text_surface_bought.get_width()
        self.text_size_bought_reload = text_surface_bought_reload.get_width()
        self.text_size_not_enough_xp = text_surface_not_enough_xp.get_width()

    def run(self, launcher):
        self.button_x, self.button_y = 50, 150
        self.products = pg.sprite.Group()
        self.products.add(Attribute(self.product_1_image, self.attribute_pos_x, 50))
        self.attribute_pos_x += 100 + self.const.shop_offers_offset_x
        self.products.add(Attribute(self.product_2_image, self.attribute_pos_x, 50))
        self.attribute_pos_x += 100 + self.const.shop_offers_offset_x
        self.products.add(Attribute(self.product_3_image, self.attribute_pos_x, 50))
        self.attribute_pos_x = 50
        self.rect_list = []
        
        for _ in self.products:
            button = Attribute(self.button_image, self.button_x, self.button_y)
            self.products.add(button)
            self.rect_list.append(button.rect)
            self.button_x += 100 + self.const.shop_offers_offset_x
        
        running = True
        self.const.SCREEN.fill((0, 0, 0))
        self.const.SCREEN.blit(launcher.game.background, (0, 0))
        pg.mixer.init()
        pg.mixer.music.load(self.const.chemin_repertoire + r'.\Assets\Soundtrack\ShopLoop.mp3')
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play(-1)

        while running:
            current_time = time.time()
            self.messages = [msg for msg in self.messages if current_time - msg[2] < 2]
            self.const.SCREEN.fill((0, 0, 0))
            self.const.SCREEN.blit(launcher.game.background, (0, 0))
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.mixer.music.stop()
                        launcher.run()
                        running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    for idx, rect in enumerate(self.rect_list[:]):
                        if rect.collidepoint(event.pos):
                            xp, inventory = self.csv_manager.fetch_save_file()
                            product_name = f'Product_{idx + 1}'
                            
                            if product_name in inventory:
                                self.messages.append(("Already in inventory.", (self.const.screen_width//2 - self.text_size_already_inv//2, self.const.screen_height//2 + self.font_size//2), time.time()))
                            elif xp >= self.costs[idx]:
                                self.record_purchase(idx, self.costs[idx])
                            else:
                                self.messages.append(("Not enough XP.", (self.const.screen_width//2 - self.text_size_not_enough_xp//2, self.const.screen_height//2 + self.font_size//2), time.time()))
            
                if not running:
                    pg.mixer.music.stop()
            
            self.draw()
            pg.display.flip()

    def record_purchase(self, product_index, cost):
        product_name = f'Product_{product_index + 1}'
        xp, inventory = self.csv_manager.fetch_save_file()

        if product_name not in inventory and xp >= cost:
            xp -= cost
            print(str(xp))
            inventory.append(product_name)
            self.csv_manager.update_save_file(new_xp=xp, new_inventory=inventory)
            self.const.update_inventory()
            if product_name == "Product_2":
                message = ("Bought. Please reload the game to apply changes.", (self.const.screen_width//2 - self.text_size_bought_reload//2, self.const.screen_height//2 + self.font_size//2), time.time())
            else: 
                message = ("Bought.", (self.const.screen_width//2 - self.text_size_bought//2, self.const.screen_height//2 + self.font_size//2), time.time())
        else:
            message = ("Already in inventory.", (self.const.screen_width//2 - self.text_size_already_inv//2, self.const.screen_height//2 + self.font_size//2), time.time())

        self.messages.append(message)

    def draw(self):
        self.products.draw(self.const.SCREEN)
        for msg, pos, _ in self.messages:
            text_surface = self.font.render(msg, True, (255, 0, 0))
            self.const.SCREEN.blit(text_surface, pos)
