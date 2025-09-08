from enemy import Enemy
import random

class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.attack_power = 15
        print(self.attack_power)
    
    def stone_throw(self):
        
        if self.health == 10:
            print("Dragon throwing stones")
        elif self.health == 20:
            print("Fire Breathing Attack")
            self.attack_power = 100
        return self.attack_power
        
        
        
    
    #Override take damage
    #def fire_breath(self, damage):
       # print("Fire Breathing Attack")
       # return super().take_damage(damage)
