from enemy import Enemy

class baby_elf(Enemy):
    # a new special ablity
    def cry():
        print("wahh wahhh")
        
# overriding take damage
    def take_damage(self, damage):
        print("Why are you attacking a baby you monster")
        return super().take_damage(damage)