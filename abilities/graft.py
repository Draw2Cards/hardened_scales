from abc import ABC

from abilities.ability import StaticAbility, Ability, TriggeredAbility


class AGraft(Ability, ABC):
    def __init__(self, card, value, game):
        Ability.__init__(self)
        self.abilities = [AGraftStatic(card, value, game), AGraftTriggered(card, game)]


class AGraftStatic(StaticAbility, ABC):
    def __init__(self, card, value, game):
        StaticAbility.__init__(self)
        self.card = card
        self.value = value
        self.game = game

    def execute(self):
        self.game.counter_mgr.addCounters(self.card, "+1/+1", self.value)


class AGraftTriggered(TriggeredAbility, ABC):
    def __init__(self, card, game):
        TriggeredAbility.__init__(self)
        self.card = card
        self.target = None
        self.game = game

    def set_target(self, card):
        self.target = card

    def execute(self):
        if self.card.getCountersCount("+1/+1") > 0:
            self.game.counter_mgr.removeCounters(self.card, "+1/+1", 1)
            self.game.counter_mgr.addCounters(self.target, "+1/+1", 1)
