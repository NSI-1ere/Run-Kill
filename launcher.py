from game import Game
from constantes import Const
import pygame, math

class Launcher():
    def __init__(self):
        self.game = Game()
        self.const = Const()
        self.banner = pygame.image.load(self.game.const.chemin_repertoire + r"\Sprites\Banner\Banner.png").convert_alpha()
        self.banner = pygame.transform.scale(self.banner, (self.banner.get_width()/2, self.banner.get_height()/2))
        self.baner_rect = self.banner.get_rect()
        self.baner_rect.x = math.ceil(self.const.screen_width / 2 - self.baner_rect.width / 2)
        self.baner_rect.y = math.ceil(self.const.screen_height / 3.5 - self.baner_rect.height / 2)
        self.running = True

        self.play_button = pygame.image.load(self.game.const.chemin_repertoire + r"\Sprites\Banner\Play.png").convert_alpha()
        self.play_button = pygame.transform.scale(self.play_button, (self.const.button_width, self.const.button_height))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = math.ceil(self.const.screen_width / 2 - self.play_button_rect.width / 2)
        self.play_button_rect.y = math.ceil(self.const.screen_height / 2 - self.play_button_rect.height / 2)

    def run(self):
        print(self.banner.get_width(), self.banner.get_height())
        pygame.key.set_repeat()
        self.const.SCREEN.fill((255, 0, 0))
        self.const.SCREEN.blit(self.game.resized_background, (0, 0))
        self.const.SCREEN.blit(self.play_button, self.play_button_rect)
        self.const.SCREEN.blit(self.banner, self.baner_rect)
        while self.running:

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        self.game.run(self)
                        self.running = False
            
            # Rafraîchissement
            pygame.display.flip()
            self.const.CLOCK.tick(self.const.FPS)