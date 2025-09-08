import random
class Enemy: 
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = random.randint(12, 18)
        self.size = 21
    def attack(self):
        attack = random.randint(1, self.attack_power)
        if attack > 14:
            print(f"{self.name}'s attack was critical!")
        return attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        # TODO We should prevent the goblins health from going into the NEGATIVE
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
        if self.health == 0:
            print(f"{self.name} has died!")

    def is_alive(self):
        return self.health > 0
