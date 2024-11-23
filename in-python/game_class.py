class game_state:
    def __init__(self, p1, p2):
        self.game_board = [[' ',' ',' '] for _ in range(3)]
        player1 = [p1, 'X']
        p1c = player1[1]
        player2 = [p2, 'O']
        p2c = player2[1]

    def make_move(self, player, move):
        #make the move, check to ensure its a legal move
        pass

    def check_win(self):
        #checks for a winner
        pass