import random
from enemy import Enemy
class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.health = 300
        self.attack_power = random.randint(15, 30)
    
    def attack(self):
        return random.randint(5, self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
       
     