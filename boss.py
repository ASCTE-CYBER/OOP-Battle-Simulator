import random
from enemy import Enemy

class Basilisk(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 100
        self.attack_power = random.randint(15, 30)
    def sting(self):
        return 50
    def attack(self):
        choice = random.choice(["normal", "sting"])
        if choice == "sting":
            return self.sting()
        if self.health < 50:
            self.attack_power = 30
        elif self.health < 75:
            self.attack_power = 25
        elif self.health < 90:
            self.attack_power = 20
        return self.attack_power
    

