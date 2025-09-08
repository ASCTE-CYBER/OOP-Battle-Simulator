from enemy import enemy
class BabyElf(enemy):
    def take_damage(self, damage):
        self.health -=damage
        print("Cry, How could you hit a baby, you monster!")
    