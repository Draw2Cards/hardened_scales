import unittest

from cards.hangarback_walker import CHangarbackWalker
from game import Game
from player import Player


class TestHangarbackWalker(unittest.TestCase):
    def test_1st_ability(self):
        game = Game()
        player = Player(game)
        p_hw = player.cast(CHangarbackWalker(game, 1))
        self.assertEqual(1, p_hw.getCountersCount("+1/+1"))

    def test_2nd_ability_part_1(self):
        game = Game()
        player = Player(game)
        p_hw = player.cast(CHangarbackWalker(game, 1))
        game.destroyCard(p_hw)
        self.assertEqual(["Token", "Creature", "Artifact", "Thopter"], game.zones.get("battlefield", [])[0].types)

    def test_2nd_ability_part_2(self):
        game = Game()
        player = Player(game)
        p_hw = player.cast(CHangarbackWalker(game, 2))
        game.destroyCard(p_hw)
        self.assertEqual(2, len(game.zones.get("battlefield", [])))

    def test_3th_ability_part_1(self):
        game = Game()
        player = Player(game)
        p_hw = player.cast(CHangarbackWalker(game, 1))
        player.active_ability(p_hw, 2)

        self.assertEqual(2, p_hw.getCountersCount("+1/+1"))

    def test_3th_ability_part_2(self):
        game = Game()
        player = Player(game)
        p_hw = player.cast(CHangarbackWalker(game, 1))
        player.active_ability(p_hw, 2)

        self.assertEqual(False, p_hw.untapped)

    def test_3th_ability_part_3(self):
        game = Game()
        player = Player(game)
        p_hw = player.cast(CHangarbackWalker(game, 1))
        player.addToManaPool("{C}")
        player.active_ability(p_hw, 2)

        self.assertEqual("", player.getManaPool())
