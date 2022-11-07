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
        self.super_use_rate = 4
        self.regeneration = 2

    def __repr__(self):
        return f"name: {self.name} \nhp: {self.hp} \nlvl: {self.lvl}"

    def attack(self, player_hp, attacks_in_row_left):
        if attacks_in_row_left > 0:
            player_hp -= 10 + self.lvl * 3
            return player_hp
        else:
            return player_hp
