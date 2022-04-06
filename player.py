class Player:
    def __init__(self):
        self.player_one = self.choose_name()
        

    def choose_name(self):
        print('What is player ones name?: ')
        user_input = input()
        return user_input