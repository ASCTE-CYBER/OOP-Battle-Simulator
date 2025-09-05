from Enemy import Enemy
class BabyElf(Enemy):
    def take_damage(self,damage):
        print("why are you hitting a babY elf! you monster")
        return super().take_damage(damage)