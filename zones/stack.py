from abc import ABC

from zones.zone import Zone


class ZStack(Zone, list, ABC):
    def __init__(self):
        Zone.__init__(self)
        list.__init__(self)

    def push(self, value):
        self.append(value)
