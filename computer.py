from player import Player
import random


class computer(Player):
    def __init__(self):
        super().__init__()
        self.gesture

    def computer_name(self):
        self.name = input('Please enter the computers name: ')

    def chosen_gesture(self):
        self.chosen_gesture = random.randint(0, 4)
        print(f'{self.ai_name} has chosen {self.chosen_gesture}')
        return self.chosen_gesture
