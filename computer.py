from player import Player
import random
class computer(Player):
    def __init__(self):
        super().__init__()
      
    def computer_name(self):
        self.name = input('Please enter the computers name: ')
    def choose_gesture(self):
        random_gesture = random.choice(self.gestures)
        self.gesture_selection = random_gesture
        print(f'{self.name} has chosen {self.gesture_selection}')
