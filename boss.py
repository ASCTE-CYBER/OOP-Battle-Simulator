from enemy import Enemy

class Boss_Baby(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 2000
        self.attack_power = 1000

    def instant_kill(self):
        if self.health < 1000:
            self.attack_power = 2000
        print("BOOM SHAKALAKA")
        

    #Override Take Dammage
    def take_damage(self,  damage):
        print("WAHH")
        return super().take_damage(damage)
        
