from computer import computer
from humans import human


class Playfield:
    def __init__(self):
        self.player_one = human()
        self.player_two = None

    def run_game(self):
        self.display_message()
        self.game_settings()
        self.battlefield()
        self.display_winner()

    def display_message(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("RULES: Rock crushes Scissors")
        print("Scissors cuts Paper") 
        print("Paper covers Rock") 
        print("Rock crushes Lizard") 
        print("Lizard poisons Spock") 
        print("Spock smashes Scissors") 
        print("Scissors decapitates Lizard") 
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")

    def game_settings(self):
        game_type = input('Do you want to play single player or multiplayer?: ')
        game_settings = False
        while game_settings == False:
            if game_type == 'single player':
                self.player_two = computer()
                self.player_one.player_one_name()
                self.player_two.computer_name()
                print('Are you really sure you want to play against the AI?')
                game_settings = True
            elif game_type == 'multiplayer':
                self.player_two = human()
                self.player_one.player_one_name()
                self.player_two.player_two_name()
                print('Awesome! Let the games begin!')
                game_settings = True

# displays welcome message and rules of the game
# 
    def battlefield(self):

            

            print()

# shows player one and player two
# RPLSP playfield, displays list of gestures, lets user/AI choose gesture
# if user chooses something other than list of choices, user will be asked to pick from list of choices
# displays winner at the end of each round after users/AI gesture choice
    def display_winner(self):
        print()
# displays winner after best of 3 rounds