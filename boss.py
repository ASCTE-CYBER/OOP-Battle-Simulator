from enemy import Enemy

class Fey(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150 
        self.attack_power = 8

    def  attack(self):
        if self.health < 20:
            self.attack_power = 35
            print(f"👹RAWR👹")
        elif self.health < 75:
            self.attack_power = 16
        return self.attack_power    
            
    """
    This is our boss blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    
   