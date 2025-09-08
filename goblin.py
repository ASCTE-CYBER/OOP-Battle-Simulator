import random

from enemy import enemy

class Goblin(enemy):
   def __init__(self,name, color):
      super().__init__(name)
      self.color = color
