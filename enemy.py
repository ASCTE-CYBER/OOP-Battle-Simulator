import random

class Enemy:
    '''
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    '''
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = random.randint(5, 15)

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        turnG=True
        while self.health>=0 and turnG==True:
            self.health -= damage
            print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
            turnG=False

    def is_alive(self):
        return self.health > 0