import random


class Player:
    def __init__(self, letter):
        self.letter = letter ## This is to determin whether its X or O
        
        
    def next_move(self, next):
        pass
    
    
    
    
class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def next_move(self, next):
        spot = random.choice(next.available_spots())
        
        return spot ## this get a random valid spot
    
    
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def next_move(self, next):
        
        valid_spot = False
        value = None
        
        while not valid_spot:
            spot = input(self.letter + "'s. turn, move from 0 - 8: ")  # we check if the if this value is correct by converting it to an integer if not then its not valid also we check if it's available if not we set it as invalid
                                                                                                                                        
            try:
                value = int(spot) 
                
                if value not in next.available_spots():
                    return ValueError
                
                valid_spot = True ## success                                                        
                
            except ValueError:
                print('Invalid spot, Try again.')
                
        return value
                                                                      
                                                
            