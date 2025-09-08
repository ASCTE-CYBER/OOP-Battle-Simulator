from enemy import Enemy
class Baby_elf(Enemy):
    #new ability 
    def cry():
        print("WAHHH WAHHHH")

    #override take damage
    def take_damage(self, damage):
        print("YOU HIT A BABY YOU HORIBLE PERSON")
        return super().take_damage(damage)