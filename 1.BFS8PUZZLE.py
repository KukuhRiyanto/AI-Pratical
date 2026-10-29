# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Function to print the puzzle
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Generate all possible moves
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)  # Position of blank/zero
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors

# BFS Algorithm
def bfs(start):
    queue = [(start, [])]   # Simple queue
    visited = set()

    while queue:
        state, path = queue.pop(0)   # Remove first item

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                queue.append((neighbor, path + [state]))

    return None

# Example start state
start = (1, 0, 2,
         3, 4, 5,
         6, 7, 8)

solution = bfs(start)

if solution:
    print("Solution found in", len(solution)-1, "moves:\n")

    for step in solution:
        print_board(step)
else:
    print("No solution found.")
