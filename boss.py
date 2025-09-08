import random
from enemy import Enemy

class MINIPEKKA(Enemy):
    """
    This is our boss blueprint
    """
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 30
        self.health = 250

    def attack(self):
        if self.health < 200:
            self.attack_power = 12
        elif self.health < 150:
            self.attack_power = 25
        elif self.health < 100:
            self.attack_power = 72
        elif self.health < 50:
            self.attack_power = 85
        return self.attack_power


