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
        self.health = 145
        self.power = random.randint(30, 40)
    

    def strike(self):
        if self.health >= 100:
            return 50
        return random.randint(30, 40)
    
    def receive_damage(self, damage):
        self.health-=damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
    
    #TODO define is_alive
    def is_alive(self):
        return self.health > 0
