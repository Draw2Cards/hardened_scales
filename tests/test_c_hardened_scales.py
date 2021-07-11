import unittest

from cards.arcbound_worker import CArcboundWorker
from cards.hardened_scales import CHardenedScales
from game import Game
from player import Player


class TestHardenedScales(unittest.TestCase):
    def test__add_counter(self):
        game = Game()
        player = Player(game)

        p_aw = player.cast(CArcboundWorker(game))
        player.cast(CHardenedScales(game))

        game.counter_mgr.addCounters(p_aw, "+1/+1", 1)

        self.assertEqual(3, p_aw.getCountersCount("+1/+1"))

    def test__add_counter_after_hs_destroy(self):
        game = Game()
        player = Player(game)

        p_aw = player.cast(CArcboundWorker(game))
        p_hs = player.cast(CHardenedScales(game))

        game.destroyCard(p_hs)
        game.counter_mgr.addCounters(p_aw, "+1/+1", 1)

        self.assertEqual(2, p_aw.getCountersCount("+1/+1"))
