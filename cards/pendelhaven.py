from abc import ABC

from abilities.ability import AMana
from abilities.pendelhave import APendelhaven
from objects.land import Land


class CPendelhaven(Land, ABC):
    def __init__(self, player):
        Land.__init__(self)
        self.mana_cost = ""
        self.cmc = 0
        self.types = ["Legendary", "Land"]
        self.colors = []
        self.abilities = [AMana(["{T}"], "{G}", player), APendelhaven(["{T}"])]
