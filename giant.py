from enemy import *


class Giant(Enemy):
    def __init__(self, lvl):
        super().__init__(
            name="Goblin",
            hp=150+self.lvl*20,
            lvl=lvl,
            attacks_in_row=1+lvl,
            cooldown=2
        )
        self.super_use_rate = 6
        self.armor = 100 + self.lvl*10
