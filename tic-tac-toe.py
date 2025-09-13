import random

def print_board(board):
    """Prints the Tic-Tac-Toe board"""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    """Check if a player has won"""
    # Rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Check if the board is full"""
    return all(cell != " "
     for row in board for cell in row)

def player_move(board, player):
    """Handles player input"""
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That spot is taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

def computer_move(board):
    """Computer picks a random empty spot"""
    available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    move = random.choice(available_moves)
    board[move[0]][move[1]] = "O"

def play_game(mode="2p"):
    """Main game loop"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are like this:\n")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print("-" * 9)

    current_player = "X"

    while True:
        print_board(board)

        if mode == "1p" and current_player == "O":
            print("Computer's turn...")
            computer_move(board)
        else:
            player_move(board, current_player)

        #Winner
        if check_winner(board, current_player):
            print_board(board)
            if mode == "1p" and current_player == "O":
                print("Computer wins! 🤖")
            else:
                print(f"Player {current_player} wins! 🎉")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie! 🤝")
            break

        current_player = "O" if current_player == "X" else "X"

def main():
    print("===== Tic-Tac-Toe =====")

    while True:
        mode = input("Choose mode: 1p (vs Computer) or 2p (vs Player): ").lower().strip()

        if mode in ["1", "1p"]:
            mode = "1p"
        elif mode in ["2", "2p"]:
            mode = "2p"
        else:
            print("Invalid choice. Defaulting to 2 player mode.")
            mode = "2p"

        play_game(mode)

        #play again
        again = input("Do you want to play again? (y/n): ").lower().strip()
        if again not in ["y", "yes"]:
            print("Thanks for playing! 👋")
            break


if __name__ == "__main__":
    main()
