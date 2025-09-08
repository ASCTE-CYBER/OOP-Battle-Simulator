import random
from enemy import enemy 

class Giant(enemy):
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 67
        self.health = 1000

def attack(self):
    if self.health < 300:
        self.attack_power = 35
    elif self.health < 200:
        self.attack_power = 45
    elif self.health < 150:
        self.attack_power = 65
    elif self.health < 100:
        self.attack_power = 75
    return self.attack_power
        


        
    

