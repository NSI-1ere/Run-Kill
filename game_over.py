import pygame
from constantes import Const
from map import Map

class GameOver():
    def __init__(self):
        self.const = Const()
        self.map = Map()
        self.font = pygame.font.Font(None, 160)
        self.text = self.font.render("Game Over", True, (255, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.const.screen_width // 2, self.const.screen_height // 2)
        self.is_game_over = False

    def run(self, game, launcher):
        self.is_game_over = True
        self.const.SCREEN.fill((0, 0, 0))
        self.map.draw_map(self.const.SCREEN, self.map.tmx_data, self.const.screen_width / (self.map.tile_width * 20))
        self.const.SCREEN.blit(self.text, self.text_rect)
        while self.is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_game_over = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        launcher.run()
                        self.is_game_over = False
                    if event.key == pygame.K_RETURN:
                        self.is_game_over = False
                        game.run(launcher)
            pygame.display.flip()
            self.const.CLOCK.tick(self.const.FPS)
                        
