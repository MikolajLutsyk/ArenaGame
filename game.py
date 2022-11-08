import os.path

from player import *
from shop import *


def start_game():
    if os.path.getsize("save files/player_save.txt") == 0:
        player = Player.create_player()
        player.save()
    shop = Shop()
    player = Player.read_player_save()
    game_process(player, shop)


def game_process(player, shop):
    continue_game = 1
    while continue_game == 1:
        print(player.__repr__())
        action = int(input("\nWhat action do you want to do: \n1 - sleep(-5 gold, but restores hp) \n2 - "
                           "buy a new sword \n3 - buy a healing potion(-5 gold each)\n4 - buy sword repair "
                           "kits(-10 gold each)\n5 - fight a goblin\nChoice: "))

        match action:
            case 1:
                player.recovery()
                player.save()
                print(player.__repr__())
            case 2:
                player.buy_sword(shop)
                player.save()
                print(player.__repr__())
            case 3:
                player.potion_buy()
                player.save()
                print(player.__repr__())
            case 4:
                player.buy_repair_kit()
                player.save()
                print(player.__repr__())
            case 5:
                player.fight_goblin()
                player.save()
                print(player.__repr__())
            case 6:
                player.fight_giant()
                player.save()
                print(player.__repr__())

        continue_game = int(input("\nDo you want to continue playing(1-yes, 2-no)? "))
        if continue_game != 1:
            print("Game stopped:)")


start_game()
