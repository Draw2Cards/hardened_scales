class CounterManager:
    def __init__(self):
        self.modifiers = {}

    def getModifier(self, card):
        for t in card.getTypes():
            if t in self.modifiers:
                return self.modifiers[t]
        else:
            return 0

    def addCounters(self, permanent, counter_name, counter_count):
        before_add = permanent.counters.get(counter_name, 0)
        permanent.counters.update({counter_name: before_add + counter_count + self.getModifier(permanent)})

    def removeCounters(self, permanent, counter_name, counters_to_remove):
        counters_removed = 0
        before_remove = permanent.counters.get(counter_name, 0)
        if before_remove > 0:
            if counters_to_remove == -1:
                permanent.counters.update({counter_name: 0})
                counters_removed = before_remove
            else:
                if counters_to_remove >= before_remove:
                    permanent.counters.update({counter_name: 0})
                    counters_removed = before_remove
                else:
                    permanent.counters.update({counter_name: before_remove - counters_to_remove})
                    counters_removed = counters_to_remove
        return counters_removed

    def raiseModifier(self, card_type):
        before_add = self.modifiers.get(card_type, 0)
        self.modifiers.update({card_type: before_add + 1})

    def reduceModifier(self, card_type):
        before_add = self.modifiers.get(card_type, 0)
        if before_add > 0:
            self.modifiers.update({card_type: before_add - 1})
