from player import Player
import random

class computer(Player):
    def __init__(self):
        super().__init__()
        self.gesture

    def set_ai_name(self):
        self.ai_name = random.choice(0, 2)
        return self.ai_name

    def chosen_gesture(self):
        self.chosen_gesture = random.randint(0, 4)
        print(f'{self.ai_name} has chosen {self.chosen_gesture}')
        return self.chosen_gesture