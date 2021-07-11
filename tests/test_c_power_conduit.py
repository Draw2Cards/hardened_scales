import unittest

from cards.arcbound_worker import CArcboundWorker
from cards.power_conduit import CPowerConduit
from game import Game
from player import Player


class TestPowerConduit(unittest.TestCase):
    def test_ability_1st_mode_part_1(self):
        game = Game()
        player = Player(game)
        pc = player.cast(CPowerConduit(game))
        aw1 = player.cast(CArcboundWorker(game))
        aw2 = player.cast(CArcboundWorker(game))
        pc.abilities[0].set_permanent(aw1)
        pc.abilities[0].set_target(aw2)
        player.active_ability(pc, 0)

        self.assertEqual(False, pc.untapped)

    def test_ability_1st_mode_part_2(self):
        game = Game()
        player = Player(game)
        pc = player.cast(CPowerConduit(game))
        aw1 = player.cast(CArcboundWorker(game))
        aw2 = player.cast(CArcboundWorker(game))
        pc.abilities[0].set_permanent(aw1)
        pc.abilities[0].set_target(aw2)
        player.active_ability(pc, 0)

        self.assertEqual(0, aw1.getCountersCount("+1/+1"))

    def test_ability_1st_mode_part_3(self):
        game = Game()
        player = Player(game)
        pc = player.cast(CPowerConduit(game))
        aw1 = player.cast(CArcboundWorker(game))
        aw2 = player.cast(CArcboundWorker(game))
        pc.abilities[0].set_permanent(aw1)
        pc.abilities[0].set_target(aw2)
        player.active_ability(pc, 0)

        self.assertEqual(2, aw2.getCountersCount("+1/+1"))
