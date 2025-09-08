from enemy import Enemy

class Grim_reaper(Enemy):
    # Super ability
    def super_Attack(self):
        attack_power = int(self.attack_power)
        print("GRIM REAPER Uses Sythe!")
        return attack_power

    def soul_harvest(self):
        attack_power = int(self.attack_power * 2)
        print("GRIM REAPER Uses Soul Harvest, it drains your life force!")
        return attack_power
    
    def __init__(self, name):
        super().__init__(name)
        self.health = 600
        self.attack_power = 80