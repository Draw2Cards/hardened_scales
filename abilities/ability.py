from abc import ABC


class Ability:
    def __init__(self):
        self.abilities = []

    def execute(self):
        raise NotImplementedError


class StaticAbility(Ability, ABC):
    def __init__(self):
        Ability.__init__(self)

    def revoke(self):
        pass


class TriggeredAbility(Ability, ABC):
    def __init__(self):
        Ability.__init__(self)
        self.triggered_on = ""

    def isTriggeredOn(self, trigger):
        return self.triggered_on == trigger


class ActivatedAbility(Ability, ABC):
    def __init__(self):
        Ability.__init__(self)

    def activate(self, source):
        raise NotImplementedError


class AMana(ActivatedAbility, ABC):
    def __init__(self, cost, mana, player):
        ActivatedAbility.__init__(self)
        self.cost = cost  # TODO member not used
        self.mana = mana
        self.player = player

    def activate(self, source):
        self.player.addToManaPool(self.mana)


class ATapped(StaticAbility, ABC):
    def __init__(self, card):
        StaticAbility.__init__(self)
        self.card = card

    def execute(self):
        self.card.untapped = False


class AOzolith(Ability, ABC):
    def __init__(self, game, card):
        Ability.__init__(self)
        self.abilities = [AOzStatic(game, card), AOzTriggered(game, card)]


class AOzStatic(StaticAbility, ABC):
    def __init__(self, game, card):
        StaticAbility.__init__(self)
        self.game = game
        self.card = card

    def execute(self):
        self.game.addAbilityOnDestroy(self.copyCountersFromCreature)

    def copyCountersFromCreature(self, card):
        if card.isTypes("Creature"):
            counters_count = card.getCountersCount("+1/+1")  # TODO copy every type of counter
            self.game.counter_mgr.addCounters(self.card, "+1/+1", counters_count)  # TODO copy every type of counter


class AOzTriggered(StaticAbility, ABC):
    def __init__(self, game, card):
        StaticAbility.__init__(self)
        self.game = game
        self.card = card
        self.triggered_on = "Combat"
        self.legal_target = "Creature"
        self.target_card = None

    def execute(self):
        self.game.addAbilityOnCombat(self.onCombat)

    def onCombat(self):
        if self.card.getCountersCount("+1/+1") > 0:
            if self.isLegalTarget():
                self._moveCounters()

    def _moveCounters(self):
        counters_removed = self.game.counter_mgr.removeCounters(self.card, "+1/+1", -1)
        self.game.counter_mgr.addCounters(self.target_card, "+1/+1", counters_removed)

    def set_target(self, card):
        self.target_card = card

    def isLegalTarget(self):
        return self.target_card.isTypes(self.legal_target)


class AEntersWithCounters(StaticAbility, ABC):
    def __init__(self, card, game, value, counter):
        StaticAbility.__init__(self)
        self.card = card
        self.game = game
        self.value = value
        self.counter = counter

    def execute(self):
        self.game.counter_mgr.addCounters(self.card, self.counter, self.value)


class APutCounter(ActivatedAbility, ABC):
    def __init__(self, cost, counter, card, game):
        ActivatedAbility.__init__(self)
        self.cost = cost  # TODO member not used
        self.counter = counter
        self.card = card
        self.game = game
        self.target = None

    def set_target(self, target):
        self.target = target

    def activate(self, source):
        self.game.counter_mgr.addCounters(self.card, self.counter, 1)


class AFlying(StaticAbility, ABC):
    def __init__(self):
        StaticAbility.__init__(self)

    def execute(self):
        pass


class AInfect(StaticAbility, ABC):
    def __init__(self):
        StaticAbility.__init__(self)

    def execute(self):
        pass
