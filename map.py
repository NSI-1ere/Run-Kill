import pygame, pytmx
from pytmx import load_pygame
from constantes import Const

class Map():
    def __init__(self):
        self.const = Const()
        self.chemin_repertoire = self.const.chemin_repertoire
        self.tmx_data = load_pygame(self.chemin_repertoire + r"\Backgrounds\Map.tmx")  # Assurez-vous que le fichier existe
        self.tile_width = self.tmx_data.tilewidth
        self.tile_height = self.tmx_data.tileheight

    def draw_map(self, surface, tmx_data, scale_factor):
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        # Redimensionner la tuile
                        scaled_tile = pygame.transform.scale(
                            tile, 
                            (int(self.tile_width * scale_factor), int(self.tile_height * scale_factor))
                        )
                        # Calculer la position redimensionnée
                        surface.blit(scaled_tile, 
                                    (x * self.tile_width * scale_factor, y * self.tile_height * scale_factor))