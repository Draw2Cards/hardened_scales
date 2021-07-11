import unittest

from cards.arcbound_worker import CArcboundWorker
from game import Game
from player import Player


class TestArcboundWorker(unittest.TestCase):
    def test__modular_static_ability(self):
        game = Game()
        player = Player(game)
        p_aw = player.cast(CArcboundWorker(game))
        self.assertEqual(1, p_aw.getCountersCount("+1/+1"))

    def test__modular_trigger_ability(self):
        game = Game()
        player = Player(game)
        c_aw = CArcboundWorker(game)
        p_aw1 = player.cast(c_aw)
        p_aw2 = player.cast(c_aw)

        p_aw1.abilities[1].set_target(p_aw2)
        game.destroyCard(p_aw1)

        self.assertEqual(2, p_aw2.getCountersCount("+1/+1"))

    def test__modular_trigger_ability_with_additional_counter(self):
        game = Game()
        player = Player(game)
        p_aw1 = player.cast(CArcboundWorker(game))
        p_aw2 = player.cast(CArcboundWorker(game))

        game.counter_mgr.addCounters(p_aw1, "+1/+1", 1)

        p_aw1.abilities[1].set_target(p_aw2)
        game.destroyCard(p_aw1)

        self.assertEqual(3, p_aw2.getCountersCount("+1/+1"))
