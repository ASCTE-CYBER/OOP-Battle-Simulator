
from enemy import enemy

class baby_elf(enemy):
   def take_damage(self, damage):
      print("why are you hitting me. IM A BABY.")
      
      return super().take_damage(damage)