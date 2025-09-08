import random
from enemy import Enemy

class Boss(Enemy):
    def __init__(self, name):
        self.name = name
        self.health = 250
        self.attack_power = random.randint(50, 70)


    def specialattack(self):
        self.attack_power = 100
        print("FIRE BLAST!!!!")
        return random.randint(10, self.attack_power)

    def attack(self):
        strike =  random.randint(25, self.attack_power)
        if strike <= 30:
            return self.specialattack

        return strike
       