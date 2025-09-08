from enemy import Enemy
import random

class mrs_wright(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 30
        
    def attack(self):
        if self.health<70:
            self.attack_power, 140
        return (self.attack_power)

