from ENEMY import ENEMY
import random
class Big_Irish_Man(ENEMY):
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 3
        self.health = 100
    def Insult():
        print("You small individual")

    def attack(self):
        self.attack_power = random.randint(3, 50)
        return random.randint(1, self.attack_power)


    def take_damage(self, damage):
        return super().take_damage(damage)
        
       
    