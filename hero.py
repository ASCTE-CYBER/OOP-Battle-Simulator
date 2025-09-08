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
        self.health = 300 
        #TODO Set the hero's attack power. Should it be more consistent than the goblin's?
        self.attack_power = random.randint(25, 50)
    

    def strike(self):
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
        return random.randint(1, self.attack_power)

    def receive_damage(self, damage):
        med_kit = 1
        # TODO Implement take_damage
        self.health -= med_kit
        # TODO We should prevent health from going into the NEGATIVE
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now{self.health}.")
        if self.health < 200:
            if med_kit >= 1:
                self.health == 250
                print("Medkit used")
                med_kit = med_kit - 1

    def more_bandages(hero, goblin):
        if hero.is_alive and (not goblin.is_alive):
            med_kit = med_kit + 1

    
    #TODO define is_alive
    def is_alive(self):
        return self.health > 0
