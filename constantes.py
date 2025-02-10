import os, pygame as pg
class Const():
    def __init__(self):
        # Affichage
        self.SCREEN = pg.display.set_mode((0, 0), pg.FULLSCREEN)
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
        # Squelette
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

        # Vitesses
        self.update_opps_frames = 5
        self.skeleton_velocity = 3
        self.scrolling_velocity = 1
        self.running_car_velocity = 6
        self.car_start_px_from_player = 300
        self.speed = 10

        # Autres
        self.lanes = 3
        self.chemin_repertoire = os.path.dirname(os.path.abspath(__file__))
        self.lane_positions = [self.screen_width / 4, self.screen_width/4*2, self.screen_width/4*3]
        self.draw_heart_position = self.screen_width - 50 - (self.heart_width * 3 + self.heart_offset * 3)
        self.blinking_interval = 30
        self.blinking_iterations = 3
        self.opponents = ["skeleton", "running_car", "broken_car"]