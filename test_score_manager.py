import unittest
import score_manager

class TestScoreManager(unittest.TestCase):
    def setUp(self):                                                                        # This function will create a new instance of scoreboard for different test function below
        self.scoreboard = score_manager.ScoreManager()

    def test_initial_score(self):
        self.assertEqual((0,0), self.scoreboard.get_score())                                # Test for initial score (user_score, computer_score)

    def test_update_score(self):        
        self.assertEqual((1,0), self.scoreboard.update_score("User"))                       # Test if the function will add 1 to the user's score
        self.assertEqual((1,1), self.scoreboard.update_score("Computer"))                   # Test if the function will add 1 to the computer's score
        self.assertRaises(ValueError, lambda: self.scoreboard.update_score("Player"))       # Test for invalid input
        self.assertRaises(TypeError, lambda: self.scoreboard.update_score(10))              # Test for wrong input type

    def test_get_score(self):
        self.assertEqual((0,0), self.scoreboard.get_score())                                # Test if function is able to get the correct score after updates
        self.scoreboard.update_score("User")
        self.assertEqual((1,0), self.scoreboard.get_score())                                
        self.scoreboard.update_score("Computer")
        self.assertEqual((1,1), self.scoreboard.get_score())                                
