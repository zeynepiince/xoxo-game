def print_board(board):
    """Print the game board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check for a winner"""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False

def get_user_move(board):
    """Get a valid move from the user"""
    while True:
        try:
            move = input("Enter your move (row and column, e.g., 1 2): ")
            x, y = map(int, move.split())
            if board[x][y] == " ":
                return x, y
            else:
                print("That cell is already taken! Choose another one.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column numbers between 0 and 2.")

def get_computer_move(board):
    """Choose a random empty cell for the computer"""
    from random import choice
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return choice(empty_cells)

def play_game():
    """Start the Tic-Tac-Toe game"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("\nSimple Tic-Tac-Toe Game\n")
    print("Press Ctrl+C to exit the game.\n")
    
    # Game loop
    for turn in range(9):
        print_board(board)
        if turn % 2 == 0:
            print("Your turn (X)")
            x, y = get_user_move(board)
            board[x][y] = "X"
        else:
            print("Computer is making a move (O)...")
            x, y = get_computer_move(board)
            board[x][y] = "O"
        
        if check_winner(board):
            print_board(board)
            print("Winner: {}".format("You (X)" if turn % 2 == 0 else "Computer (O)"))
            return
    
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    play_game()
