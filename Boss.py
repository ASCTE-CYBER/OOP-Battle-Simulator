from Enemy import Enemy
import random
class Boss(Enemy):
    def __init__(self, name,):
        super().__init__(name)
        self.attack_power=20
        self.health=360
    def attack(self):
        if self.health<180:
            while Enemy.is_alive == True:
                self.attack_power=self.attack_power+1

    