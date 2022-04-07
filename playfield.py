from player import Player
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
        print("Here are the rules:") 
        print("Rock crushes Scissors")
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
    def battlefield(self):
  
    
        while self.player_one.score < 2 and self.player_two.score <2:
      
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()

            if self.player_one.gesture_selection == self.player_two.gesture_selection:
             print('The result is a tie')

            elif  self.player_one.gestures[0] and  self.player_two.gestures[2]:
             self.player_one.score += 1
             print(f'{self.player_one.name} wins.')
            elif  self.player_one.gestures[0] and  self.player_two.gestures[3]:
             self.player_one.score += 1
             print(f'{self.player_one.name} wins.')
            elif self.player_one.gestures[1] and  self.player_two.gestures[0]:
             self.player_one.score += 1
             print(f'{self.player_one.name} wins.')
            elif self.player_one.gestures[1] and self.player_two.gestures[4]:
             self.player_one.score += 1
             print(f'{self.player_one.name} wins.')
            elif  self.player_one.gestures[2] and self.player_two.gestures[1]:
             self.player_one.score += 1
             print(f'{self.player_one.name} wins.')
            elif  self.player_one.gestures[2] and  self.player_two.gestures[3]:
             self.player_one.score += 1
             print(f'{self.player_one.name} wins.')
            elif  self.player_one.gestures[3] and  self.player_two.gestures[1]:
             self.player_one.score += 1
             print(f'{self.player_one.name} wins.')
            elif  self.player_one.gestures[3] and  self.player_two.gestures[4]:
             self.player_one.score += 1
             print(f'{self.player_one.name} wins.')
            elif  self.player_one.gestures[4] and  self.player_two.gestures[0]:
             self.player_one.score += 1
             print(f'{self.player_one.name} wins.')
            elif  self.player_one.gestures[4] and self.player_two.gestures[2]:
             self.player_one.score += 1
             print(f'{self.player_one.name} wins.')

            else:
             self.player_two.score += 1
             print(f'{self.player_two.name} wins.')

    def display_winner(self):
      if self.player_one.score == 2:
          print(f'{self.player_one.name} wins!')
      elif self.player_two.score == 2:
            print(f'{self.player_two.name} wins!')