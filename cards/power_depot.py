from abc import ABC

from abilities.ability import ATapped, AMana
from abilities.modular import AModular
from objects.land import Land


class CPowerDepot(Land, ABC):
    def __init__(self, player, game):
        Land.__init__(self)
        self.mana_cost = ""
        self.cmc = 0
        self.types = ["Artifact", "Land"]
        self.colors = []
        self.abilities = [ATapped(self),
                          AMana(["{T}"], "{C}", player),
                          AModular(self, game, 1)]  # TODO 3th ability is missing
