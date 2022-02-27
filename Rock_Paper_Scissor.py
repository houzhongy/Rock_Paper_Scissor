from random import randint
import game_manager, score_manager

moves = ["ROCK", "PAPER", "SCISSOR"]

while True:
    print("WELCOME TO THE SCRIPTED GAME!!!")
    print("Choose the game mode: ")
    try:                                                                                        # Get the user's preferred game mode
        game_mode = int(input("1. Player VS Computer\n2. Computer VS Computer\n"))              # Check for input validity
        if game_mode != 1 and game_mode != 2:                                           
            raise ValueError("Please enter a valid number!\n")            
        max_score = int(input("Choose the maximum score for the game "))                        # To determine at which score one will win
    except Exception as e:
        print(e)
        print()
        continue
        
    manager = game_manager.GameManager(max_score)
    scoreboard = score_manager.ScoreManager()
    
    if game_mode == 1:                                                                          # Player VS Computer
        while not manager.game_end(max(scoreboard.get_score())):
            print(f"--------Current Score--------\nUser: {scoreboard.get_score()[0]} \tComputer: {scoreboard.get_score()[1]}")
            print("-----------------------------")
            try:
                choice = int(input("Play ur hand: \n1: Rock \n2: Paper \n3: Scissors \n"))
                if choice < 1 or choice > 3:                            # Error handling
                    raise ValueError("Please enter a valid number!\n")
            except Exception as e:
                print(e)
                continue
            user_choice = moves[choice-1]                                                  # Link user's selection to the respective move
            computer_choice = moves[randint(0,2)]                                               # Randomize computer move selection
            result = manager.determine_winner(user_choice,computer_choice)
            print(f"User chooses: {user_choice}")
            print(f"Computer chooses: {computer_choice}")
            if result == "WIN":
                scoreboard.update_score("User")
                print("User Wins...\n")
            elif result == "LOSE":
                scoreboard.update_score("Computer")
                print("Computer Wins...\n")
            else:
                print("Its a tie...\n")
            print("--------------------------------------------")
        print(f"--------Final Score--------\nUser: {scoreboard.get_score()[0]} \tComputer: {scoreboard.get_score()[1]}")
        print("-----------------------------")
        if scoreboard.get_score()[0] > scoreboard.get_score()[1]:
            print("User wins the game\n")
        else:
            print("Computer wins the game\n")
    else:                                                                                       # Computer VS Computer
        while not manager.game_end(max(scoreboard.get_score())):
            print(f"--------Current Score--------\nComputer1: {scoreboard.get_score()[0]} \tComputer2: {scoreboard.get_score()[1]}")
            print("-----------------------------")
            user_choice = moves[randint(0,2)]                                                   # Randomize computer move selection
            computer_choice = moves[randint(0,2)]                                               # Randomize computer move selection
            result = manager.determine_winner(user_choice,computer_choice)
            print(f"Computer1 chooses: {user_choice}")
            print(f"Computer2 chooses: {computer_choice}")
            if result == "WIN":
                scoreboard.update_score("User")
                print("Computer1 Wins...\n")
            elif result == "LOSE":
                scoreboard.update_score("Computer")
                print("Computer2 Wins...\n")
            else:
                print("Its a tie...\n")
        print(f"--------Final Score--------\nComputer1: {scoreboard.get_score()[0]} \tComputer2: {scoreboard.get_score()[1]}")
        print("-----------------------------")
        if scoreboard.get_score()[0] > scoreboard.get_score()[1]:                               # To check who wins the game
            print("Computer1 wins the game\n")
        else:
            print("Computer2 wins the game\n")
    
    valid = False
    while not valid:
        try:
            quit_game = input("Quit? (Y/N): ")                                                          # Quit condition
            if quit_game.lower() != "y" and quit_game.lower() != "n":    
                raise ValueError("Please enter Y/N!\n")   
            else:
                valid = True                                        
        except Exception as e:
            print(e)
    if quit_game.lower() == "y":
        break
