from abc import ABC

from abilities.ability import ActivatedAbility, AFlying, AInfect


class AInkmothNexus(ActivatedAbility, ABC):
    def __init__(self, cost, card):
        ActivatedAbility.__init__(self)
        self.cost = cost
        self.target = self
        self.card = card

    def activate(self, source):
        source.mana_cost = ""
        source.cmc = 0
        source.types = ["Land", "Artifact", "Creature"]
        source.base_power = 1
        source.base_toughness = 1
        source.colors = []
        source.abilities = [AFlying(), AInfect()]
