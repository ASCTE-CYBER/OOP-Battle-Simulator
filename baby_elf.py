from enemy import enemy

class BabyElf(enemy):
    
    def take_damage(self, damage):
        self.health -= damage
        