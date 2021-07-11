from abc import ABC

from abilities.ability import TriggeredAbility
from tokens.thopter import TThopter


class AHangarbackWalker(TriggeredAbility, ABC):
    def __init__(self, card, game):
        TriggeredAbility.__init__(self)
        self.triggered_on = "Destroy"
        self.card = card
        self.game = game

    def execute(self):
        value = self.card.getCountersCount("+1/+1")
        self.game.create_tokens(TThopter(), value)
