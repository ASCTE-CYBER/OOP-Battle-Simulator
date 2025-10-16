import random
from boss import Kenny_Clark

class Hero:


    
    """
    This is our hero blueprint.
    
    O=('-'Q)
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 250
        self.strength = random.randint(30, 70)
   

    def strike(self):
        return random.randint(10,self.strength)
    
    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0 


    def is_alive(self):  
        return self.health > 0
        
        # TODO We should prevent health from going into the NEGATIVE
    
    #TODO define is_alive
 

