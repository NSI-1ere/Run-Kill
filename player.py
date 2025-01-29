import random, pygame as pg
from constantes import Const
from sprite import Sprite
from attack import Attack
from zombie import Zombie

class Player():
    def __init__(self):
        self.const = Const()
        self.sprites = Sprite()
        self.x = self.const.lane_positions[1]
        self.y = self.const.screen_height/5*4
        self.height = self.const.player_height
        self.width = self.const.player_width
        self.speed = self.const.speed
        self.current_lane = round(self.const.lanes/2)
        self.lane_positions = self.const.lane_positions
        self.key_counter = 0
        self.last_action_time = pg.time.get_ticks()
        self.zombie_x = self.const.screen_width/2
        self.zombie_y = 0
        self.zombie_key_counter = 10

        # Groupe de sprites (facilite le rendu et les collisions)
        self.all_projectiles = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_opponents = pg.sprite.Group()
        self.all_sprites.add(self.sprites)
    
    def handle_input(self):
        self.actual_time = pg.time.get_ticks()
        keys = pg.key.get_pressed()
        if self.key_counter > 0:
            self.key_counter -= 1
            return
        # Déplacements horizontaux
        if keys[pg.K_LEFT] or keys[pg.K_q]:
            if self.current_lane >= 2:
                self.current_lane -= 1
                self.x = self.lane_positions[self.current_lane-1]
                self.key_counter = 10
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            if self.current_lane <= self.const.lanes-1:
                self.current_lane += 1
                self.x = self.lane_positions[self.current_lane-1]
                self.key_counter = 10
        if keys[pg.K_SPACE] or keys[pg.K_z]:
            if self.actual_time - self.last_action_time >= 250:
                self.last_action_time = self.actual_time
                self.all_projectiles.add(Attack(self))

    def gen_opponents(self):
        if self.zombie_key_counter > 0:
            self.zombie_key_counter -= 1
        if self.zombie_key_counter == 0:
            self.zombie_x = self.const.lane_positions[random.randint(0, 2)]
            self.all_opponents.add(Zombie(self))
            self.zombie_key_counter = 100

    def check_collision(self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)

    def update(self, keys):
        self.handle_input()
        self.sprites.active_sprite(keys, self.x, self.y, self.width, self.height)
        self.gen_opponents()
        for each in self.all_projectiles:
            each.move()
            if each.rect.y < self.const.screen_height/2:
                self.all_projectiles.remove(each)
            if self.check_collision(each, self.all_opponents):
                for opponent in self.all_opponents:
                    if self.check_collision(opponent, self.all_projectiles):
                        self.all_opponents.remove(opponent)
                self.all_projectiles.remove(each)
        for each in self.all_opponents:
            each.move()
            if each.rect.y > self.const.screen_height:
                self.all_opponents.remove(each)
        

    def draw(self):
        self.all_sprites.draw(self.const.SCREEN)
        self.all_projectiles.draw(self.const.SCREEN)
        self.all_opponents.draw(self.const.SCREEN)