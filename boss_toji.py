from enemy import Enemy
import random


class Boss_Toji(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 500
        self.attack_power = random.randint(15, 25)

    def attack(self):
        return random.randint(10, self.attack_power)

    def inverted_spear_of_heaven(self):
        print("Toji used the Inverted Spear of Heaven to bypass Infinity!")
        return 100
