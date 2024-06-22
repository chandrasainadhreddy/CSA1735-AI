from collections import deque

def is_valid_state(state, capacity):
    x, y = state
    return 0 <= x <= capacity[0] and 0 <= y <= capacity[1]

def is_goal_state(state, goal):
    return state[0] == goal or state[1] == goal

def bfs_water_jug(capacity, goal):
    start_state = (0, 0)
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        (current_state, path) = queue.popleft()
        x, y = current_state

        if is_goal_state(current_state, goal):
            return path + [current_state]

        if current_state in visited:
            continue

        visited.add(current_state)

        # Fill jug 1
        next_state = (capacity[0], y)
        if is_valid_state(next_state, capacity):
            queue.append((next_state, path + [current_state]))

        # Fill jug 2
        next_state = (x, capacity[1])
        if is_valid_state(next_state, capacity):
            queue.append((next_state, path + [current_state]))

        # Empty jug 1
        next_state = (0, y)
        if is_valid_state(next_state, capacity):
            queue.append((next_state, path + [current_state]))

        # Empty jug 2
        next_state = (x, 0)
        if is_valid_state(next_state, capacity):
            queue.append((next_state, path + [current_state]))

        # Pour jug 1 to jug 2
        pour = min(x, capacity[1] - y)
        next_state = (x - pour, y + pour)
        if is_valid_state(next_state, capacity):
            queue.append((next_state, path + [current_state]))

        # Pour jug 2 to jug 1
        pour = min(y, capacity[0] - x)
        next_state = (x + pour, y - pour)
        if is_valid_state(next_state, capacity):
            queue.append((next_state, path + [current_state]))

    return None

def solve_water_jug_problem(jug1, jug2, goal):
    capacity = (jug1, jug2)
    path = bfs_water_jug(capacity, goal)

    if path:
        print("Solution:")
        for state in path:
            print(f"Jug 1: {state[0]} liters, Jug 2: {state[1]} liters")
    else:
        print("No solution found.")

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    goal_amount = 2
    solve_water_jug_problem(jug1_capacity, jug2_capacity, goal_amount)
