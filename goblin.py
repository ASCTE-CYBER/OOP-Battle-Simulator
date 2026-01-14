import random
from enemy import Enemy
class Goblin(Enemy):
    """
    This is our goblin blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack_power = random.randint(2, 10)

    def attack(self):
        return random.randint(1, 10)
