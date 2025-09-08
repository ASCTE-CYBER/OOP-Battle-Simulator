import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 525
        self.attack_power = random.randint(40, 45)
    
    def strike(self):
        return random.randint(20, self.attack_power)
    
    def receive_damage(self, damage):
        self.health = self.health - damage 
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
    
    def is_alive(self):
        return self.health > 0
