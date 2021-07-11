from abc import ABC

from abilities.ability import AEntersWithCounters, APutCounter
from abilities.hangarback_walker import AHangarbackWalker
from objects.spell import Spell


class CHangarbackWalker(Spell, ABC):
    def __init__(self, game, value):
        Spell.__init__(self)
        self.mana_cost = "{X}{X}"
        self.cmc = 1
        self.types = ["Creature", "Artifact", "Construct"]
        self.base_power = 0
        self.base_toughness = 0
        self.colors = []
        self.abilities = [AEntersWithCounters(self, game, value, "+1/+1"),
                          AHangarbackWalker(self, game),
                          APutCounter(["{1}", "{T}"], "+1/+1", self, game)]
