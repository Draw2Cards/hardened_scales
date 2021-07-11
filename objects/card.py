from abc import ABC

from abilities.ability import TriggeredAbility, StaticAbility
from objects.object import Object


class Card(Object, ABC):
    def __init__(self):
        Object.__init__(self)
        self.abilities = []
        self.types = []
        self.power_mod = 0
        self.toughness_mod = 0
        self.game = None
        self.base_power = None
        self.base_toughness = None

    def getCountersCount(self, counter_name):
        return self.counters.get(counter_name, 0)

    def onDestroy(self):
        for a in self.abilities:
            if isinstance(a, StaticAbility):
                a.revoke()
            else:
                for sa in a.abilities:
                    if isinstance(sa, StaticAbility):
                        sa.revoke()

        for a in self.abilities:
            if isinstance(a, TriggeredAbility):
                if a.isTriggeredOn("Destroy"):
                    a.execute()
            else:
                for sa in a.abilities:
                    if isinstance(sa, TriggeredAbility):
                        if sa.isTriggeredOn("Destroy"):
                            sa.execute()

    def getTypes(self):
        return self.types

    def isTypes(self, card_type):
        if not isinstance(card_type, list):
            for t in self.types:
                if t == card_type:
                    return True
        else:
            for t in card_type:
                if not self.isTypes(t):
                    return False
            return True
        return False

    def set_modifier(self, mod):
        self.power_mod = mod[0]
        self.toughness_mod = mod[1]
