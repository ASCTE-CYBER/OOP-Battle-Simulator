from enemy import Enemy

class BabyElf(Enemy):
    def take_damage(self, damage):
        self.health -= damage
        print("OW!!!!! How could you hit a baby 😭 you MONSTER!")

