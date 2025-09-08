from enemy import Enemy
import random

class Tarrasque(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = random.randint(50, 70)
        self.health= 676


    def bite(self):
        return random.randint(30, self.attack_power)
    
    def claw(self):
        return random.randint(5, self.attack_power)
    
    def tail(self):
        return random.randint(20, 60)