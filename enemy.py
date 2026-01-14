import random
class Enemy:
    
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0