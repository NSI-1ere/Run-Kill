import sys, os, subprocess, pygame as pg
from constantes import Const
from player import Player
from zombie import Zombie
from map import Map

class Game():
    def __init__(self):
        self.const = Const()
        self.player = Player()
        self.map = Map()
        self.is_running = False
        self.running = True
        self.clock = self.const.CLOCK
        self.chemin_repertoire = self.const.chemin_repertoire
        self.scale_factor = self.const.screen_width / (self.map.tile_width * 20)

        # Redimensionner l'image de l'arrière-plan aux dimensions de l'écran
        self.background = pg.image.load(self.chemin_repertoire + r".\Backgrounds\8-bit roads.jpg") 
        self.resized_background = pg.transform.scale(self.background, (self.const.screen_width, self.const.screen_height))

    def run(self):
        pg.key.set_repeat()
        self.is_running = True
        while self.running:
            # Gestion des événements
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False

            # Mise à jour
            keys = pg.key.get_pressed()
            self.player.update(keys)

            # Dessiner la carte et le fond
            self.map.draw_map(self.const.SCREEN, self.map.tmx_data, self.scale_factor)


            # Dessiner le joueur
            self.player.draw()

            # Rafraîchissement
            pg.display.flip()
            self.const.CLOCK.tick(self.const.FPS)

        pg.quit()
        sys.exit()
