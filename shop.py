from sword import *


class Shop:
    def __init__(self):
        Sword.instantiate_from_csv()
        self.swords = []
        for sword in Sword.all:
            if sword.name != "Witcher sword":
                self.swords.append(sword)

    def __repr__(self):
        reprs = ""
        for sword in self.swords:
            reprs += f"\n{self.swords.index(sword) + 1}.{sword.__repr__()}\n"
        return reprs
