import random 
class boss:

    def __init__(self, name):
        super()._init_(name)
        self.color = "purple"
        self.name = "BOSS"
        self.health = 175
        self.attack_power = random.randint(10, 25)

    def attack(self):
        return random.randint(10, self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        # TODO We should prevent the goblins health from going into the NEGATIVE
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    