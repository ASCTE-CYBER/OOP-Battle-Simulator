from enemy import Enemy

class CoachBlanding(Enemy):
    def __init__(self, name, color):
        super().__init__(name)
        self.attack_power = 45
        self.health = 200

    def attack(self):
        if self.health < 200:
            self.attack_power = 50

        return self.attack_power
