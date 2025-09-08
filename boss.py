from enemy import Enemy
import random

class boss(Enemy):
    def __init__(self, name):
        self.name = name
        self.health = 300
        self.attack_power = random.randint(30, 40)

    
    def attack(self):
        angercount=0
        if self.health<100 and angercount<1:
            print("Now I'm ANGRY >:(")
            angercount= angercount + 1
            return (random.randint(10, self.attack_power)*2)
        elif self.health<100 and angercount>=1:
            return (random.randint(10, self.attack_power)*2)
        else:
            return random.randint(10, self.attack_power)
        


    def take_damage(self, damage):
        self.health -= damage
        # TODO We should prevent the goblins health from going into the NEGATIVE
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    
    def is_alive(self):
        if self.health < 0:
            return self.health == 0
        else:
            return self.health > 0