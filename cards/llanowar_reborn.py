from abc import ABC

from abilities.ability import ATapped, AMana
from abilities.graft import AGraft
from objects.land import Land


class CLlanowarReborn(Land, ABC):
    def __init__(self, player, game):
        Land.__init__(self)
        self.mana_cost = ""
        self.cmc = 0
        self.types = ["Land"]
        self.colors = []
        self.abilities = [ATapped(self), AMana(["{T}"], "{G}", player), AGraft(self, 1, game)]
