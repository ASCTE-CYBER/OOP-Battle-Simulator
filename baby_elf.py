from enemy import Enemy

class baby_elf(Enemy):
    def cry():
        print("waaaaaaahhh waaahahahaaahhhh")
#overide taking damage
    def take_damage(self, damage):
        print("Why are you attacking a baby meanie? >:(")
        return super().take_damage(damage)