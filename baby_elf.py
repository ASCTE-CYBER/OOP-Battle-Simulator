from enemy import Enemy

class Baby_Elf(Enemy):
    #new ability
    def cry():
        print("WAHHHHH WAHHHH")
    
    #Override take damage
    def take_damage(slef, damage):
        print("YOU HIT A BABY! YOU MONSTER!!!")
        return super().take_damage(damage)
