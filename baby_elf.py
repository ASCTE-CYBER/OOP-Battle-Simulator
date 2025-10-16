from enemy import Jim

class baby_elf(Jim):
    def cry():
        #New attribute
        print("WAAAHHHHHHHHHH")
    def take_damage(self, damage):
        #Overriding take damage
        print("WHY ARE YOU ATTACKING A BABY YOU MONSTER!")
        return super().take_damage(damage)
    
    