import unittest

from cards.arcbound_worker import CArcboundWorker
from cards.pendelhaven import CPendelhaven
from game import Game
from player import Player


class TestPendelhaven(unittest.TestCase):
    def test_1st_ability_part_1(self):
        game = Game()
        player = Player(game)
        p_ph = player.play(CPendelhaven(player))
        player.active_ability(p_ph, 0)

        self.assertEqual("{G}", player.getManaPool())

    def test_1st_ability_part_2(self):
        game = Game()
        player = Player(game)
        p_ph = player.play(CPendelhaven(player))
        player.active_ability(p_ph, 0)

        self.assertEqual(False, p_ph.untapped)

    def test_2nd_ability_part_1(self):
        game = Game()
        player = Player(game)
        p_ph = player.play(CPendelhaven(player))
        p_aw = player.play(CArcboundWorker(game))

        p_ph.abilities[1].set_target(p_aw)
        player.active_ability(p_ph, 1)

        self.assertEqual(2, p_aw.calc_power())

    def test_2nd_ability_part_2(self):
        game = Game()
        player = Player(game)
        p_ph = player.play(CPendelhaven(player))
        p_aw = player.play(CArcboundWorker(game))

        p_ph.abilities[1].set_target(p_aw)
        player.active_ability(p_ph, 1)

        self.assertEqual(3, p_aw.calc_toughness())

    def test_2nd_ability_part_3(self):
        game = Game()
        player = Player(game)
        p_ph = player.play(CPendelhaven(player))
        p_aw = player.play(CArcboundWorker(game))

        p_ph.abilities[1].set_target(p_aw)
        player.active_ability(p_ph, 1)

        self.assertEqual(False, p_ph.untapped)
