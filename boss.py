from enemy import enemy

class bigboss(enemy):
    def __init__(self, name):
            super().__init__(name)
            self.health = 500
            self.attack_power = 250
    def take_damage(self, damage):
        if self.health > 250:
            self.health -= damage / 2
        else:
            self.health -= damage

             