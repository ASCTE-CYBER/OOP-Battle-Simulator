import random
from enemy import enemy

class wizard(enemy):

    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 50
        self.health = 200

    def attack(self):
        if self.health < 100:
            self.attack_power = 30
        elif self.health < 50:
            self.attack_power = 15
        return self.attack_power