from abc import ABC

from abilities.ability import AFlying
from tokens.token import Token


class TThopter(Token, ABC):
    def __init__(self):
        Token.__init__(self)
        self.mana_cost = ""
        self.cmc = 0
        self.types = ["Token", "Creature", "Artifact", "Thopter"]
        self.power = 1
        self.toughness = 1
        self.colors = []
        self.abilities = [AFlying]
