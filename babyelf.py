from ENEMY import ENEMY
class Baby_Elf(ENEMY):
    def cry():
        print("WAAAAAAAAA")

    def take_damage(self, damage):
        print("WHY DID U HIT THE BABY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return super().take_damage(damage)
    