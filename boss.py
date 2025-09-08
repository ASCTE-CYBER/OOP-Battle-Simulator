from enemy import Enemy

class bossgoblin(Enemy):
    def take_damage(self, damage):
        self.health -= damage

    def attack(self):
        if self.health<200:
            self.attack_power=40
        elif self.health<150:
            self.attack_power=50
        elif self.health<100:
            self.attack_power=65
        elif self.health<50:
            self.attack_power=80
        return self.attack_power