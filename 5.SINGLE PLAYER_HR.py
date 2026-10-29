import random

SIZE = 5

# Generate random treasure location
treasure_row = random.randint(0, SIZE - 1)
treasure_col = random.randint(0, SIZE - 1)

player_row = 0
player_col = 0

attempts = 0


def calculate_distance(r1, c1, r2, c2):
    """AI heuristic: Manhattan Distance"""
    return abs(r1 - r2) + abs(c1 - c2)


def display_position():
    print("\nCurrent Position:")
    for i in range(SIZE):
        row = ""
        for j in range(SIZE):
            if i == player_row and j == player_col:
                row += " $ "
            else:
                row += " . "
        print(row)


print("================================")
print("      AI TREASURE HUNT")
print("================================")
print("Find the hidden treasure!")
print("Commands:")
print("U = Up")
print("D = Down")
print("L = Left")
print("R = Right")
print("Q = Quit")

while True:

    display_position()

    distance = calculate_distance(
        player_row,
        player_col,
        treasure_row,
        treasure_col
    )

    print("AI Hint: Treasure distance =", distance)

    if player_row == treasure_row and player_col == treasure_col:
        print("\nCongratulations!")
        print("You found the treasure!")
        print("Attempts:", attempts)
        break

    move = input("\nEnter your move: ").upper()
    attempts += 1

    new_row = player_row
    new_col = player_col

    if move == "U":
        new_row -= 1
    elif move == "D":
        new_row += 1
    elif move == "L":
        new_col -= 1
    elif move == "R":
        new_col += 1
    elif move == "Q":
        print("Game Over!")
        break
    else:
        print("Invalid move!")
        attempts -= 1
        continue

    # Check boundaries
    if 0 <= new_row < SIZE and 0 <= new_col < SIZE:
        player_row = new_row
        player_col = new_col
    else:
        print("You cannot move outside the grid!")
        attempts -= 1

print("\nThank you for playing!")
