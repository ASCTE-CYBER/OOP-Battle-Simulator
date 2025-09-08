from enemy import Enemy

class BabyElf(Enemy):
   def take_damage(self, damage):
        self.health -= damage
        print("Cry, Im just a behbeh :(")