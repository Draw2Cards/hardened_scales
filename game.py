from managers.counter_manager import CounterManager
from tokens.thopter import TThopter


class Game:
    def __init__(self):
        self.counter_mgr = CounterManager()
        self.ability_on_destroy = None
        self.ability_on_combat = None
        self.a_modular_trig_mod = 0
        self.zones = {}

    def destroyCard(self, card):
        card.onDestroy()
        if self.ability_on_destroy is not None:
            self.ability_on_destroy(card)

    def addAbilityOnDestroy(self, ability):
        self.ability_on_destroy = ability

    def combat(self):
        if self.ability_on_combat is not None:
            self.ability_on_combat()

    def addAbilityOnCombat(self, ability):
        self.ability_on_combat = ability

    def create_tokens(self, token, value):
        self.zones.setdefault("battlefield", []).extend([TThopter()] * value)
