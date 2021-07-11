from abc import ABC

from abilities.ability import AMana
from objects.land import Land


class CForest(Land, ABC):
    def __init__(self, player):
        Land.__init__(self)
        self.mana_cost = ""
        self.cmc = 0
        self.types = ["Basic", "Land", "Forest"]
        self.colors = []
        self.abilities = [AMana(["{T}"], "{G}", player)]
