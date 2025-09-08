from enemy import Enemy

class Baby_Elf(Enemy):
    def cry():
        print('WAH WAH')

    def take_damage(self, damage):
        print('you hit a baby :(')
        return super().take_damage(damage)