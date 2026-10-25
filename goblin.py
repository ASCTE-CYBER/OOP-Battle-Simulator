from enemy import Enemy


class Goblin(Enemy):
    """A basic enemy found in the arena."""

    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)