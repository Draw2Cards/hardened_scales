from abc import ABC

from abilities.ability import Ability, StaticAbility, TriggeredAbility


class AModular(Ability, ABC):
    def __init__(self, card, game, number):
        Ability.__init__(self)
        self.abilities = [AModularStatic(card, game, number), AModularTriggered(card, number, game)]


class AModularStatic(StaticAbility, ABC):
    def __init__(self, card, game, number):
        self.number = number
        self.game = game
        self.card = card
        StaticAbility.__init__(self)

    def execute(self):
        self.game.counter_mgr.addCounters(self.card, "+1/+1", self.number)


class AModularTriggered(TriggeredAbility, ABC):
    def __init__(self, card, number, game):
        TriggeredAbility.__init__(self)
        self.number = number
        self.triggered_on = "Destroy"
        self.target_card = None
        self.legal_target = ["Artifact", "Creature"]
        self.card = card
        self.game = game

    def execute(self):
        if self.target_card:
            if self.isLegalTarget(self.target_card):
                self.game.counter_mgr.addCounters(
                    self.target_card, "+1/+1", self.card.getCountersCount("+1/+1") + self.game.a_modular_trig_mod)

    def isLegalTarget(self, card):
        return card.isTypes(self.legal_target)

    def set_target(self, card):
        self.target_card = card
