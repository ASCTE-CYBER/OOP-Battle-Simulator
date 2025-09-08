from enemy import Enemy 

class baby_elf(Enemy):
    #a new special ability
    def cry():
        print("Wahh WAHHH")

    #overriding take damage
    def take_damage(self,damage):
        print("why are you killing babies, you monster!")
        return super().take_damage(damage)