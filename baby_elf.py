from enemy import enemy

class Baby_Elf(enemy):
    #NEW ABILITY
    def cry():
        print("WAHHH WAHHH")

    #Override Take Dammage
    def take_damage(self,  damage):
        print("YOU HIT A BABY YOU MONSTER")
        return super().take_damage(damage)