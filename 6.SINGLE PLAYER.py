import random

SIZE = 5

# Generate random treasure location
treasure_row = random.randint(0, SIZE - 1)
treasure_col = random.randint(0, SIZE - 1)

# Player starting position
player_row = 0
player_col = 0

attempts = 0


# Display player position
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
print("       TREASURE HUNT")
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

    # Check whether treasure is found
    if player_row == treasure_row and player_col == treasure_col:

        print("\nCongratulations!")
        print("You found the treasure!")
        print("Attempts:", attempts)

        break


    move = input("\nEnter your move: ").upper()

    attempts += 1

    new_row = player_row
    new_col = player_col


    # Player movement
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