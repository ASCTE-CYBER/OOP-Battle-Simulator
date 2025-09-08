from enemy import Enemy
import random

class Jimmy(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = random.randint(10, 20)
        self.health = 250

    def attack(self):
        if self.health < 50:
            self.attack_power = random.randint(1, 5)
        elif self.health < 100:
            self.attack_power = random.randint(5, 10)
        return random.randint(5, self.attack_power)