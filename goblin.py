import random
from enemy import Enemy

class Goblin(Enemy):
    """
    This is our goblin blueprint 
    """
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
 

