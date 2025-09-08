
import random
from enemy import enemy

class brute(enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 500
        self.attack_power = 20

    def smash(self):
        if self.health < 50:
            self.health = 80 
        elif self.attack_power < 150:
            self.health = 50
        elif self.health < 300:
            self.attack_power = 40
        elif self.health < 400:
            self.attack_power = 20  
        return self.attack_power 