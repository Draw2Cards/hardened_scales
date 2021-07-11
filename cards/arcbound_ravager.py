from abc import ABC

from abilities.ability import APutCounter
from abilities.modular import AModularStatic, AModularTriggered
from objects.spell import Spell


class CArcboundRavager(Spell, ABC):
    def __init__(self, game):
        Spell.__init__(self)
        self.mana_cost = "{1}"
        self.cmc = 1
        self.types = ["Creature", "Artifact", "Beast"]
        self.base_power = 0
        self.base_toughness = 0
        self.colors = []
        self.abilities = [APutCounter(["sac"], "+1/+1", self, game),
                          AModularStatic(self, game, 1),
                          AModularTriggered(self, 1, game)]
