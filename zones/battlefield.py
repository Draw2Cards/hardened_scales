from abc import ABC

from zones.zone import Zone


class ZBattlefield(Zone, ABC):
    def __init__(self):
        Zone.__init__(self)
        self.permanents = []
