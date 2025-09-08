import random
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 67416741
        self.attack_power = random.randint(41, 67)
    

    def strike(self):
        return random.randint(8, self.attack_power)
    
    def receive_damage(self, damage):
        self.health = self.health - damage
        print(f"{self.name} recieve {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0 

