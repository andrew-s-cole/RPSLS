from computer import computer
from humans import human
from player import Player

class Playfield:
    def __init__(self):
        self.player_one = human()
        self.player_one = None

    def run_game(self):
        self.display_message()
        self.game_settings()
        self.battlefield()
        self.display_winner()

    def display_message(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("""RULES: Rock crushes Scissors
                        Scissors cuts Paper 
                        Paper covers Rock 
                        Rock crushes Lizard 
                        Lizard poisons Spock 
                        Spock smashes Scissors 
                        Scissors decapitates Lizard 
                        Lizard eats Paper 
                        Paper disproves Spock 
                        Spock vaporizes Rock""")

    def game_settings(self):
        game_type = input(
            'Do you want to play single player or multiplayer?: ')
        game_settings = False
        while game_settings == False:
            if game_type == 'single player':
                self.player_two = computer()
                self.player_one.player_name()
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
    def battlefield(self, Player):
        players = human, computer
        gestures = ['Rock', 'Paper','Scissors', 'Lizard','Spock']

        if human == input("Rock"):
            

            print()

# shows player one and player two
# RPLSP playfield, displays list of gestures, lets user/AI choose gesture
# if user chooses something other than list of choices, user will be asked to pick from list of choices
# displays winner at the end of each round after users/AI gesture choice
    def display_winner(self):
        print()
# displays winner after best of 3 rounds