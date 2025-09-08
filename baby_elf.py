from enemy import Enemy

class Babyelf(Enemy):
    def take_damage(self, damage):
        self.health -=damage
        print("cry, how could u hit a baby :")