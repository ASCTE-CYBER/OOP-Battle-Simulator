import random

from enemy import enemy

class witch(enemy):
   def take_damage(self, damage):
     reduced_damage= damage / 2
     return super().take_damage(reduced_damage)
   

   
