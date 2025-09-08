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
        #TANK
        self.name=name
        self.health=999
        self.attack_power=random.randint(3,20)

    

    def strike(self):
        return random.randint(1, self.attack_power) + 10
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
    
    def heal(self):
        heal=random.randint(1,10)
        self.health=self.health+(heal/2)
    
    def receive_damage(self, damage):
        turnH=True
        while self.health>=0 and turnH==True:
            self.health -= damage
            print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
            turnH=False


    def is_alive(self):
        return self.health > 0
