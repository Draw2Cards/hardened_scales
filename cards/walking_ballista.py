from abc import ABC

from abilities.ability import AEntersWithCounters, APutCounter
from abilities.walking_ballista import AWalkingBallista
from objects.spell import Spell


class CWalkingBallista(Spell, ABC):
    def __init__(self, game, value):
        Spell.__init__(self)
        self.mana_cost = "{X}{X}"
        self.cmc = 1
        self.types = ["Creature", "Artifact", "Construct"]
        self.base_power = 0
        self.base_toughness = 0
        self.colors = []
        self.abilities = [AEntersWithCounters(self, game, value, "+1/+1"),
                          APutCounter(["{4}"], "+1/+1", self, game),
                          AWalkingBallista(["counter"], self, game)]
