import random
from enemy import Enemy

class Goblin(Enemy):
   
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        print(f"Goblin {self.name} of color {self.color} has entered the battle!")

       

    def attack(self):
        return random.randint(1, self.attack_power)

   
        
        # TODO We should prevent the goblins health from going into the NEGATIVE
        self.health = max(0, self.health)
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

