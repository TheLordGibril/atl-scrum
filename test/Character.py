import random
import sys
import unittest

from src.Character import Character


class MyTestCase(unittest.TestCase):
    def test_character_receive_damage(self):
        damage = 5
        player = Character()
        player.receive_damage(damage)
        self.assertEqual(player.max_hp - damage, player.hp)

    def test_character_receive_fatal_damage(self):
        fatal_damage = sys.maxsize
        player = Character()
        player.receive_damage(fatal_damage)
        self.assertEqual(0, player.hp)
        self.assertTrue(player.is_dead)

    def test_character_receive_fumble_damage(self):
        fumble_damage = random.randint(1, 25)
        player1 = Character(fumble_chance=100, fumble_damage=fumble_damage)
        player2 = Character()
        player1.attack(player2)
        self.assertEqual(player1.max_hp - fumble_damage, player1.hp)

    def test_character_attack_critical(self):
        attack = random.randint(1, 25)
        player1 = Character(fumble_chance=0, critical_chance=100, min_damage=attack, max_damage=attack)
        player2 = Character()
        player1.attack(player2)
        self.assertEqual(player2.max_hp - (attack*2), player2.hp)

    def test_character_attack(self):
        attack = random.randint(1, 50)
        player1 = Character(fumble_chance=0, critical_chance=0, min_damage=attack, max_damage=attack)
        player2 = Character()
        player1.attack(player2)
        self.assertEqual(player2.max_hp - attack, player2.hp)

    def test_character_dead_attack(self):
        player1 = Character()
        player2 = Character()
        player1.die()
        player1.attack(player2)
        self.assertEqual(player2.max_hp, player2.hp)

if __name__ == '__main__':
    unittest.main()
