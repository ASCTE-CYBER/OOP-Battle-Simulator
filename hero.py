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
        self.health = 9999999999
        self.defence = random.randint(1,100)
        self.attack_power = 9999
    

    def strike(self, crit):
        if crit == True:
            return 999999999
        else:
            return random.randint(100,self.attack_power)
    
    def receive_damage(self, damage):
        damage_taken = damage - self.defence
        self.health = self.health - damage_taken
        if self.health <= 0:
            print(f"{self.name} is dead!")
        else:
            print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
    
    def is_alive(self):
        return self.health > 0

