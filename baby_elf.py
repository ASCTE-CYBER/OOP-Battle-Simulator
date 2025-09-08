from enemy import Enemy

class baby_elf(Enemy):
    def cry():
        print("WAHHHHHHHHHHHH WAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

    def take_damage(self, damage):
        print("You monster, you babykiller, mom doesnt love you, dad left you, monster, you freak, you mistake, mom wished you wernt born")
        return super().take_damage(damage)