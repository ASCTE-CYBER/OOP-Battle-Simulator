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
        if self.health < 12:
            print("BIG IRISH UPGRADE YOU SMALL PATHETIC CHILD")
            print("HEALTH IS NOW 50 POINTS HIGHER")
            self.health = 50
        return random.randint(1, self.attack_power)


    def take_damage(self, damage):
        return super().take_damage(damage)
        
       
    