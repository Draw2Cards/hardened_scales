from abc import ABC


class Effect:
    def __init__(self):
        pass


class EContinuous(Effect, ABC):
    def __init__(self):
        Effect.__init__(self)


class EReplacement(EContinuous, ABC):
    def __init__(self):
        EContinuous.__init__(self)
