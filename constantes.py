import pygame as pg
class Const():
    def __init__(self):
        self.SCREEN = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.CLOCK = pg.time.Clock()
        self.FPS = 60
        self.screen_width, self.screen_height = pg.display.get_surface().get_size()
        self.player_width = 70
        self.player_height = 70
        self.speed = 10
        self.lanes = 3
        self.lane_width = 200