import csv


class Sword:
    all = []

    def __init__(self, name, price, armor_pen_rate, power, max_sword_hp, equipped):
        self.price = price
        self.name = name
        self.armor_pen_rate = armor_pen_rate
        self.power = power
        self.sword_hp = max_sword_hp
        self.max_sword_hp = max_sword_hp
        self.equipped = equipped
        if equipped:
            Sword.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('save files/sword_shop.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Sword(
                name=item.get('name'),
                price=int(item.get('price')),
                armor_pen_rate=float((item.get('armor_pen_rate'))),
                power=int((item.get('power'))),
                max_sword_hp=int((item.get('max_sword_hp'))),
                equipped=eval(item.get('equipped'))
            )

    def __repr__(self):
        return f"\nName: {self.name} \nprice: {self.price} \narmor penetration: {self.armor_pen_rate} \npower: {self.power} \nhp: {self.sword_hp}"
