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

if __name__ == '__main__':
    unittest.main()
