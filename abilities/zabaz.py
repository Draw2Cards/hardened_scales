from abc import ABC

from abilities.ability import StaticAbility


class AZabaz(StaticAbility, ABC):
    def __init__(self, game):
        StaticAbility.__init__(self)
        self.game = game

    def execute(self):
        self.game.a_modular_trig_mod += 1

    def revoke(self):
        self.game.a_modular_trig_mod -= 1
