from abc import ABC

from abilities.ability import ActivatedAbility


class APendelhaven(ActivatedAbility, ABC):
    def __init__(self, cost):
        ActivatedAbility.__init__(self)
        self.cost = cost
        self.target = None

    def activate(self, source):
        self.target.set_modifier([1, 2])

    def set_target(self, target):
        self.target = target
