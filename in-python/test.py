def prompt_move(player):
    move = input(f"{player}, please enter your move:\n")
    move_array = [int(move[0]), int(move[1])]
    print(move_array)
    return move_array



player_move = prompt_move('ja')