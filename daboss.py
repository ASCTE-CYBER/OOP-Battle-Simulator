import random
from enemy import Enemy

class Principal(Enemy):


    def __init__(self, name):
        super().__init__(name)
        self.health = 150
        self.attack_power = random.randint(20, 25)

    def attack(self):
        if self.health < 50:
            self.attack_power = 35
        elif self.health < 100:
            self.attack_power = 30
        return self.attack_power
