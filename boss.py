import random
from enemy import Enemy

class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name)

    def __init__(self, name):
        self.name = name
        self.health = 200
        self.attack_power = random.randint(20, 25)

    def attack(self):
        if health < 50 
            self.attack_power = 80:
        elif self.health < 150:
            self.attack_power
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0

