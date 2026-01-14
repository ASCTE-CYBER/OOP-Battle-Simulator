import random
from enemy import Enemy
class Boss(Enemy):
    """
    Boss blueprint.

    """
    
    def __init__(self, hp):
        self.name = "Jeromy"
        self.hp = 10000000000
    
    def attack(self):
        if random.randint(1,2) == 1:
            self.dmg = random.randint(1, 1000)
        else:
            self.dmg = random.randint(1,1000000)
    
    def is_alive(self):
        return self.hp > 0