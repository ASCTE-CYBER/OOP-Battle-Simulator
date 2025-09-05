from enemy import Enemy
import random

class The_Hunter(Enemy):
    def __init__(self,name):
        super().__init__(name)
        self.health = 400
        self.attack_power = 20

    def special_attack(self):
        tool = random.randint(1,4):
        if tool == 1:
            shotgun_shells= 6
            if shotgun_shells > 0:
                self.attack_power = random.randint(50,200)
                shotgun_shells-=1
            else:
                return print("The hunter is out of bullets!")
        elif tool == 2:
            durability = 100
            if durability > 0:
                self.attack_power = random.randint(20,50)



