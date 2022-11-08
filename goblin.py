from enemy import *


class Goblin(Enemy):
    def __init__(self, lvl):
        super().__init__(
            name="Goblin",
            hp=100+lvl*10,
            lvl=lvl,
            attacks_in_row=4+lvl,
            cooldown=1
        )
        self.regeneration = 4

    def __repr__(self):
        return f"name: {self.name} \nhp: {self.hp} \nlvl: {self.lvl}"
