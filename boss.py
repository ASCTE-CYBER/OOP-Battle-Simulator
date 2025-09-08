import random
from enemy import Enemy

class False_Knight(Enemy):
    
    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack_power = random.randint(20, 35)

    def attack(self):
        return random.randint(15, self.attack_power + 5)