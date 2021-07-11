from abc import ABC

from abilities.power_conduit import APowerConduit
from objects.spell import Spell


class CPowerConduit(Spell, ABC):
    def __init__(self, game):
        Spell.__init__(self)
        self.mana_cost = "{2}"
        self.cmc = 2
        self.types = ["Artifact"]
        self.colors = []

        self.abilities = [APowerConduit(["{T}", "counter"], "+1/+1", self, game)]

