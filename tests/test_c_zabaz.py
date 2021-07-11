import unittest

from cards.arcbound_worker import CArcboundWorker
from cards.zabaz import CZabaz
from game import Game
from player import Player


class TestZabaz(unittest.TestCase):
    def test__zabaz_modular_static(self):
        game = Game()
        player = Player(game)
        zabaz = player.cast(CZabaz(game))
        self.assertEqual(1, zabaz.getCountersCount("+1/+1"))

    def test__zabaz_modular_trigger(self):
        game = Game()
        player = Player(game)
        zabaz = player.cast(CZabaz(game))
        aw = player.cast(CArcboundWorker(game))

        zabaz.abilities[0].abilities[1].set_target(aw)
        game.destroyCard(zabaz)

        self.assertEqual(2, aw.getCountersCount("+1/+1"))

    def test__zabaz_continuous_effect(self):
        game = Game()
        player = Player(game)
        zabaz = player.cast(CZabaz(game))
        aw = player.cast(CArcboundWorker(game))

        aw.abilities[1].set_target(zabaz)
        game.destroyCard(aw)

        self.assertEqual(3, zabaz.getCountersCount("+1/+1"))

    def test__zabaz_continuous_effect_after_zabaz_is_destroyed(self):
        game = Game()
        player = Player(game)
        zabaz = player.cast(CZabaz(game))
        aw = player.cast(CArcboundWorker(game))

        zabaz.abilities[0].abilities[1].set_target(aw)
        game.destroyCard(zabaz)

        self.assertEqual(2, aw.getCountersCount("+1/+1"))
