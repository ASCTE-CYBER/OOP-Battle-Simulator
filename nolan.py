import random
from boss import Boss

class Nolan(Boss):

    def __init__(self, name, color):
        super().__init__(name)
        self.attack_power = 45
        self.color = color
        print(f"Nolan {self.name} of color {self.color} has entered the battle!")


    def attack(self):
        if self.health < 200:
            self.attack_power = 55
        elif self.health < 150:
            self.attack_power = 60
        elif self.health < 100:
            self.attack_power = 65
        elif self.health < 45:
            self.attack_power = 75
        return self.attack_power


   
        
        # TODO We should prevent the goblins health from going into the NEGATIVE
        self.health = max(0, self.health)
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")