from enemy import Enemy

class MegaKnight(Enemy):
    def __init__(self, name, color):
        super().__init__(name)
        self.attack_power = 25
        self.health = 350
    
    def attack(self):
        if self.health < 100:
            print(f"{self.name} is in a rage! Attack power massively increased!")
            self.attack_power = 45
        elif self.health < 200:
            print(f"{self.name} is enraged! Attack power heavily increased!")
            self.attack_power = 40
        elif self.health < 300:
            print(f"{self.name} is furious! Attack power increased!")
            self.attack_power = 35
        elif self.health < 325:
            print(f"{self.name} is getting angry! Attack power slightly increased!")
            self.attack_power = 30
        return self.attack_power
    
    