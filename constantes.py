import os, pygame as pg
class Const():
    def __init__(self):
        self.SCREEN = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.CLOCK = pg.time.Clock()
        self.FPS = 60
        self.screen_width, self.screen_height = pg.display.get_surface().get_size()
        self.player_width = 110
        self.player_height = 110
        self.opponents = ["skeleton", "running_car", "broken_car"]
        self.heart_width = 50
        self.broken_heart_width = 56
        self.heart_height = 50
        self.heart_offset = 30
        self.heart_y = 50
        self.skeleton_width = 67
        self.skeleton_height = 120
        self.running_car_width = 110
        self.running_car_height = 196
        self.broken_car_width = 110
        self.broken_car_height = 196
        self.button_width = 400
        self.button_height = 150
        self.update_opps_frames = 5
        self.skeleton_velocity = 3
        self.scrolling_velocity = 1
        self.running_car_velocity = 6
        self.car_start_px_from_player = 300
        self.speed = 10
        self.lanes = 3
        self.chemin_repertoire = os.path.dirname(os.path.abspath(__file__))
        self.lane_positions = [self.screen_width / 4, self.screen_width/4*2, self.screen_width/4*3]
        self.draw_heart_position = self.screen_width - 50 - (self.heart_width * 3 + self.heart_offset * 3)
        self.attribute_width, self.attribute_height = 100, 100
        self.store_button_width, self.store_button_height = 200, 200
        self.blinking_interval = 30
        self.blinking_iterations = 3
        self.buy_button_width, self.buy_button_height = 100, 32