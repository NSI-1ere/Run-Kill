from constantes import Const

class Opponents(type):
    def __init__(self):
        self.const = Const()
        self.chemin_repertoire = self.const.chemin_repertoire
        self.zombie_x = 0

    def move(self):
        if type == "zombie":
            pass
        if type == "car":
            pass
        if type == "truck":
            pass

    def zombie(self):
        self.zombie_x = self.zombie_x - self.const.speed