import time
from player import ComputerPlayer, HumanPlayer


class TICTACTOE:
    def __init__(self):
        self.board = [' ' for _ in range(9)] ## here we are using a sigle list to represent 3x3
        self.winner = None # To determine who is the winner
        
        
    
    def print_board(self):
        
        for r in [self.board[i*3:(i+1)*3] for i in range(3)]: ## here we are getting the rows of the board
            print('| ' + ' | '.join(r) + ' |')
            
            
    @staticmethod
    def print_numbers_onBoard():
        
        Board_number = [[str(i) for i in range(3*j, (j+1)*3)] for j in range(3)] ##  This for loop is to output the board like this --> 0 | 1 | 2
        
        for r in Board_number:
            print('| ' + ' | '.join(r) + ' |')
            
            
            
    def available_spots(self):
        moves = []
        
        for (i, spot) in enumerate(self.board): ## ['x', 'O', 'O'] ---> [(0, 'x'), (1, 'O'), (2, 'O')]
            if spot == ' ':
                moves.append(i)
        return moves 
    
    
    def empty_spots(self):
        return ' ' in self.board ## returns a boolian whether the spot is empty or not
    
    
    def count_of_empty_spots(self):
        return len(self.available_spots()) ## returns the number of avialable spots on the board
    
    
    def make_move(self, spot, letter):
        if self.board[spot] == ' ': ## assignig the letter to the spot if available
            self.board[spot] = letter
            if self.is_winner(spot, letter):
                self.winner = letter
            return True
        
        return False
    
    
    def is_winner(self, spot, letter):
        
        ## This is for row winners
        
        row_idx = spot // 3
        row = self.board[row_idx * 3: (row_idx + 1) * 3]
        
        if all([s == letter for s in row]):
            return True
        
        ## Now we check for the column
        
        col_ind = spot % 3
        
        column = [self.board[col_ind + i *3] for i in range(3)]
        
        if all([s == letter for s in column]):
            return True
        
        ## here we will check the diagonals 
        
        if spot % 2 == 0:
            
            leftDiagonal = [self.board[i] for i in [0, 4, 8]]
            
            if all([s == letter for s in leftDiagonal]):
                return True
            
            
            rightDiagonal = [self.board[i] for i in [2, 4, 6]]
                
            if all([s == letter for s in rightDiagonal]):
                return True   
            
        ### if none of these cases returns true it means we don't have a winner
        
        return False
    


def play( game, X_player, O_player, print_game=True): ## getting the letter(winner) if there is one if not NONE which is a tie
    
    if print_game:
        game.print_numbers_onBoard()
        
    letter = 'X' ## The letter we start with
    
    ## iterate while the game has empty spots
    while game.empty_spots():
        
        # gettin the move from the appropriate player
        
        if letter == 'O':
            spot = O_player.next_move(game)
        else:
            spot = X_player.next_move(game)
            
        
        if game.make_move(spot, letter):
            if print_game:
                print(letter + f' made a move to {spot}')
                game.print_board()
                print('')
                print('') ## extra empty lines
                
            if game.winner:
                if print_game:
                    print(letter + ' won the game woo hoooo !!!') ## checking if there is a winner before switching players
                return letter
                
                
            letter = 'O' if letter == 'X' else 'X' ## here we switch letters the next players turn

            
        ## a small pause between player and computer turns
        time.sleep(1)
        
        
            
    if print_game:
        print("It's a tie !!")
            
              
    
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')    
    t = TICTACTOE()
    play(t, x_player, o_player, print_game=True)
    