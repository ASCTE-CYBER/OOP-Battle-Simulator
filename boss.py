from enemy import Enemy

class bigBoss(Enemy):
        def __init__(self, name):
            super().__init__(name)
            self.health = 300
            self.attack_power = 20
        
        def attack(self):
            if self.health > 50:
                self.attack_power = 75
            if self.health > 100:
                self.attack_power = 100
            if self.health > 200:
                self.attack_power = 150
            if self.health > 250:
                self.attack_power = 200

    