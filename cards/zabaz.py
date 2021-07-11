from abc import ABC

from abilities.modular import AModular
from abilities.zabaz import AZabaz
from objects.spell import Spell


class CZabaz(Spell, ABC):
    def __init__(self, game):
        Spell.__init__(self)
        self.mana_cost = "{1}"
        self.cmc = 1
        self.types = ["Legendary", "Creature", "Artifact", "Insect"]
        self.base_power = 0
        self.base_toughness = 0
        self.colors = []

        self.abilities = [AModular(self, game, 1), AZabaz(game)]
