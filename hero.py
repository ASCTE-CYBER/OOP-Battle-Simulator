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
        self.attack_power = random.randint(40, 50)
    

    def strike(self):
        return random.randint(15, self.attack_power)
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"Health is {self.health}:")
        # TODO Implement take_damage
        # TODO We should prevent health from going into the NEGATIVE
    
    #TODO define is_alive
    def is_alive(self):
        if self.health == 0:
            return False
        else:
            return True


