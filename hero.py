import random

class Hero:
    def __init__(self, name, hp=100, stamina=5, attack_power=10):
        self.name = name
        self.hp = hp
        self.stamina = stamina
        self.attack_power = attack_power

    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} receives {damage} damage! (HP: {self.hp}/100)")

    def strike(self):
        if self.stamina < 1:
            print(f"Not enough stamina for Strike! (need 1, have {self.stamina})")
            return False, 0
        self.stamina -= 1
        print(f"{self.name} uses Strike! (stamina now {self.stamina}/5)")
        return True, self.attack_power

    def power_slash(self):
        if self.stamina < 3:
            print(f"Not enough stamina for Power Slash! (need 3, have {self.stamina})")
            return False, 0
        self.stamina -= 3
        print(f"{self.name} uses Power Slash! (stamina now {self.stamina}/5)")
        if random.random() < 0.3:
            print("Power Slash missed!")
            return True, 0
        return True, int(self.attack_power * 3)

    def recovery(self):
        recover_amount = 40
        self.hp += recover_amount
        if self.hp > 100:
            self.hp = 100
        self.stamina += 4
        if self.stamina > 5:
            self.stamina = 5
        print(f"{self.name} uses Recovery and recovers {recover_amount} HP! Stamina is now {self.stamina}/5.")
        return True, 0
    
    def is_alive(self):
        return self.hp > 0
