from abc import ABC

from abilities.ability import AFlying, AInfect
from objects.card import Card


class Permanent(Card, ABC):  # TODO permanent should not be a child of Card (change to Object)
    def __init__(self, card):
        Card.__init__(self)
        if card:
            self.abilities = card.abilities
            self.types = card.types
            self.game = card.game
            self.untapped = True
            self.base_power = card.base_power
            self.power_mod = card.power_mod
            self.base_toughness = card.base_toughness
            self.toughness_mod = card.toughness_mod

            for a in self.abilities:
                if a.abilities:
                    for sa in a.abilities:
                        sa.card = self
                else:
                    a.card = self

    def untap(self):
        self.untapped = True

    def tap(self):
        self.untapped = False

    def deal_dmg(self, value, target):
        target.life -= value

    def calc_power(self):
        return self.base_power + self.getCountersCount("+1/+1") + self.power_mod

    def calc_toughness(self):
        return self.base_toughness + self.getCountersCount("+1/+1") + self.toughness_mod

