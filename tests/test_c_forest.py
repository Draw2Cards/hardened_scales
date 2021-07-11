import unittest

from cards.forest import CForest
from game import Game
from player import Player


class TestForest(unittest.TestCase):
    def test_1st_ability_part_1(self):
        game = Game()
        player = Player(game)
        p_fr = player.play(CForest(player))
        player.active_ability(p_fr, 0)

        self.assertEqual("{G}", player.getManaPool())
