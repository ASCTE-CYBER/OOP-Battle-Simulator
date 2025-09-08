import random
from enemy import Enemy 


class boss_baby(Enemy):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        # Boss has more health and power
        self.health = 350
        self.attack_power = 23

    def firePower(self): 
        return 25

    attack_counter = 0
    def attack(self): 
        attack_counter = + 1 
        if attack_counter % 5 == 0:
            return self.firePower()
        
        if self.health < 5: 
            self.attack_power = self.health * 10
            if self.attack_power > 30: 
                print("Big Boss is MAAAAAAAAD!!!!!!!!!")
        return self.attack_power
    



