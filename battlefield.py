from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.robot = Robot("VX13", Weapon("Sword", 25))
        self.dinosaur = Dinosaur("Shaq", 25)
    

    def run_game(self):
        while True:
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)
            elif self.dinosaur.health <= 0:
                print("The dinosaur's health has reached zero. The robot has won this battle!")
            elif self.robot.health <= 0:
                print("The robot's health has reached zero. The dinosaur has won this battle!")

        #need to call the attack functions
        #need the robot and dinosaur to alternate attacks
        #need ot print out the attack weapon, damage done, health remaining after each attack
        #need to display who won after health reaches 0
        pass 


    def display_welcome(self):
        print("Welcome to Fight Island! Enjoy the Show!")

    def battle(self):
        pass

    def winner(self):
        print("The winner is:")

