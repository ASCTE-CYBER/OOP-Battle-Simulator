from enemy import Enemy

class Baby_Elf(Enemy):
    #NewAbility
    def cry():
        print("WAHHH WAHHH")


#Override Take Damage
def take_damage(self, damage):
    print("YOU HIT A BABY!!! YOU MONSTER")
    return  super().take_damage(damage)






