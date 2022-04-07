from player import Player
class human(Player):
    def __init__(self):
        super().__init__()
 
    def player_one_name(self):
        self.name = input("Please enter player one's name: ")
    
    def player_two_name(self):
        self.name = input("Please enter player two's name name: ")
    def choose_gesture(self):
        
        
        
        player_input = (input('Please select your gesture: '))
            
        if player_input == self.gestures[0]:
                    self.gesture_selection = self.gestures[0]
                    print(f'You have chosen {self.gestures[0]}')
                    
        elif player_input == self.gestures[1]:
                    self.gesture_selection = self.gestures[1]
                    print(f'You have chosen {self.gestures[1]}')
                   
        elif player_input == self.gestures[2]:
                    self.gesture_selection = self.gestures[2]
                    print(f'You have chosen {self.gestures[2]}')
                      
        elif player_input== self.gestures[3]:
                    self.gesture_selection = self.gestures[3]
                    print(f'You have chosen {self.gestures[3]}')
                  
        elif player_input == self.gestures[4]:
                    self.gesture_selection = self.gestures[4]
                    print(f'You have chosen {self.gestures[4]}')