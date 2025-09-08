from Enemy import Enemy
import random
class Boss(Enemy):
    def __init__(self, name,):
        super().__init__(name)
        self.attack_power=random.randint(10,20)
        self.health=350
    def attack(self):
        if self.health<180:
        if self.health<180:      
            self.attack_power=self.attack_power+10
        return self.attack_power

    