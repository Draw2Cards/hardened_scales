import unittest

from cards.arcbound_worker import CArcboundWorker
from cards.hardened_scales import CHardenedScales
from cards.ozolith import COzolith
from game import Game
from player import Player


class TestOzolith(unittest.TestCase):
    def test_move_counters_on_creature_destroy(self):
        game = Game()
        player = Player(game)
        oz = player.cast(COzolith(game))
        aw = player.cast(CArcboundWorker(game))
        game.destroyCard(aw)

        self.assertEqual(1, oz.getCountersCount("+1/+1"))

    def test_move_counters_on_combat_part_1(self):
        game = Game()
        player = Player(game)
        oz = player.cast(COzolith(game))
        aw = player.cast(CArcboundWorker(game))
        game.counter_mgr.addCounters(oz, "+1/+1", 1)
        oz.abilities[0].abilities[1].set_target(aw)
        game.combat()

        self.assertEqual(2, aw.getCountersCount("+1/+1"))

    def test_move_counters_on_combat_part_2(self):
        game = Game()
        player = Player(game)
        oz = player.cast(COzolith(game))
        aw = player.cast(CArcboundWorker(game))
        game.counter_mgr.addCounters(oz, "+1/+1", 1)

        oz.abilities[0].abilities[1].set_target(aw)
        game.combat()

        self.assertEqual(0, oz.getCountersCount("+1/+1"))

    def test_move_counters_on_combat_with_hs(self):
        game = Game()
        player = Player(game)
        oz = player.cast(COzolith(game))
        game.counter_mgr.addCounters(oz, "+1/+1", 1)
        player.cast(CHardenedScales(game))
        aw = player.cast(CArcboundWorker(game))

        oz.abilities[0].abilities[1].set_target(aw)
        game.combat()

        self.assertEqual(4, aw.getCountersCount("+1/+1"))
