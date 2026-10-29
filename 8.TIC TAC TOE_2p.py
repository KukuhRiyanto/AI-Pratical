# ============================================================
# TWO PLAYER TIC-TAC-TOE USING HEURISTIC FUNCTION
# ============================================================

# Create empty board
board = [" " for _ in range(9)]


# ------------------------------------------------------------
# DISPLAY BOARD
# ------------------------------------------------------------

def display_board():
    print("\n")
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")
    print()


# ------------------------------------------------------------
# CHECK WINNER
# ------------------------------------------------------------

def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and \
           board[b] == player and \
           board[c] == player:
            return True

    return False


# ------------------------------------------------------------
# HEURISTIC FUNCTION
# ------------------------------------------------------------

def heuristic(player):

    opponent = "O" if player == "X" else "X"

    score = 0

    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:

        line = [board[a], board[b], board[c]]

        # Three player's symbols
        if line.count(player) == 3:
            score += 100

        # Two player's symbols and one empty
        elif line.count(player) == 2 and line.count(" ") == 1:
            score += 10

        # One player's symbol and two empty
        elif line.count(player) == 1 and line.count(" ") == 2:
            score += 1

        # Opponent has a winning opportunity
        if line.count(opponent) == 2 and line.count(" ") == 1:
            score -= 10

    # Center position is valuable
    if board[4] == player:
        score += 3

    # Corners are slightly valuable
    corners = [0, 2, 6, 8]

    for corner in corners:
        if board[corner] == player:
            score += 1

    return score


# ------------------------------------------------------------
# DISPLAY HEURISTIC VALUES
# ------------------------------------------------------------

def display_heuristic():

    x_score = heuristic("X")
    o_score = heuristic("O")

    print("--------------------------------")
    print("        HEURISTIC VALUES")
    print("--------------------------------")

    print("Player X Score:", x_score)
    print("Player O Score:", o_score)

    if x_score > o_score:
        print("Current board advantage: Player X")

    elif o_score > x_score:
        print("Current board advantage: Player O")

    else:
        print("Current board evaluation: Balanced")

    print("--------------------------------")


# ------------------------------------------------------------
# CHECK DRAW
# ------------------------------------------------------------

def is_draw():
    return " " not in board


# ------------------------------------------------------------
# GET PLAYER MOVE
# ------------------------------------------------------------

def get_move(player):

    while True:

        try:
            position = int(
                input(f"Player {player}, enter position (1-9): ")
            )

            if position < 1 or position > 9:
                print("Enter a number between 1 and 9.")
                continue

            index = position - 1

            if board[index] != " ":
                print("That position is already occupied.")
                continue

            board[index] = player
            break

        except ValueError:
            print("Please enter a valid number.")


# ------------------------------------------------------------
# MAIN GAME
# ------------------------------------------------------------

def play_game():

    current_player = "X"

    print("=" * 50)
    print("       TWO PLAYER TIC-TAC-TOE")
    print("       USING HEURISTIC FUNCTION")
    print("=" * 50)

    print("\nBoard Positions:")
    print()
    print("  1  |  2  |  3")
    print("-----|-----|-----")
    print("  4  |  5  |  6")
    print("-----|-----|-----")
    print("  7  |  8  |  9")

    while True:

        display_board()

        get_move(current_player)

        # Show board after move
        display_board()

        # Calculate heuristic values
        display_heuristic()

        # Check winner
        if check_winner(current_player):

            print("\n" + "=" * 50)
            print(f"        PLAYER {current_player} WINS!")
            print("=" * 50)

            print(
                "Final Heuristic Score:",
                heuristic(current_player)
            )

            break

        # Check draw
        if is_draw():

            print("\n" + "=" * 50)
            print("              GAME DRAW")
            print("=" * 50)

            break

        # Change player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


# ------------------------------------------------------------
# START PROGRAM
# ------------------------------------------------------------

play_game()