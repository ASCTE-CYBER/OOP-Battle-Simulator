from enemy import Enemy
import random

class LLorona(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.atack_power = 200

    def attack(self):
        return random.randint(1, self.attack_power)

    def laugh():
        print("🤣🤣🤣")

        

