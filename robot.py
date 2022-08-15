from weapon import Weapon
from dinosaur import Dinosaur
class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.weapon = weapon

    def attack(self, dinosaur):
        self.dinosaur = dinosaur
        while self.dinosaur.health >= 0:
            self.dinosaur.health -= self.weapon.attack_power
            print(self.dinosaur.health) 