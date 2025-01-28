import os, pygame as pg
class Const():
    def __init__(self):
        self.SCREEN = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.CLOCK = pg.time.Clock()
        self.FPS = 60
        self.screen_width, self.screen_height = pg.display.get_surface().get_size()
        self.player_width = 110
        self.player_height = 110
        self.speed = 10
        self.lanes = 3
        self.lane_width = (self.screen_width / 20) * 2
        self.chemin_repertoire = os.path.dirname(os.path.abspath(__file__))
        self.lane_positions = [(self.screen_width / 20) * 4.5 + self.player_width/2 - self.lane_width/4 , (self.screen_width / 20) * 9.5 + self.player_width/2 - self.lane_width/4, (self.screen_width / 20) * 14.5 + self.player_width/2 - self.lane_width/4]