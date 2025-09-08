from enemy import Enemy
import random

class The_Hunter(Enemy):
    def __init__(self,name):
        super().__init__(name)
        self.health = 400
        self.attack_power = 20

    def attack(self):
        tool = random.randint(1,4)
        if tool == 1:
            shotgun_shells= 6
            if shotgun_shells > 0:
                shotgun_shells-=1
                print(f"ch-POW! {self.name} fired his shot gun! Now at {shotgun_shells} bullets")
                return random.randint(50,200)
            else:
                return print("The hunter is out of bullets!")
        elif tool == 2:
            durability = 100
            self.attack_power = random.randint(20,80)
            print("The hunter slashed with his knife!")
            if durability > 0:
                if self.attack_power == 67:
                    durability = 0
                elif self.attack_power > 50:
                    durability = durability * 0.5
                elif self.attack_power > 30:
                    durability = durability * 0.5
                elif self.attack_power > 10:
                    durability = durability * 0.80
                return random.randint(20,80)
        elif tool == 3 :
            print("The hunter threw a punch!")
            return random.randint(1,10)
        else:
            if self.health > 200:
                print(f"{self.name} ran away!" )
                return False
            else:
                print(f"{self.name} tried to run, but couldn't!")
            



