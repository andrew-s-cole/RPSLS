from player import Player

class human(Player):
    def __init__(self):
        super().__init__()
        self.gesture

    def player_name(self):
        self.name = input('Please enter your name: ')
        

    def chosen_gesture(self):
        self.chosen_gesture = self.gesture[0:4]
        player_input = input('Please pick your gesture: ')