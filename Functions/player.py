import random, pygame as pg
from constantes import Const
from Functions.sprite import Sprite
from Functions.life import Life
from Functions.attack import Attack
from Functions.skeleton import Skeleton
from Functions.running_car import RunningCar
from Functions.broken_car import BrokenCar
from Functions.game_over import GameOver
from Functions.image_loader import ImageLoader
from Functions.xp_counter import XPCounter
from Functions.csv_manager import CSVManager

class Player():
    def __init__(self):
        self.const = Const()
        self.sprites = Sprite()
        self.game_over = GameOver()
        self.loader = ImageLoader()
        self.csv_manager = CSVManager()
        self.x = self.const.lane_positions[1] - self.const.player_width/2
        self.y = self.const.screen_height / 5 * 4
        self.height = self.const.player_height
        self.width = self.const.player_width
        self.speed = self.const.speed
        self.current_lane = 2
        self.lane_positions = self.const.lane_positions
        self.key_counter = 0
        self.last_action_time = pg.time.get_ticks()
        self.skeleton_x = self.const.screen_width / 2
        self.skeleton_y = 0
        self.item_generation_counter = 10
        self.running_car_x = self.const.screen_width / 2
        self.running_car_y = 0
        self.broken_car_x = self.const.screen_width / 2
        self.broken_car_y = 0
        self.hp_counter = 3
        self.blinking_interval = 0
        self.blinking_iterations = 0
        self.last_generated_opponent = None
        self.last_generated_opponent_lane = None
        self.inventory = []

        if self.csv_manager.fetch_save_file() == (0, []):
            self.csv_manager.write_save_file(0, [])
        
        self.xp_counter = self.csv_manager.fetch_save_file()[0]

        # Groupes de sprites (facilitent le rendu et les collisions)
        self.all_projectiles = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_opponents = pg.sprite.Group()
        self.all_hearts = pg.sprite.Group()
        self.all_xp = pg.sprite.Group()
        self.all_sprites.add(self.sprites)

        # Gérer la vie
        self.heart_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Life\Heart.png', self.const.heart_width, self.const.heart_height)
        self.broken_heart_image = self.loader.load_image(self.const.chemin_repertoire + r'.\Assets\Life\BrokenHeart.png', self.const.broken_heart_width, self.const.heart_height)
        self.previous_hp = self.hp_counter

        self.previous_xp_counter = self.xp_counter

    def new_game(self):
        self.all_projectiles = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_opponents = pg.sprite.Group()
        self.all_sprites.add(self.sprites)
        self.all_hearts = pg.sprite.Group()
        self.all_xp = pg.sprite.Group()
        self.x = self.const.lane_positions[1] - self.const.player_width/2
        self.hp_counter = 3
        self.previous_hp = self.hp_counter
        self.previous_xp_counter = self.xp_counter
        self.update_hearts()
        self.update_xp_count()

        # Music

        pg.mixer.init()
        pg.mixer.music.load(self.const.chemin_repertoire + r'.\Assets\Soundtrack\MainLoop.mp3')
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play(-1)

        self.hit_sound = pg.mixer.Sound(self.const.chemin_repertoire + r'.\Assets\Soundtrack\DamageSound.mp3')
        self.attack_hit_sound = pg.mixer.Sound(self.const.chemin_repertoire + r'.\Assets\Soundtrack\AttackSound.mp3')
        self.gun_firing_sound = pg.mixer.Sound(self.const.chemin_repertoire + r'.\Assets\Soundtrack\GunFiringSound.mp3')


    def handle_input(self):
        self.actual_time = pg.time.get_ticks()
        keys = pg.key.get_pressed()
        if self.key_counter > 0:
            self.key_counter -= 1
            return
        if keys[pg.K_LEFT] or keys[pg.K_q]:
            if self.current_lane >= 2:
                self.current_lane -= 1
                self.x = self.lane_positions[self.current_lane - 1] - self.const.player_width/2
                self.key_counter = 10
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            if self.current_lane <= self.const.lanes - 1:
                self.current_lane += 1
                self.x = self.lane_positions[self.current_lane - 1] - self.const.player_width/2
                self.key_counter = 10
        if keys[pg.K_SPACE] or keys[pg.K_z]:
            if self.actual_time - self.last_action_time >= 250:
                self.last_action_time = self.actual_time
                self.all_projectiles.add(Attack(self))
                self.gun_firing_sound.play().set_volume(0.3)

    def gen_opponents(self):
        if self.item_generation_counter > 0:
            self.item_generation_counter -= 1

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

            if what_to_gen == "skeleton":
                self.skeleton_x = lane_to_use - self.const.skeleton_width/2
                self.all_opponents.add(Skeleton(self))
            elif what_to_gen == "running_car":
                self.running_car_x = lane_to_use - self.const.running_car_width/2
                self.all_opponents.add(RunningCar(self))
            elif what_to_gen == "broken_car":
                self.broken_car_x = lane_to_use - self.const.broken_car_width/2
                self.all_opponents.add(BrokenCar(self))

            self.item_generation_counter = 350

    def check_collision(self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)

    def update(self, keys, game, launcher):
        self.handle_input()
        self.sprites.active_sprite(keys, self.x, self.y)
        self.gen_opponents()

        for each in self.all_projectiles:
            each.move()
            if each.rect.y < self.const.screen_height / 2:
                self.all_projectiles.remove(each)
            if self.check_collision(each, self.all_opponents):
                for opponent in self.all_opponents:
                    if isinstance(opponent, Skeleton):
                        if self.check_collision(opponent, self.all_projectiles):
                            self.all_opponents.remove(opponent)
                            self.attack_hit_sound.play().set_volume(0.5)
                            self.xp_counter += 1
                self.all_projectiles.remove(each)

        for each in self.all_opponents:
            if isinstance(each, RunningCar):
                isCarRunning = each.rect.y > self.y - self.const.car_start_px_from_player and self.x == each.rect.x
                each.move(isCarRunning)
            else:
                each.move()

            if self.check_collision(each, self.all_sprites) and self.blinking_iterations <= 0:
                self.all_opponents.remove(each)
                self.hp_counter -= 1
                self.blinking_interval = self.const.blinking_interval
                self.blinking_iterations = self.const.blinking_iterations
                self.hit_sound.play().set_volume(0.5)
                if self.hp_counter <= 0:
                    pg.mixer.music.stop()
                    self.game_over.run(game, launcher)
                
        if self.hp_counter != self.previous_hp:
            self.update_hearts()

        if self.xp_counter != self.previous_xp_counter:
            self.update_xp_count()


    def update_hearts(self):
        self.all_hearts.empty()
        self.draw_pos = self.const.draw_heart_position
        for _ in range(self.hp_counter):
            self.all_hearts.add(Life(self.heart_image, self.draw_pos, self.const.heart_y))
            self.draw_pos += self.const.heart_width + self.const.heart_offset
        for _ in range(3 - self.hp_counter):
            self.all_hearts.add(Life(self.broken_heart_image, self.draw_pos, self.const.heart_y))
            self.draw_pos += self.const.heart_width + self.const.heart_offset
        self.previous_hp = self.hp_counter

    def update_xp_count(self):
        self.csv_manager.update_save_file(self.xp_counter)
        self.all_xp.empty()
        self.all_xp.add(XPCounter(self))
        self.previous_xp_counter = self.xp_counter


    def draw(self):
        if self.blinking_iterations > 0:
            if self.blinking_interval >= 0:
                self.all_sprites.draw(self.const.SCREEN)
            elif self.blinking_interval <= -self.const.blinking_interval:
                self.blinking_interval = self.const.blinking_interval
                self.blinking_iterations -= 1
            self.blinking_interval -= 1
        
        if self.blinking_iterations <= 0:
            self.all_sprites.draw(self.const.SCREEN)
        
        self.all_xp.draw(self.const.SCREEN)
        self.all_projectiles.draw(self.const.SCREEN)
        self.all_opponents.draw(self.const.SCREEN)
        self.all_hearts.draw(self.const.SCREEN)
