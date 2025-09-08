from enemy import Enemy

class BabyElf(Enemy):
    def take_damage(self, damage):
        self.health -= damage
        if self.health< 0:
            self.health=0
            print("Cry!! how could you hit a baby?! You MONSTER!!!")