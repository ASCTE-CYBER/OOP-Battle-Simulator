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
        self.hp = 150  
        self.attack_power = 25
        self.stamina = 3

    def strike(self):
        if self.stamina < 2:
            print(f"Not enough stamina for Strike! (need 2, have {self.stamina})")
            return 0
        self.stamina -= 2
        print(f"{self.name} uses Strike! (stamina now {self.stamina}/5)")
        return self.attack_power

    def power_slash(self):
        if self.stamina < 3:
            print(f"Not enough stamina for Power Slash! (need 3, have {self.stamina})")
            return 0
        self.stamina -= 3
        print(f"{self.name} uses Power Slash! (stamina now {self.stamina}/5)")
        if random.random() < 0.2:
            print("Power Slash missed!")
            return 0
        return int(self.attack_power * 2)

    def recovery(self):
        recover_amount = 40
        self.hp += recover_amount
        if self.stamina < 5:
            self.stamina += 2
            if self.stamina > 5:
                self.stamina = 5
        print(f"{self.name} uses Recovery and recovers {recover_amount} HP! Stamina is now {self.stamina}/5.")
        return 0

    
    def receive_damage(self, damage):
        self.hp -= damage
        if (self.hp < 0):
            self.hp = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.hp}.")
    
    def is_alive(self):
        return self.hp > 0