from enemy import Enemy
import random

class Goggles(Enemy):

    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.attack_power = random.randint (10, 25)

    def heal(self):
        chance = random.randint(1,6)
        if chance == 1:
            self.health == self.health + 25
        