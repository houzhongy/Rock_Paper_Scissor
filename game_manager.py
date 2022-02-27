# A class used to managed most of the game's logic
class GameManager():

    def __init__(self, max_score):
        if type(max_score) != int:
            raise TypeError("Please enter an Integer!")
        self.max_score = max_score          # Maximum score the game will go until

    def determine_winner(self, user_choice, computer_choice):
        try:
            user_choice = user_choice.upper()
            computer_choice = computer_choice.upper()
        except Exception as e:
            print(e)
        victories = {
            "ROCK" : ["SCISSOR"],             # Rock beats Scissor
            "PAPER" : ["ROCK"],               # Paper beats Rock
            "SCISSOR": ["PAPER"]              # Scissor beats Paper
        }
        if (user_choice not in victories) or (computer_choice not in victories):
            raise ValueError("Please enter a valid choice!")   
        defeats = victories[user_choice]    # Hold the list of choice that loses to the user
        # Based on user's perspective
        if user_choice == computer_choice:
            return "TIE"
        elif computer_choice in defeats:
            return "WIN"
        else:
            return "LOSE"
        

    def game_end(self, current_score):
        # End the game when either player's score have reached the max score
        if self.max_score == current_score:
            return True
        elif self.max_score > current_score:
            return False
        else:
            raise ValueError("Invalid score!")

    # Getter function to obtain max score
    def get_max_score(self):
        return self.max_score