from weapon import Weapon
from dinosaur import Dinosaur
class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.weapon = weapon

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{dinosaur.name} has been hit! Its remaining health is: {dinosaur.health}.")