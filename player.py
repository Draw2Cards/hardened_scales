from abilities.ability import StaticAbility
from objects.permanent import Permanent


class Player:
    def __init__(self, game):
        self.life = 20
        self.counters = {}
        self.mana_pool = {}
        self.game = game

    def cast(self, obj):  # TODO to refactor
        per = Permanent(obj)
        for a in per.abilities:
            if isinstance(a, StaticAbility):
                a.execute()
            else:
                for sa in a.abilities:
                    if isinstance(sa, StaticAbility):
                        sa.execute()
        return per

    def play(self, obj):  # TODO to refactor
        permanent = Permanent(obj)
        for a in permanent.abilities:
            if isinstance(a, StaticAbility):
                a.execute()
            else:
                for sa in a.abilities:
                    if isinstance(sa, StaticAbility):
                        sa.execute()
        return permanent

    def addToManaPool(self, mana):
        if mana == "{4}":
            if "{C}" in self.mana_pool:
                self.mana_pool["{C}"] += 4
            else:
                self.mana_pool.setdefault("{C}", 4)
        elif mana in self.mana_pool:
            self.mana_pool[mana] += 1
        else:
            self.mana_pool.setdefault(mana, 1)

    def remove_from_mana_pool(self, mana):
        value = self.mana_pool.get(mana, 0)
        if value > 0:
            self.mana_pool[mana] -= 1

    def getManaPool(self):
        result = ""
        for c in self.mana_pool:
            for _ in range(self.mana_pool[c]):
                result += c
        return result

    def active_ability(self, source, ability_id):
        self.pay(source.abilities[ability_id].cost, source, ability_id)
        source.abilities[ability_id].activate(source)

    def pay(self, cost, resource, ability_id):
        for c in cost:
            if c == "{T}":
                resource.tap()
            elif c == "{1}":
                self.remove_from_mana_pool("{C}")
            elif c == "{4}":
                self.remove_from_mana_pool("{C}")
                self.remove_from_mana_pool("{C}")
                self.remove_from_mana_pool("{C}")
                self.remove_from_mana_pool("{C}")
            elif c == "counter":
                if resource.abilities[ability_id].permanent:
                    self.game.counter_mgr.removeCounters(resource.abilities[ability_id].permanent, "+1/+1", 1)
                else:
                    self.game.counter_mgr.removeCounters(resource, "+1/+1", 1)
            elif c == "sac":

                self.game.destroyCard(resource.abilities[ability_id].target)
            else:
                raise NotImplementedError
