from enemy import enemy

class landon_burton_boss(enemy):
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 123456789012345673645645
        self.health = 12345678456543456765434567654345676540

    def attack(self):
        if self.health < 123456789:
            self.health += 1234567
            self.attack_power = 1234567890123456736456450
        return self.attack_power

    