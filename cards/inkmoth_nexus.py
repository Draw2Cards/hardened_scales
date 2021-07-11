from abc import ABC

from abilities.ability import AMana
from abilities.inkmoth_nexus import AInkmothNexus
from objects.land import Land


class CInkmothNexus(Land, ABC):
    def __init__(self, player):
        Land.__init__(self)
        self.mana_cost = ""
        self.cmc = 0
        self.types = ["Land"]
        self.colors = []
        self.abilities = [AMana(["{T}"], "{C}", player), AInkmothNexus(["{1}"], self)]
