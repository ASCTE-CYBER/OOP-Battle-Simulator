from enemy import enemy

class baby_elf(enemy):
    def cry():
        print("WAHHHH WAHHHHHH")

    def take_damage(self, damage):
        print("YOU HIT A BABY U MONSTER")
        return super().take_damage(damage)
