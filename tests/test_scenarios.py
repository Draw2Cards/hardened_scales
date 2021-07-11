import unittest

from cards.arcbound_ravager import CArcboundRavager
from cards.arcbound_worker import CArcboundWorker
from cards.forest import CForest
from cards.hardened_scales import CHardenedScales
from cards.inkmoth_nexus import CInkmothNexus
from cards.ozolith import COzolith
from cards.pendelhaven import CPendelhaven
from game import Game
from player import Player


class TestScenarios(unittest.TestCase):
    def test_scenario_1(self):
        game = Game()
        player = Player(game)
        player.cast(CHardenedScales(game))
        ar = player.cast(CArcboundRavager(game))
        aw = player.cast(CArcboundWorker(game))
        ph = player.play(CPendelhaven(player))
        fr = player.play(CForest(player))
        ink = player.play(CInkmothNexus(player))

        player.active_ability(fr, 0)
        player.active_ability(ink, 1)

        ph.abilities[1].set_target(ink)
        player.active_ability(ph, 1)

        ar.abilities[0].set_target(aw)
        aw.abilities[1].set_target(ar)
        player.active_ability(ar, 0)

        ar.abilities[0].set_target(ar)
        ar.abilities[2].set_target(ink)
        player.active_ability(ar, 0)
        self.assertEqual(8, ink.getCountersCount("+1/+1"))

    def test_scenario_2_a(self):
        game = Game()
        player = Player(game)

        ar = player.cast(CArcboundRavager(game))
        aw1 = player.cast(CArcboundWorker(game))
        aw2 = player.cast(CArcboundWorker(game))
        ph = player.play(CPendelhaven(player))
        fr = player.play(CForest(player))
        ink = player.play(CInkmothNexus(player))
        player.cast(CHardenedScales(game))

        player.active_ability(fr, 0)
        self.assertEqual("{G}", player.getManaPool())

        player.active_ability(ink, 1)
        self.assertEqual(["Land", "Artifact", "Creature"], ink.types)

        ph.abilities[1].set_target(ink)
        player.active_ability(ph, 1)
        self.assertEqual(2, ink.calc_power())

        ar.abilities[0].set_target(aw1)
        aw1.abilities[1].set_target(aw2)
        player.active_ability(ar, 0)
        #self.assertEqual(7, ar.getCountersCount("+1/+1"))

        ar.abilities[0].set_target(aw2)
        aw2.abilities[1].set_target(ar)
        player.active_ability(ar, 0)

        ar.abilities[0].set_target(ar)
        ar.abilities[2].set_target(ink)
        player.active_ability(ar, 0)
        self.assertEqual(10, ink.getCountersCount("+1/+1"))

    def test_scenario_2_b(self):
        game = Game()
        player = Player(game)

        ar = player.cast(CArcboundRavager(game))
        aw1 = player.cast(CArcboundWorker(game))
        aw2 = player.cast(CArcboundWorker(game))
        ph = player.play(CPendelhaven(player))
        fr = player.play(CForest(player))
        ink = player.play(CInkmothNexus(player))
        player.cast(CHardenedScales(game))

        player.active_ability(fr, 0)
        self.assertEqual("{G}", player.getManaPool())

        player.active_ability(ink, 1)
        self.assertEqual(["Land", "Artifact", "Creature"], ink.types)

        ph.abilities[1].set_target(ink)
        player.active_ability(ph, 1)
        self.assertEqual(2, ink.calc_power())

        ar.abilities[0].set_target(aw1)
        aw1.abilities[1].set_target(ar)
        player.active_ability(ar, 0)
        # self.assertEqual(7, ar.getCountersCount("+1/+1"))

        ar.abilities[0].set_target(aw2)
        aw2.abilities[1].set_target(ar)
        player.active_ability(ar, 0)

        ar.abilities[0].set_target(ar)
        ar.abilities[2].set_target(ink)
        player.active_ability(ar, 0)
        self.assertEqual(10, ink.getCountersCount("+1/+1"))

    def test_scenario_3(self):
        game = Game()
        player = Player(game)

        oz = player.cast(COzolith(game))
        ar = player.cast(CArcboundRavager(game))
        aw = player.cast(CArcboundWorker(game))
        ph = player.play(CPendelhaven(player))
        fr = player.play(CForest(player))
        ink = player.play(CInkmothNexus(player))
        player.cast(CHardenedScales(game))

        player.active_ability(fr, 0)
        player.active_ability(ink, 1)

        ph.abilities[1].set_target(ink)
        player.active_ability(ph, 1)

        ar.abilities[0].set_target(aw)
        aw.abilities[1].set_target(ar)
        player.active_ability(ar, 0)

        ar.abilities[0].set_target(ar)
        ar.abilities[2].set_target(ink)
        player.active_ability(ar, 0)

        oz.abilities[0].abilities[1].set_target(ink)
        game.combat()

        self.assertEqual(13, ink.getCountersCount("+1/+1"))
