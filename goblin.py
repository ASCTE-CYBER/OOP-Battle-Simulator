import random
from enemy import Enemy

class Goblin(Enemy):


    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.health = 50
        self.attack_power = random.randint(5, 15)
