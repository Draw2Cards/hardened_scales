import unittest

from cards.arcbound_ravager import CArcboundRavager
from cards.hardened_scales import CHardenedScales
from cards.ozolith import COzolith
from game import Game
from player import Player


class TestArcboundRavager(unittest.TestCase):
    def test__modular_static_ability(self):
        game = Game()
        player = Player(game)
        ar = player.cast(CArcboundRavager(game))
        self.assertEqual(1, ar.getCountersCount("+1/+1"))

    def test__modular_trigger_ability(self):
        game = Game()
        player = Player(game)
        ar1 = player.cast(CArcboundRavager(game))
        ar2 = player.cast(CArcboundRavager(game))

        ar1.abilities[2].set_target(ar2)
        game.destroyCard(ar1)

        self.assertEqual(2, ar2.getCountersCount("+1/+1"))

    def test__modular_trigger_ability_with_additional_counter(self):
        game = Game()
        player = Player(game)
        ar1 = player.cast(CArcboundRavager(game))
        ar2 = player.cast(CArcboundRavager(game))

        game.counter_mgr.addCounters(ar1, "+1/+1", 1)

        ar1.abilities[2].set_target(ar2)
        game.destroyCard(ar1)

        self.assertEqual(3, ar2.getCountersCount("+1/+1"))

    def test_ravager_ability_part_1(self):
        game = Game()
        player = Player(game)
        ar1 = player.cast(CArcboundRavager(game))
        ar2 = player.cast(CArcboundRavager(game))

        ar1.abilities[0].set_target(ar2)
        ar2.abilities[2].set_target(ar1)
        player.active_ability(ar1, 0)

        self.assertEqual(3, ar1.getCountersCount("+1/+1"))

    def test_ravager_ability_part_2(self):
        game = Game()
        player = Player(game)
        player.cast(CHardenedScales(game))
        ar1 = player.cast(CArcboundRavager(game))
        ar2 = player.cast(CArcboundRavager(game))

        ar1.abilities[0].set_target(ar2)
        ar2.abilities[2].set_target(ar1)
        player.active_ability(ar1, 0)

        self.assertEqual(7, ar1.getCountersCount("+1/+1"))

    def test_ravager_ability_part_3(self):
        game = Game()
        player = Player(game)
        player.cast(CHardenedScales(game))
        oz = player.cast(COzolith(game))
        ar1 = player.cast(CArcboundRavager(game))
        ar2 = player.cast(CArcboundRavager(game))

        ar1.abilities[0].set_target(ar2)
        ar2.abilities[2].set_target(ar1)
        player.active_ability(ar1, 0)
        oz.abilities[0].abilities[1].set_target(ar1)
        game.combat()

        self.assertEqual(10, ar1.getCountersCount("+1/+1"))