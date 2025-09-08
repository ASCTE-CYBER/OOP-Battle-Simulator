from enemy import Enemy

class Sparky(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 110
        self.attack_power = 25
    def attack(self):
        if self.health <50:
            print("SPARKY IS ANGRY!!")
            self.attack_power= self.attack_power *2

        return self.attack_power