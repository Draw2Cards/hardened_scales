import unittest

from cards.arcbound_worker import CArcboundWorker
from cards.power_depot import CPowerDepot
from game import Game
from player import Player


class TestPowerDepot(unittest.TestCase):
    def test_tapped_ability(self):
        game = Game()
        player = Player(game)
        pd = player.play(CPowerDepot(player, game))
        self.assertEqual(False, pd.untapped)

    def test_mana_ability_part_1(self):
        game = Game()
        player = Player(game)
        p_pd = player.play(CPowerDepot(player, game))
        p_pd.untap()
        player.active_ability(p_pd, 1)

        self.assertEqual(False, p_pd.untapped)

    def test_mana_ability_part_2(self):
        game = Game()
        player = Player(game)
        c_pd = CPowerDepot(player, game)
        p_pd = player.play(c_pd)
        p_pd.untap()
        player.active_ability(p_pd, 1)

        self.assertEqual("{C}", player.getManaPool())

    def test__modular_static_ability(self):
        game = Game()
        player = Player(game)
        pd = player.play(CPowerDepot(player, game))
        self.assertEqual(1, pd.getCountersCount("+1/+1"))

    def test__modular_trigger_ability(self):
        game = Game()
        player = Player(game)
        pd = player.play(CPowerDepot(player, game))
        aw = player.cast(CArcboundWorker(game))

        pd.abilities[2].abilities[1].set_target(aw)
        game.destroyCard(pd)

        self.assertEqual(2, aw.getCountersCount("+1/+1"))
