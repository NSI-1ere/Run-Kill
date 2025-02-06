import pygame

class ImageLoader():
    def __init__(self):
        self.image_cache = {}

    def load_image(self, key, width, height):
        if not key in self.image_cache:
            self.image_cache[key] = pygame.transform.scale(pygame.image.load(key).convert_alpha(), (width, height))
        return self.image_cache[key]