from abc import ABC

from abilities.hardened_scales import AHardenedScales
from objects.spell import Spell


class CHardenedScales(Spell, ABC):
    def __init__(self, game):
        Spell.__init__(self)
        self.mana_cost = "{G}"
        self.cmc = 1
        self.types = ["Enchantment"]
        self.colors = []

        self.abilities = [AHardenedScales(game.counter_mgr)]
