from enemy import Enemy

class Baby_Elf(Enemy):
    def cry():
        print("WAHHHH WAHHHHH")
    
    def take_damage(self, damage):
        print("YOU HIT A BABY YOU MONSTER")
        return super().take_damage(damage)