from enemy import Enemy
import random

class Ogre(Enemy):
    def Attack(self):
        return random.randint(20, self.attack_power) * 10
    def health(self):
        return self.health + 20
    def specialAbility(self):
        if self.health < 20:
            self.health + 20 == self.health 
            print("extra armour for the Ogre! good luck!")

