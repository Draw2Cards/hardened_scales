import unittest

from cards.walking_ballista import CWalkingBallista
from game import Game
from player import Player


class TestWalkingBallista(unittest.TestCase):
    def test_1st_ability(self):
        game = Game()
        player = Player(game)
        wb = player.cast(CWalkingBallista(game, 1))
        self.assertEqual(1, wb.getCountersCount("+1/+1"))

    def test_2nd_ability_part_1(self):
        game = Game()
        player = Player(game)
        wb = player.cast(CWalkingBallista(game, 1))
        player.addToManaPool("{4}")
        player.active_ability(wb, 1)
        self.assertEqual(2, wb.getCountersCount("+1/+1"))

    def test_2nd_ability_part_2(self):
        game = Game()
        player = Player(game)
        wb = player.cast(CWalkingBallista(game, 1))
        player.addToManaPool("{4}")
        player.active_ability(wb, 1)
        self.assertEqual("", player.getManaPool())

    def test_3th_ability_part_1(self):
        game = Game()
        player = Player(game)
        player2 = Player(game)
        wb = player.cast(CWalkingBallista(game, 1))
        wb.abilities[2].set_target(player2)
        player.active_ability(wb, 2)
        self.assertEqual(0, wb.getCountersCount("+1/+1"))

    def test_3th_ability_part_2(self):
        game = Game()
        player1 = Player(game)
        player2 = Player(game)
        wb = player1.cast(CWalkingBallista(game, 1))
        wb.abilities[2].set_target(player2)
        player1.active_ability(wb, 2)
        self.assertEqual(19, player2.life)
