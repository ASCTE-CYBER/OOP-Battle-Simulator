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
        self.health = 75
        self.attack_power = random.randint(10, 20)

    def attack(self):
        return random.randint(10, self.attack_power)
        


    def take_damage(self, damage):
        self.health -= damage
        # TODO We should prevent the goblins health from going into the NEGATIVE
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    
    def is_alive(self):
        if self.health < 0:
            return self.health == 0
        else:
            return self.health > 0