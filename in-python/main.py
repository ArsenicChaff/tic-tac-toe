from game_class import game_state

def print_game(game_board):
    r = 1
    x = 1
    print('  c1  c2  c3')
    for row in game_board:
        print(f"r{x} {row[0]} | {row[1]} | {row[2]} ")
        if x < 3:
            print('  -----------')
        x += 1
        r += 1

def initialize_game():
    #this is a script to begin the game, assign player names to X and O
    start = input('Hello! Welcome to Tic Tac Toe.\nWould you like to play a game? yes[y]/no[n]\n')
    if start.lower().strip() == 'n':
        return
    p1 = input("The first player will play as X! What is your name?\n")
    p2 = input("The second player will play as O! What is your name?\n")
    
    print('\nTo play the game, you enter your move when prompted by typing\nthe column, then the row. For example, to move in the top right;\nEnter: "31"')
    return p1, p2

#p1, p2 = initialize_game()
p1, p2 = 'j', 't'
game = game_state(p1, p2)
print_game(game.game_board)