from abc import ABC

from abilities.ability import Ability, StaticAbility, TriggeredAbility


class AHardenedScales(Ability, ABC):
    def __init__(self, counter_mgr):
        Ability.__init__(self)
        self.abilities = [AHSStatic(counter_mgr), AHSTriggered(counter_mgr)]


class AHSStatic(StaticAbility, ABC):
    def __init__(self, counter_manager):
        StaticAbility.__init__(self)
        self.counter_manager = counter_manager

    def execute(self):
        self.counter_manager.raiseModifier("Creature")

    def revoke(self):
        self.counter_manager.reduceModifier("Creature")


class AHSTriggered(TriggeredAbility, ABC):
    def __init__(self, counter_manager):
        TriggeredAbility.__init__(self)
        self.triggered_on = "Destroy"  # TODO should be on __del__
        self.counter_manager = counter_manager

    def __del__(self):
        pass

    def execute(self):
        self.counter_manager.reduceModifier("Creature")
