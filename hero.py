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
        self.hp = 160
        self.attack_power = 22.5
    

    def strike(self):
        return self.attack_power
    
    def receive_damage(self, damage):
        self.hp -= damage
        if (self.health <= -1):
            print(f"{self.name} takes {damage} damage. {self.name} is now dead")
        else:
            print(f"{self.name} takes {damage} damage. Health is now {self.hp}.")
    
    def is_alive(self):
        return self.hp > 0
