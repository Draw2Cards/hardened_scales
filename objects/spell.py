from abc import ABC

from objects.card import Card


class Spell(Card, ABC):
    def __init__(self, c_spell=None):
        Card.__init__(self)
        if c_spell:
            self.abilities = c_spell.abilities
            self.counters = c_spell.counters
            self.supertypes = c_spell.supertypes
            self.types = c_spell.types
            self.subtypes = c_spell.subtypes
            self.game = c_spell.game
