from game_class import game_state

def quit_check(var_to_check):
    if var_to_check.lower().strip() == 'q':
        print('Exiting program')
        exit()
    return

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
    print()

def initialize_game():
    #this is a script to begin the game, assign player names to X and O
    start = input('Hello! Welcome to Tic Tac Toe.\nWould you like to play a game? yes[y]/no[n]\n')
    while start != 'y':
        if start.lower().strip() == 'n':
            print("Exiting program")
            exit()
        quit_check(start.lower().strip())
        start = input("Sorry, I didnt catch that. Please enter 'y' to play, or 'n' to exit.")

    print("Quit the game at any point by entering 'Q'.")
    p1 = input("The first player will play as X! What is your name?\n")
    quit_check(p1)

    p2 = input("The second player will play as O! What is your name?\n")
    quit_check(p2)
    
    print('\nTo play the game, you enter your move when prompted by typing\nthe column, then the row. For example, to move in the top right;\nEnter: "31"')
    return p1, p2

def prompt_move(player):
    correct_entry = False
    while correct_entry == False:
        try:
            move = input(f"{player}, please enter your move as two numbers, column then row:\n")
            if move.lower().strip() == 'q':
                break
            move_array = [int(move[0]), int(move[1])]
            correct_entry = True
        except:
            print("Sorry, invalid move entry. Please enter your move as two numbers, column then row.\nFor example: 32")
    quit_check(move)
    return move_array

if __name__ == "__main__":
    p1, p2 = initialize_game()
    game = game_state(p1, p2)
    print_game(game.game_board)

#initializing variables
    player_turn_check = 2
    player_whos_turn = p1
    player_move = [0, 0] #col, row
    succsesful_move = False
    winner = [False, 'winner_symbol']

    while winner[0] == False:
        if player_turn_check % 2 == 0:
            player_whos_turn = p1
        else:
            player_whos_turn = p2

        while succsesful_move == False:
            player_move = prompt_move(player_whos_turn)
            succsesful_move = game.make_move(player_whos_turn, player_move)
    
        if succsesful_move == True:
            player_turn_check += 1
    
        if player_turn_check >= 11: # 11 because variable initialized to 2 plus 9 moves
            winner = [True, 'tie']
        elif player_turn_check >= 7: # 7 because variable initialized to 2 plus 5 moves minimum before a winner is possible
            winner = game.check_win()

        print_game(game.game_board)

        succsesful_move = False #reset value to prompt for turn again

    if winner[1] == 'tie':
        print("It's a Tie! Play again to see who wins.")
    else:
        player_winner = p1 if winner[1] == 'X' else p2
    print(f"Congrats! Player {player_winner} wins! Rerun the program to play again.")