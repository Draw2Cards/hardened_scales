from abc import ABC

from objects.card import Card


class Land(Card, ABC):
    def __init__(self, c_land=None):
        Card.__init__(self)
        if c_land:
            self.abilities = c_land.abilities
            self.counters = c_land.counters
            self.supertypes = c_land.supertypes
            self.types = c_land.types
            self.subtypes = c_land.subtypes
            self.game = c_land.game
