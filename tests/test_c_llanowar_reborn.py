import unittest

from cards.arcbound_worker import CArcboundWorker
from cards.hardened_scales import CHardenedScales
from cards.llanowar_reborn import CLlanowarReborn

from game import Game
from player import Player


class TestLlanowarReborn(unittest.TestCase):
    def test_enters_the_battlefield_tapped(self):
        game = Game()
        player = Player(game)
        p_pr = player.play(CLlanowarReborn(player, game))
        self.assertEqual(False, p_pr.untapped)

    def test_mana_ability_part_1(self):
        game = Game()
        player = Player(game)
        c_lr = CLlanowarReborn(player, game)
        p_lr = player.play(c_lr)

        p_lr.untap()
        player.active_ability(p_lr, 1)

        self.assertEqual(False, p_lr.untapped)

    def test_mana_ability_part_2(self):
        game = Game()
        player = Player(game)
        c_lr = CLlanowarReborn(player, game)
        p_lr = player.play(c_lr)
        p_lr.untap()

        player.active_ability(p_lr, 1)

        self.assertEqual("{G}", player.getManaPool())

    def test_graft_static_ability(self):
        game = Game()
        player = Player(game)
        lr = player.play(CLlanowarReborn(player, game))
        self.assertEqual(1, lr.getCountersCount("+1/+1"))

    def test_graft_triggered_ability_part_1(self):
        game = Game()
        player = Player(game)
        p_lr = player.play(CLlanowarReborn(player, game))
        p_aw = player.cast(CArcboundWorker(game))

        p_lr.abilities[2].abilities[1].set_target(p_aw)
        p_lr.abilities[2].abilities[1].execute()

        self.assertEqual(2, p_aw.getCountersCount("+1/+1"))

    def test_graft_triggered_ability_part_2(self):
        game = Game()
        player = Player(game)
        lr = CLlanowarReborn(player, game)
        player.play(lr)

        aw = CArcboundWorker(game)
        player.cast(aw)

        lr.abilities[2].abilities[1].set_target(aw)
        lr.abilities[2].abilities[1].execute()

        self.assertEqual(0, lr.getCountersCount("+1/+1"))

    def test_hardened_scales_interaction_part_1(self):
        game = Game()
        player = Player(game)
        hs = CHardenedScales(game)
        player.cast(hs)
        lr = player.play(CLlanowarReborn(player, game))
        self.assertEqual(1, lr.getCountersCount("+1/+1"))

    def test_hardened_scales_interaction_part_2(self):
        game = Game()
        player = Player(game)

        lr = player.play(CLlanowarReborn(player, game))
        player.cast(CHardenedScales(game))
        aw = player.cast(CArcboundWorker(game))

        lr.abilities[2].abilities[1].set_target(aw)
        lr.abilities[2].abilities[1].execute()

        self.assertEqual(4, aw.getCountersCount("+1/+1"))
