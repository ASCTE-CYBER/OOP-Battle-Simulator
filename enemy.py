import random

class Enemy:
    """
    This is our enemy blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = random.randint(17, 25)

    def attack(self):
        return random.randint(6, self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0
