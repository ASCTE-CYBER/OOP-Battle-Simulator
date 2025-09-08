import random 
from enemy import enemy 
class SlimeBoss(enemy):

    def __init__(self, name):
        super()._init_(name)
        self.health = 250
        self.attack_power = 30

    def attack(self):
        return random.randint(1, self.attack_power)
    print("BOSS attacks")

    def take_damage(self, damage):
        self.health -= damage
        # TODO We should prevent the goblins health from going into the NEGATIVE
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def attack(self):
        if self.health < 250:
            self.attack_power = 35
        elif self.health < 150:
            self.attack_power = 45
        elif self.health < 100:
            self.attack_power = 55
        elif self.health < 50:
            self.attack_power = 65
        return self.attack_power
    
    