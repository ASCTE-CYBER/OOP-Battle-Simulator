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
        #TODO Set the hero's name.
        self.name = name 
        #TODO Set the hero's health. You might give the hero more health than a goblin.
        self.health = 175
        #TODO Set the hero's attack power. Should it be more consistent than the goblin's?
        self.attack_power = random.randint(15, 75)
    

    def strike(self):
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
        return random.randint(15, self.attack_power)
 
    
    
    def receive_damage(self, damage):
        gem = 2
        # TODO Implement take_damage
        self.health -= gem
        # TODO We should prevent health from going into the NEGATIVE
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
        if self.health < 80:
            if gem >= 1:
                self.health = 125
                print("Healing Gem has been used! Health is now 125.")
                gem = gem-1
                return gem 
    
    #TODO define is_alive
    def is_alive(self):
        return self.health > 0
    
