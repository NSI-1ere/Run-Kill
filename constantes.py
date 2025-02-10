import os, pygame as pg
from Functions.csv_manager import CSVManager

class Const():
    def __init__(self):
        self.csv_manager = CSVManager()
        # Affichage
        self.SCREEN = pg.display.set_mode((0, 0), pg.FULLSCREEN, pg.DOUBLEBUF | pg.HWSURFACE)
        self.CLOCK = pg.time.Clock()
        self.FPS = 60
        self.screen_width, self.screen_height = pg.display.get_surface().get_size()

        # Tailles
        # Joueur
        self.player_width = 110
        self.player_height = 110
        # Coeurs
        self.heart_width = 50
        self.broken_heart_width = 56
        self.heart_height = 50
        self.heart_offset = 30
        self.heart_y = 50
        # Experience
        self.skull_height = 83
        self.skull_width = 55
        self.skull_y = 50
        self.skull_x = 50
        #Squelette
        self.skeleton_width = 67
        self.skeleton_height = 120
        # Voitures
        self.running_car_width = 110
        self.running_car_height = 196
        self.broken_car_width = 110
        self.broken_car_height = 196
        # Launcher
        self.button_width = 265
        self.button_height = 150
        self.attack_width = 30
        self.attack_height = 30
        self.store_button_width, self.store_button_height = 200, 200
        # Shop
        self.attribute_width, self.attribute_height = 100, 100
        self.buy_button_width, self.buy_button_height = 100, 32
        self.shop_text_offset_y = 50
        self.shop_offers_offset_x = 100

        # Vitesses
        self.update_opps_frames = 5
        self.skeleton_velocity = 4
        self.scrolling_velocity = 2
        self.running_car_velocity = 8
        self.car_start_px_from_player = 600
        self.speed = 10

        # Autres
        self.lanes = 3
        self.chemin_repertoire = os.path.dirname(os.path.abspath(__file__))
        self.lane_positions = [self.screen_width / 4, self.screen_width/4*2, self.screen_width/4*3]
        self.draw_heart_position = self.screen_width - 50 - (self.heart_width * 3 + self.heart_offset * 3)
        self.blinking_interval = 30
        self.blinking_iterations = 3
        self.opponents = ["skeleton", "running_car", "broken_car"]

        # Chemins d'image
        self.skin_1 = self.chemin_repertoire + r'.\Assets\Player\Basic Skin.png'
        self.skin_2 = self.chemin_repertoire + r'.\Assets\Player\Advanced Skin.png'
        self.map_1 = self.chemin_repertoire + r'.\Backgrounds\Map.png'
        self.map_2 = self.chemin_repertoire + r'.\Backgrounds\Map_2.png'
        self.railgun = self.chemin_repertoire + r'.\Assets\Weapons\Railgun.png'
        self.products = ["Product_1", "Product_2", "Product_3"]
 
        self.railgun_stat = False
        self.skin = self.skin_1
        self.map = self.map_1

    def update_inventory(self):
        xp, inventory = self.csv_manager.fetch_save_file()
        for i in range(len(inventory)):
            if inventory[i] == "Product_1":
                self.skin = self.skin_2
            if inventory[i] == "Product_2":
                self.map = self.map_2
            if inventory[i] == "Product_3":
                self.railgun_stat = True
        
            