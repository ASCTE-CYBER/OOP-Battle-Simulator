from enemy import Enemy


class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""

    def __init__(self, name):
        super().__init__(name, health=250, attack_power=30)

    def attack(self):
        damage = super().attack()
        bonus_damage = 5
        print( f"{self.name} unleashes a SMASH!")
        return damage + bonus_damage

    def take_damage(self, damage):
        damage-damage *.50
        return super().take_damage(damage)