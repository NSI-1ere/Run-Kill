import pygame as pg
from constantes import Const
from sprite import Sprite
from attack import Attack

class Player():
    def __init__(self):
        self.const = Const()
        self.sprites = Sprite()
        self.projectiles = Attack()
        self.x = self.const.screen_width/2
        self.y = self.const.screen_height/5*4
        self.height = self.const.player_height
        self.width = self.const.player_width
        self.speed = self.const.speed
        self.current_lane = round(self.const.lanes/2)
        self.lane_positions = self.const.lane_positions
        self.key_counter = 0


        # Groupe de sprites (facilite le rendu et les collisions)
        self.all_projectiles = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.sprites)
    
    def handle_input(self):
        keys = pg.key.get_pressed()
        if self.key_counter > 0:
            self.key_counter -= 1
            return
        # Déplacements horizontaux
        if keys[pg.K_LEFT]:
            if self.current_lane >= 2:
                self.current_lane -= 1
                self.x = self.lane_positions[self.current_lane-1]
                self.key_counter = 10
        if keys[pg.K_RIGHT]:
            if self.current_lane <= self.const.lanes-1:
                self.current_lane += 1
                self.x = self.lane_positions[self.current_lane-1]
                self.key_counter = 10
        if keys[pg.K_SPACE]:
            self.all_projectiles.add(self.projectiles)

    def update(self, keys):
        self.handle_input()
        self.sprites.active_sprite(keys, self.x, self.y, self.width, self.height)

    def draw(self):
        self.all_sprites.draw(self.const.SCREEN)
        self.all_projectiles.draw(self.const.SCREEN)