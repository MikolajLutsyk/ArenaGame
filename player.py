import random

from goblin import *
from sword import *


class Player:
    def __init__(self, name, maxhp, gold, exp, potions, sword, repair_kits, akt_hp):
        self.name = name
        self.maxhp = maxhp
        self.gold = gold
        self.exp = exp
        self.potions = potions
        self.sword = sword
        self.powerups = 2
        self.repair_kits = 2
        self.akthp = akt_hp
        self.repair_kits = repair_kits
        self.lvl = 0

    @classmethod
    def read_player_save(self):
        player_save = open("save files/player_save.txt", "r")
        lines = player_save.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "")
        sword = Sword(lines[5], int(lines[6]), float(lines[7]), int(lines[8]), int(lines[9]), eval(lines[10]))
        sword.sword_hp = int(lines[13])
        player = Player(lines[0], int(lines[1]), int(lines[2]), int(lines[3]), int(lines[4]), sword, int(lines[11]),
                        float(lines[12]))
        return player

    @classmethod
    def create_player(cls):
        standard_sword = Sword("Witcher sword", 10, 0.1, 10, 100, True)
        pl_name = input("Put your name in: ")
        player = Player(pl_name, 100, 50, 0, 2, standard_sword, 2, 100)
        return player

    def __repr__(self):
        return "\nPlayer name: " + self.name + "\nMax hp: " + str(self.maxhp) + "\nCurrent hp: " + str(self.akthp) + \
               "\nGold: " + str(self.gold) + "\nExp: " + str(self.exp) + "\nSword name: " + self.sword.name + \
               "\nHealing potions: " + str(self.potions) + "\nRepair kits: " + str(self.repair_kits)

    def save(self):
        player_save = open("save files/player_save.txt", "w")
        save_text = self.name
        save_text += "\n" + str(self.maxhp)
        save_text += "\n" + str(self.gold)
        save_text += "\n" + str(self.exp)
        save_text += "\n" + str(self.potions)
        save_text += "\n" + self.sword.name
        save_text += "\n" + str(self.sword.price)
        save_text += "\n" + str(self.sword.armor_pen_rate)
        save_text += "\n" + str(self.sword.power)
        save_text += "\n" + str(self.sword.max_sword_hp)
        save_text += "\n" + str(self.sword.equipped)
        save_text += "\n" + str(self.repair_kits)
        save_text += "\n" + str(self.akthp)
        save_text += "\n" + str(self.sword.sword_hp)

        player_save.writelines(save_text)
        self.__repr__()

    def sleep(self):
        if self.gold - 3 >= 0:
            self.gold -= 3
            self.hp = self.maxhp
            print("You took a nap in a tavern")
        else:
            print("\nNot enough gold!\n")

    def buy_sword(self, shop):
        print(shop.__repr__())
        sword_num = int(input("Choose a sword: "))
        if shop.swords[sword_num - 1].name == self.sword.name:
            print("Already equipped, try again!")
            self.buy_sword(shop)
        else:
            if self.gold - shop.swords[sword_num - 1].price >= 0:
                self.sword = shop.swords[sword_num - 1]
                self.sword.equipped = True
                self.gold -= shop.swords[sword_num - 1].price
            else:
                print("Not enough gold!")

    def potion_buy(self):
        count = input("\nHow many potions do you want to buy(exit - main menu): ")
        if count != "exit":
            if self.gold - 5 * int(count) >= 0:
                self.gold -= 5 * int(count)
                self.potions += int(count)
            elif self.gold - 5 * int(count) < 0:
                print("\nNot enough gold!\n")
        else:
            print("returning to main menu")


    def buy_repair_kit(self):
        count = int(input("\nHow many repair kits do you want to buy: "))
        if self.gold - 10 * count >= 0:
            self.gold -= 10 * count
            self.repair_kits += count
        else:
            print("\nNot enough gold!\n")

    def use_repair_kit(self):
        if self.sword.hp + 20 <= self.sword.max_sword_hp:
            self.sword.hp += 20
        else:
            print("\nSword is too good for a repair!\n")

    def fight_goblin(self):
        goblin = Goblin(int(self.exp / 20))
        attacks_on_row_left = goblin.attacks_in_row
        attack_order = random.randint(1, 2)
        continue_playing = 1

        while continue_playing == 1:
            if attack_order % 2 == 1:
                prev_hp = self.akthp
                self.akthp = goblin.attack(self.akthp, attacks_on_row_left)
                if prev_hp == self.akthp:
                    attacks_on_row_left = 4 + goblin.lvl
                else:
                    attacks_on_row_left -= 1
                print("\nGoblin attacked\n")
            else:
                action = int(input(f"\nEnter your action: \n1. Use Potion({self.potions} left) \n2. "
                                   f"Fix the sword({self.repair_kits} repair kits left) \n3. Attack"))
                match action:
                    case 1:
                        self.akthp += 15 + int((self.exp / 20) * 3)
                        self.potions -= 1
                    case 2:
                        self.use_repair_kit()
                    case 3:
                        goblin.hp -= self.sword.power / 2
                        self.sword.sword_hp -= 5
                        print(f"\n{self.name} attacked\n")
            attack_order += 1
            print(f"Goblin hp: {goblin.hp} \n{self.name} hp: {self.akthp}")
            if goblin.hp <= 0:
                print(f"\n{self.name} wins!\n")
                self.gold += 20
                if goblin.lvl == 0:
                    self.exp += 15
                else:
                    self.exp += goblin.lvl * 20
                continue_playing = 0
            elif self.akthp <= 0 or self.sword.sword_hp <= 0:
                continue_playing = 0
                print("\nGoblin wins:(\n")
                self.akthp = self.maxhp
                if self.gold - 20 < 0:
                    self.gold = 0
                else:
                    self.gold -= self.gold / 2
        print(goblin.__repr__())

    def fight_giant(self):
        print("Pizdilka")
