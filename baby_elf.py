from enemy import Enemy

class Baby_Elf(Enemy):
    #NEW ABILITY
    def cry():
        print("Waaah! Waaah!")

        #OVERRIDE TAKE DAMAGE
    def take_damage(self, damage):
        print("You hit a baby you monster")
        return super().take_damage(damage) 