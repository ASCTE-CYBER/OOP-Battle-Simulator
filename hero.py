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
        self.name=name
        self.health=670
        self.armour= 50 
        self.attack_power = random.randint(50, 70)
        self.ExtraSwordStrength = random.randint(41,67)
        #TODO Set the hero's health. You might give the hero more health than a goblin.
        #TODO Set the hero's attack power. Should it be more consistent than the goblin's?
    

    def strike(self):
        if self.health<50:
            return random.randint(1, self.attack_power)
        else:
             return self.ExtraSwordStrength
        
    

        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
    
    def receive_damage(self, damage):
        self.health -= (damage-self.armour)
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
        # TODO Implement take_damage
        # TODO We should prevent health from going into the NEGATIVE
    
    #TODO define is_alive
    def is_alive(self):
            return self.health > 0