def get_player_guess():
    while True:
        try:
            guess = int(input("Guess a number: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def play_game():
    """
    The main function to run the game.
    This part is already complete.
    """
    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")