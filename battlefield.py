from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.robot = Robot("VX13", Weapon("Sword", 25))
        self.dinosaur = Dinosaur("Shaq", 25)
    

    def run_game(self):
        self.display_welcome()
        self.battle_phase()


    def display_welcome(self):
        print("Welcome to Fight Island! Enjoy the show!")

    def battle_phase(self):
        while True:
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)
            elif self.dinosaur.health <= 0:
                self.winner()
                break
            elif self.robot.health <= 0:
                self.winner()
                break

    def winner(self):
        if self.dinosaur.health <= 0:
            print(f"{self.dinosaur.name} health has been crushed. {self.robot.name} is victorious!")
        elif self.robot.health <= 0:
            print(f"{self.robot.name} health has been destroyed. {self.dinosaur.name} is victorious!")
