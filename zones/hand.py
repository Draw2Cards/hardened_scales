from abc import ABC

from zones.zone import Zone


class ZHand(Zone, ABC):
    def __init__(self):
        Zone.__init__(self)
        self.cards = []
