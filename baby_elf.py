from enemy import Enemy

class baby_elf(Enemy):
    def cry():
        print("WAHHHHHHH WAHHHHHHH")

    def take_damage(sekf, damage):
        print("YOU MONSTER, WHY DID YOU ATTACK THE BABY, LOCK IN!!!")
        return super().take_damage(damage)