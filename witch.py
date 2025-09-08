from enemy import Enemy

class Witch(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 300
        self.attack_power = 10

    def attack(self):
        if self.health < 50:
            self.attack_power = 100
        print('ATTACKKKK!!💥💥')
        return self.attack_power
    
    def fly():
        print("Fly away!!🧹🧹")

    def poison():
        print("You've been poisoned...🎃🎃")