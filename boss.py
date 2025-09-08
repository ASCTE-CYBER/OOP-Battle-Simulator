import random
from enemy import Enemy

class Giant(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = random.randint(100,150)
        self.attack_power = random.randint(10, 20)


    def take_damage(self, damage):
        self.health -= damage
        if self.health<0:
            self.health=0