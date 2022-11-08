from enemy import *


class Giant(Enemy):
    def __init__(self, lvl):
        attacks_in_row = 2
        if lvl > 0:
            attacks_in_row = 1 + lvl
        super().__init__(
            name="Giant",
            hp=150+lvl*20,
            lvl=lvl,
            attacks_in_row=attacks_in_row,
            cooldown=3
        )
        self.super_use_rate = 6
        self.armor = 100 + lvl * 10

    def __repr__(self):
        return f"name: {self.name} \nhp: {self.lvl} \nlvl: {self.lvl}"