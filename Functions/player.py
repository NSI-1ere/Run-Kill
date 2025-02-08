import random, pygame as pg
from constantes import Const
from Functions.sprite import Sprite
from Functions.attack import Attack
from Functions.zombie import Zombie
from Functions.running_car import RunningCar
from Functions.broken_car import BrokenCar
from Functions.game_over import GameOver

class Player():
    def __init__(self):
        self.const = Const()
        self.sprites = Sprite()
        self.game_over = GameOver()
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
        self.item_generation_counter = 10
        self.running_car_x = self.const.screen_width/2
        self.running_car_y = 0
        self.broken_car_x = self.const.screen_width/2
        self.broken_car_y = 0
        self.last_generated_opponent = None
        self.last_generated_opponent_lane = None

        # Groupe de sprites (facilite le rendu et les collisions)
        self.all_projectiles = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_opponents = pg.sprite.Group()
        self.all_sprites.add(self.sprites)

    def new_game(self):
        self.all_projectiles = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_opponents = pg.sprite.Group()
        self.all_sprites.add(self.sprites)
        self.x = self.const.lane_positions[1]
    
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
        if self.item_generation_counter > 0:
            self.item_generation_counter -= 1

        what_to_gen = None
        
        generated_something = False
        if self.item_generation_counter == 0:
            opponents = self.const.opponents[:]
            if self.last_generated_opponent:
                opponents.remove(self.last_generated_opponent)

            lanes = self.const.lane_positions[:]
            if self.last_generated_opponent_lane:
                lanes.remove(self.last_generated_opponent_lane)

            what_to_gen = random.choice(opponents)
            lane_to_use = random.choice(lanes)
            self.last_generated_opponent = what_to_gen
            self.last_generated_opponent_lane = lane_to_use

        if what_to_gen == "zombie":
            self.zombie_x = lane_to_use
            self.all_opponents.add(Zombie(self))
            generated_something = True

        if what_to_gen == "running_car":
            self.running_car_x = lane_to_use
            self.all_opponents.add(RunningCar(self))
            generated_something = True

        if what_to_gen == "broken_car":
            self.broken_car_x = lane_to_use
            self.all_opponents.add(BrokenCar(self))
            generated_something = True
        
        if generated_something:
            self.item_generation_counter = 150


    def check_collision(self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)

    def update(self, keys, game, launcher):
        self.handle_input()
        self.sprites.active_sprite(keys, self.x, self.y, self.width, self.height)
        self.gen_opponents()
    
        for each in self.all_projectiles:
            each.move()
            if each.rect.y < self.const.screen_height / 2:
                self.all_projectiles.remove(each)
            if self.check_collision(each, self.all_opponents):
                for opponent in self.all_opponents:
                    if isinstance(opponent, Zombie):
                        if self.check_collision(opponent, self.all_projectiles):
                            self.all_opponents.remove(opponent)
                self.all_projectiles.remove(each)
    
        for each in self.all_opponents:
            if isinstance(each, RunningCar):
                isCarRunning = each.rect.y > self.y - self.const.car_start_px_from_player and self.x == each.rect.x
                each.move(isCarRunning)
            else:
                each.move()
        
            if self.check_collision(each, self.all_sprites):
                self.all_opponents.remove(each)
                self.game_over.run(game, launcher)

        

    def draw(self):
        self.all_sprites.draw(self.const.SCREEN)
        self.all_projectiles.draw(self.const.SCREEN)
        self.all_opponents.draw(self.const.SCREEN)
