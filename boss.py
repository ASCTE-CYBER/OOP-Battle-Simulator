from enemy import Enemy
import random

class Small_Cheese(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 500
        self.attack_power = random.randint(40, 75)
    def attack(self):
        if self.health < 50:
            self.attack_power = 90
        elif self.health < 100:
            self.attack_power = 80
        elif self.health < 175:
            self.attack_power = 60
        elif self.health < 250:
            self.attack_power = 50
        return self.attack_power
    def damage(self, damage, health):
        print(f"{self.name} You have been hit by the boss for  + {self.damage} +  damage and have  + {self.health} + remaining")
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
    