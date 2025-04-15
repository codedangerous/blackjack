import unittest
from player import Player

class Tests(unittest.TestCase):
    def test_player_name_string(self):
        player = Player()
        player.set_name("Testy McTesterson")
        expected = "Testy McTesterson"
        self.assertEqual(player.get_name(), expected)
    
    def test_player_name_int(self):
        with self.assertRaises(ValueError):
            player = Player()
            player.set_name(1)
    
    def test_player_name_float(self):
        with self.assertRaises(ValueError):
            player = Player()
            player.set_name(1.2)
    
    def test_player_name_bool(self):
        with self.assertRaises(ValueError):
            player = Player()
            player.set_name(False)

    
    def test_player_name_rename(self):
        with self.assertRaises(ValueError):
            player = Player()
            player.set_name("Cody")
            player.set_name("Amanda")