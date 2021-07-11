from abc import ABC

from abilities.ability import AOzolith
from objects.spell import Spell


class COzolith(Spell, ABC):
    def __init__(self, game):
        Spell.__init__(self)
        self.mana_cost = "{1}"
        self.cmc = 1
        self.types = ["Legendary", "Artifact"]
        self.colors = []

        self.abilities = [AOzolith(game, self)]
