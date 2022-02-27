import unittest
import game_manager

class TestGameManager(unittest.TestCase):
    def setUp(self):                                                                                    # This function will create a new instance of scoreboard for different test function below
        self.manager = game_manager.GameManager(10)                                                     # Set up an instance where max score == 10
    
    def test_valid_max_score(self):
        self.assertRaises(TypeError, lambda: game_manager.GameManager("2"))                             # Test for non-integer input
        self.assertEqual(10, self.manager.max_score)                                                    # Test if max score is set to 10
        self.assertNotEqual(5, self.manager.max_score)                                                  # Test to ensure max score is set correctly

    def test_determine_winner(self):
        self.assertRaises(ValueError, lambda: self.manager.determine_winner("random", "hoho"))          # Test for both invalid input
        self.assertRaises(ValueError, lambda: self.manager.determine_winner("random", "Paper"))         # Test for user_input to be invalid
        self.assertRaises(ValueError, lambda: self.manager.determine_winner("Stone", "random"))         # Test for computer_input to be invalid
        self.assertRaises(Exception, lambda: self.manager.determine_winner(1, 2))                       # Test for wrong input type
        self.assertEqual("TIE", self.manager.determine_winner("Rock","Rock"))                           # Test for TIE conditions
        self.assertEqual("WIN", self.manager.determine_winner("Rock","Scissor"))                        # Test for WIN conditions
        self.assertEqual("LOSE", self.manager.determine_winner("Rock","Paper"))                         # Test for LOSE conditions

    def test_game_end(self):
        self.assertTrue(self.manager.game_end(10))                                                      # Test if game will end when max score reach 10
        self.assertFalse(self.manager.game_end(5))                                                      # Test if game will not end when score is 5 < 10(end score)
        self.assertRaises(ValueError, lambda: self.manager.game_end(15))                                # Test for invalid input
        self.assertRaises(TypeError, lambda: self.manager.game_end("15"))                               # Test for invalid input