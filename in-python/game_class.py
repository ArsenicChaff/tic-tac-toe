class game_state:
    def __init__(self, p1, p2):
        self.game_board = [[' ',' ',' '] for _ in range(3)]
        self.player1 = [p1, 'X']
        self.player2 = [p2, 'O']

    def make_move(self, player, move):
        col = move[0] - 1
        row = move[1] - 1
        try:
            if self.game_board[row][col] != ' ':
                print("Sorry, invalid move! Please try again.") #FIXME
                return False #returns false to prompt for another move
            
            if player == self.player1[0]:
                print("Player one moves, gameboard updated.")
                self.game_board[row][col] = self.player1[1]
                return True #returns true to signal succsesful completion

            if player == self.player2[0]:
                print("Player two moves, gameboard updated.")
                self.game_board[row][col] = self.player2[1]
                return True #returns true to signal succsesful completion
        except:
            print('Sorry, invalid move! Please try again.')
            return False
        print('This message should not be printed except for an error. Please try again, or cancel the program. Cancel with "Q"')
        return False #returns false to prompt for another move
        

    def check_win(self):
        #[     0    1    2
        # 0 [ '' , '' , '' ],
        # 1 [ '' , '' , '' ],
        # 2 [ '' , '' , '' ],
        #]
        if self.game_board[0][0] != ' ':
            if self.game_board[0][0] == self.game_board[0][1] and self.game_board[0][0] == self.game_board[0][2]:
                #top row winner
                return [True, self.game_board[0][0]]
            elif self.game_board[0][0] == self.game_board[1][0] and self.game_board[0][0] == self.game_board[2][0]:
                #first column winner
                return [True, self.game_board[0][0]]
            elif self.game_board[0][0] == self.game_board[1][1] and self.game_board[0][0] == self.game_board[2][2]:
                #top left to bottom right winner
                return [True, self.game_board[0][0]]
        
        if self.game_board[1][1] != ' ':
            if self.game_board[1][0] == self.game_board[1][1] and self.game_board[1][0] == self.game_board[1][2]:
                #middle row winner
                return [True, self.game_board[1][0]]
            elif self.game_board[0][1] == self.game_board[1][1] and self.game_board[0][1] == self.game_board[2][1]:
                #middle column winner
                return [True, self.game_board[0][1]]
            elif self.game_board[2][0] == self.game_board[1][1] and self.game_board[2][0] == self.game_board[0][2]:
                #bottom left to top right winner
                return [True, self.game_board[2][0]]

        if self.game_board[2][2] != ' ':
            if self.game_board[2][0] == self.game_board[2][1] and self.game_board[2][0] == self.game_board[2][2]:
                #bottom row winner
                return [True, self.game_board[2][0]]
            elif self.game_board[0][2] == self.game_board[1][2] and self.game_board[0][2] == self.game_board[2][2]:
                #last column winner
                return [True, self.game_board[0][2]]
        
        return [False, 'winner symbol']