class Enemy:

    def __init__(self, name, hp, lvl, attacks_in_row, cooldown):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.attacks_in_row = attacks_in_row
        self.cooldown = cooldown

    def attack(self, player_hp, attacks_in_row_left, damage):
        if attacks_in_row_left > 0:
            player_hp -= damage + self.lvl * 3
            print(f"\n{self.name} made a hit!\n")
            return player_hp
        else:
            print(f"\n{self.name} is on cooldown!\n")
            return player_hp

