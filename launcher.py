from game import Game
from Functions.store import Store
from constantes import Const
import pygame, math

class Launcher():
    def __init__(self):
        self.game = Game()
        self.const = Const()
        self.store = Store()
        self.running = True

        # Creer les différents composants de la fenêtre
        # Icône
        self.banner = pygame.image.load(self.game.const.chemin_repertoire + r"\Assets\Banner\Banner.png").convert_alpha()
        self.banner = pygame.transform.scale(self.banner, (self.banner.get_width()/2, self.banner.get_height()/2))
        self.baner_rect = self.banner.get_rect()
        self.baner_rect.x = math.ceil(self.const.screen_width / 2 - self.baner_rect.width / 2)
        self.baner_rect.y = math.ceil(self.const.screen_height / 3.5 - self.baner_rect.height / 2)

        # Bouton Play
        self.play_button = pygame.image.load(self.game.const.chemin_repertoire + r"\Assets\Banner\Play.png").convert_alpha()
        self.play_button = pygame.transform.scale(self.play_button, (self.const.button_width, self.const.button_height))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = math.ceil(self.const.screen_width / 2 - self.play_button_rect.width / 2)
        self.play_button_rect.y = math.ceil(self.const.screen_height / 2 - self.play_button_rect.height / 2)

        # Bouton Stroe
        self.store_button = pygame.image.load(self.game.const.chemin_repertoire + r"\Assets\Banner\Store.png").convert_alpha()
        self.store_button = pygame.transform.scale(self.store_button, (self.const.store_button_width, self.const.store_button_height))
        self.store_button_rect = self.store_button.get_rect()
        self.store_button_rect.x = math.ceil(self.const.screen_width - 50 - self.store_button_rect.width)
        self.store_button_rect.y = math.ceil(self.const.screen_height - 50 - self.store_button_rect.height)

        pygame.mixer.init()
        pygame.mixer.music.load(self.const.chemin_repertoire + r'.\Assets\Soundtrack\LauncherLoop.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def run(self):
        pygame.key.set_repeat()
        self.const.SCREEN.fill((255, 0, 0))
        self.const.SCREEN.blit(self.game.background, (0, 0))
        self.const.SCREEN.blit(self.play_button, self.play_button_rect)
        self.const.SCREEN.blit(self.banner, self.baner_rect)
        self.const.SCREEN.blit(self.store_button, self.store_button_rect)
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
                    if self.store_button_rect.collidepoint(event.pos):
                        self.store.run(self)
                        self.running = False
            if self.running == False:
                pygame.mixer.music.stop()
            
            # Rafraîchissement
            pygame.display.flip()
            self.const.CLOCK.tick(self.const.FPS)