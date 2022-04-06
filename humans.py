from player import Player


class human(Player):
    def __init__(self):
        super().__init__()
        self.gesture

    def player_one_name(self):
        self.name = input("Please enter player one's name: ")
    
    def player_two_name(self):
        self.name = input("Please enter player two's name name: ")

    def chosen_gesture(self):
        self.chosen_gesture = self.gesture[0:4]
        player_input = input('Please pick your gesture: ')
