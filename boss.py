from enemy import Enemy
import random

class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.attack_power = random.randint(30,50)

    def attack(self):
        choice = random.choice(["normal", "bomb"])
        if choice == "bomb":
            aim = random.randint(1,3)
            if aim == 1:
                self.health -= 50
                self.attack_power = 0
                print("The boss aimed poorly!")
            elif aim == 2:
                self.health -= 25
                self.attack_power = 25
                print("The boss's aim was mediocre!")
            elif aim == 3:
                self.attack_power = 50
                print("The boss aimed perfectly!")
        if choice == "normal":
            self.attack_power = random.randint(25,50)

        return self.attack_power