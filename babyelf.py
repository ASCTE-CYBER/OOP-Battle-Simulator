from enemy import Enemy

class BabyElf(Enemy):
    def take_damage(self, damage):
        print("Why are you hitting a baby elf, you monster?!")
        return super().take_damage(damage)