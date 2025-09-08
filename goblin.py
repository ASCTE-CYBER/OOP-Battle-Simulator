import random
from enemy import Enemy
class Goblin(Enemy):
    """
    This is our goblin blueprint 
    """
    def __init__(self,name, color):
        super().__init__(name)
        self.color=color
        print(f"Goblin {self.name} of color{self.color}")
       
    '''
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    '''
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color