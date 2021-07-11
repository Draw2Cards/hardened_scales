from abc import ABC

from abilities.ability import ActivatedAbility


class AWalkingBallista(ActivatedAbility, ABC):
    def __init__(self, cost, card, game):
        ActivatedAbility.__init__(self)
        self.cost = cost  # TODO member not used
        self.card = card
        self.game = game
        self.target = None
        self.permanent = None

    def activate(self, source):
        self.card.deal_dmg(1, self.target)

    def set_target(self, target):
        self.target = target
