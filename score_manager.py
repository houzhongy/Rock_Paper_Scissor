# A class used to handle the score of the game
class ScoreManager():
    def __init__(self):
        self.user_score = 0             # Initialise the score to 0
        self.computer_score = 0

    def update_score(self, winner):
        if type(winner) != str:
            raise TypeError
        winner = winner.upper()   
        if winner == "USER":
            self.user_score += 1
        elif winner == "COMPUTER":
            self.computer_score += 1
        else:
            raise ValueError("Please enter a valid player")
        return self.get_score()
    
    def get_score(self):
        return (self.user_score, self.computer_score)
        

