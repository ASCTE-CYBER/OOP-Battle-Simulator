from enemy import Enemy

class Baby_Elf(Enemy):
    def cry():
        print("WAHHHH WAHHHH")

    #override take damage
    def take_damage(self, damage):
        print("YOU HIT A BABY! YOU MONSTER!!! 😭😡")
        return super().take_damage(damage)