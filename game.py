import sys, os, subprocess, pygame as pg
from constantes import Const
from Functions.player import Player
from Functions.game_over import GameOver
from Functions.image_loader import ImageLoader

class Game():
    def __init__(self):
        self.const = Const()
        self.player = Player()
        self.game_over = GameOver()
        self.loader = ImageLoader()
        self.is_running = False
        self.running = True
        self.clock = self.const.CLOCK
        self.chemin_repertoire = self.const.chemin_repertoire
        self.scale_factor = self.const.screen_width / (16 * 20)
        self.map_y = 0
        self.map_2_y = 0 - self.const.screen_height
        self.const.update_inventory()
        # Redimensionner l'image de l'arrière-plan aux dimensions de l'écran
        self.background = self.loader.load_image(self.const.map, self.const.screen_width, self.const.screen_height)

    def new_game(self):
        self.background = self.loader.load_image(self.const.map, self.const.screen_width, self.const.screen_height)
        # Groupes de sprites
        self.all_projectiles = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_opponents = pg.sprite.Group()
        self.all_sprites.add(self.player.sprites)
        # Coordonées de chargement de l'arrière-plan
        self.map_y = 0
        self.map_2_y = 0 - self.const.screen_height

    def scrolling(self):
        self.const.SCREEN.fill((0, 0, 0))
        self.const.SCREEN.blit(self.background, (0, self.map_y))
        self.map_y += self.const.scrolling_velocity
        self.const.SCREEN.blit(self.background, (0, self.map_2_y))
        self.map_2_y += self.const.scrolling_velocity
        if self.map_y >= self.const.screen_height:
            self.map_y = 0 - self.const.screen_height
        if self.map_2_y >= self.const.screen_height:
            self.map_2_y = 0 - self.const.screen_height

    def run(self, launcher):
        self.new_game()
        pg.display.set_caption("Run&Kill")
        Icon = pg.image.load(self.const.chemin_repertoire + r'/Assets/Banner/Icon.png')
        pg.display.set_icon(Icon)
        pg.key.set_repeat()
        self.player.new_game()
        self.is_running = True
        while self.running:
            # Gestion des événements
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        launcher.run()
                        self.running = False

            # Mise à jour
            keys = pg.key.get_pressed()
            self.player.update(keys, self, launcher)

            # Dessiner l'arrière-plan
            self.scrolling()
            # Dessiner le joueur
            self.player.draw()

            # Rafraîchissement
            pg.display.flip()
            self.const.CLOCK.tick(self.const.FPS)
            self.is_running = not self.game_over.is_game_over

        pg.quit()
        sys.exit()
