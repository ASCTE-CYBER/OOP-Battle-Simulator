import random


class Goblin:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 15

    def attack(self):
        "This returns a random amount of damage based on the attack power that hits the goblin"
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        "This subtracts the health without letting it fall below zero."
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        "This remains True while the goblin is still alive"
        return self.health > 0
