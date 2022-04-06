from computer import computer
from humans import human

class Playfield:
    def __init__(self):
        self.player_one = human()
        self.player_one = None

    def run_game(self):
        self.display_message()
        self.battlefield()
        self.display_winner()

    def display_message(self):
        print()
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