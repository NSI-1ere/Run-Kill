from constantes import Const
import pygame, random

class Opponents():
    def __init__(self):
        self.const = Const()
        self.chemin_repertoire = self.const.chemin_repertoire
        self.zombie_velocity = 5
        self.zombie_sprite = self.chemin_repertoire + r'.\Sprites\Zombie\Zombie.png'
        self.gen_counter_zombie = 7 * 60
        self.gen_counter_car = 5 * 60
        self.gen_counter_train = 10 * 60
        self.elems_on_screen = []
        self.update_counter = self.const.update_opps_frames  # Compteur d'update des coords des elems sur l'ecran

    def handle(self): 
        if self.gen_counter_zombie <= 0:
            self.generate("zombie")
            self.gen_counter_zombie = random.randint(5 * 60, 10 * 60)  # Reset spawn timer
        else:
            self.gen_counter_zombie -= 1

        self.update()  # Update enemy positions
        return self.elems_on_screen  # Return elements for rendering


    def update(self):
        """Move zombies downward every 10 frames & remove if off-screen"""
        self.update_counter -= 1
        if self.update_counter > 0:  
            return
        else:
            self.update_counter = self.const.update_opps_frames

        # Suppression des zombies hors écran
        self.elems_on_screen = [
            elem for elem in self.elems_on_screen if elem[2].y < self.const.screen_height
        ]

        # Update de la pos y des autres zombies
        for elem in self.elems_on_screen:
            match elem[0]:
                case "zombie":
                    elem[2].y += self.zombie_velocity 

    def generate(self, obj_type):
        spawn_lane = random.randint(1, self.const.lanes)
        spawn_coords = self.const.lane_positions[spawn_lane - 1]

        match obj_type:
            case "zombie":
                zombie_image = pygame.transform.scale(
                    pygame.image.load(self.zombie_sprite).convert_alpha(), 
                    (self.const.zombie_width, self.const.zombie_height)
                )
                zombie_rect = zombie_image.get_rect()
                zombie_rect.y = -100
                zombie_rect.x = spawn_coords

                # Stockage des données liées au zombie généré.
                self.elems_on_screen.append(["zombie", zombie_image, zombie_rect])
