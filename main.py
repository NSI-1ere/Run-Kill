import pygame
from launcher import Launcher

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    launcher = Launcher()
    launcher.run()