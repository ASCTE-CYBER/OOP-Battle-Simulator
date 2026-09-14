import random

class Monster:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):#, health, power, mana):
        self.name = name
        self.health = 100#health
        self.attack_power = 15#power
        #self.mana = mana

    def attack(self):
        """Return a random amount of damage."""
        attackDamage = random.randint(0, self.attack_power+5)
        if attackDamage == self.attack_power:
            attackDamage = attackDamage + self.attack_power
            print("critical hit")
        return attackDamage

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0
