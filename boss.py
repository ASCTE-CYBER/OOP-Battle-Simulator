import random
from enemy import Jim

class Kenny_Clark(Jim):
   
    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.attack_power = random.randint(15, 40)

    def special_attack(self):
        sattack = random.randint(0,100)
        if sattack == 65:
            return self.attack_power * 2
        else:
            return self.attack_power
            
