import unittest

from cards.inkmoth_nexus import CInkmothNexus
from game import Game
from player import Player


class TestInkmothNexus(unittest.TestCase):
    def test_1st_ability_part_1(self):
        game = Game()
        player = Player(game)
        p_in = player.play(CInkmothNexus(player))
        player.active_ability(p_in, 0)

        self.assertEqual("{C}", player.getManaPool())

    def test_2nd_ability_part_1(self):
        game = Game()
        player = Player(game)
        p_in = player.play(CInkmothNexus(player))
        player.addToManaPool("{C}")
        player.active_ability(p_in, 1)

        self.assertEqual("", player.getManaPool())

    def test_2nd_ability_part_2(self):
        game = Game()
        player = Player(game)
        p_in = player.play(CInkmothNexus(player))
        player.addToManaPool("{C}")
        player.active_ability(p_in, 1)

        self.assertEqual(["Land", "Artifact", "Creature"], p_in.types)
