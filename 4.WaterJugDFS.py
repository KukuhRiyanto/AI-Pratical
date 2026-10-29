# Capacities of the two jugs
CAP_A = 4
CAP_B = 3

# Goal amount
GOAL = 2


# Function to print the state
def print_state(state):
    print("Jug A:", state[0], "liters")
    print("Jug B:", state[1], "liters")
    print()


# Generate all possible moves
def get_neighbors(state):
    neighbors = []

    a, b = state

    # 1. Fill Jug A
    if a < CAP_A:
        neighbors.append(((CAP_A, b), "Fill Jug A"))

    # 2. Fill Jug B
    if b < CAP_B:
        neighbors.append(((a, CAP_B), "Fill Jug B"))

    # 3. Empty Jug A
    if a > 0:
        neighbors.append(((0, b), "Empty Jug A"))

    # 4. Empty Jug B
    if b > 0:
        neighbors.append(((a, 0), "Empty Jug B"))

    # 5. Pour Jug A -> Jug B
    amount = min(a, CAP_B - b)

    if amount > 0:
        neighbors.append(
            ((a - amount, b + amount),
             "Pour Jug A -> Jug B")
        )

    # 6. Pour Jug B -> Jug A
    amount = min(b, CAP_A - a)

    if amount > 0:
        neighbors.append(
            ((a + amount, b - amount),
             "Pour Jug B -> Jug A")
        )

    return neighbors


# DFS Algorithm
def dfs(start):
    stack = [(start, [])]
    visited = set()

    while stack:

        state, path = stack.pop()  # LIFO -> depth-first instead of FIFO (breadth-first)

        if state in visited:
            continue

        visited.add(state)

        # Check goal
        if state[0] == GOAL or state[1] == GOAL:
            return path + [(state, "Goal Reached")]

        # Generate neighbors (pushed in reverse so the FIRST generated
        # neighbor ends up on TOP of the stack and is explored first —
        # this matches the left-to-right order used in the HTML DFS)
        for neighbor, action in reversed(get_neighbors(state)):

            if neighbor not in visited:
                stack.append(
                    (neighbor, path + [(neighbor, action)])
                )

    return None


# Starting state
start = (0, 0)

# Run DFS
solution = dfs(start)


# Print solution
if solution:

    print("Solution found in", len(solution) - 1, "moves:\n")

    print("Initial State:")
    print_state(start)

    for state, action in solution:
        print(action)
        print_state(state)

else:
    print("No solution found.")
