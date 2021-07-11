from abc import ABC

from abilities.ability import ActivatedAbility


class APowerConduit(ActivatedAbility, ABC):
    def __init__(self, cost, counter, card, game):
        ActivatedAbility.__init__(self)
        self.cost = cost  # TODO member not used
        self.counter = counter
        self.card = card
        self.game = game
        self.permanent = None
        self.target = None

    def activate(self, source):
        self.game.counter_mgr.addCounters(self.target, self.counter, 1)

    def set_target(self, target):
        self.target = target

    def set_permanent(self, permanent):
        self.permanent = permanent
