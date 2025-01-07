def initialize_board(): return [[' '] * 3 for _ in range(3)]
def display_board(board): [print("|".join(row), "\n-----") for row in board]
def get_player_move(): return int(input("Row (0-2): ")), int(input("Col (0-2): "))
def is_valid_move(board, r, c): return 0 <= r < 3 and 0 <= c < 3 and board[r][c] == ' '
def make_move(board, player, r, c): board[r][c] = player
def check_winner(board, p): 
    return any(all(c == p for c in row) for row in board) or \
           any(all(row[i] == p for row in board) for i in range(3)) or \
           all(board[i][i] == p for i in range(3)) or \
           all(board[i][2 - i] == p for i in range(3))
def is_board_full(board): return all(c != ' ' for row in board for c in row)
def play_tic_tac_toe():
    board, player = initialize_board(), 'X'
    while True:
        display_board(board)
        print(f"Player {player}'s turn.")
        r, c = get_player_move()
        if is_valid_move(board, r, c):
            make_move(board, player, r, c)
            if check_winner(board, player): print(f"Player {player} wins!"); break
            if is_board_full(board): print("The game ends in a tie!"); break
            player = 'O' if player == 'X' else 'X'
        else: print("Invalid move. Try again.")
play_tic_tac_toe()
