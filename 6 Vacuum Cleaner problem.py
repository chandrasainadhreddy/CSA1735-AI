from collections import deque

# Directions for moving up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_move(x, y, grid, visited):
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and (x, y) not in visited and grid[x][y] != -1

def bfs(grid, start):
    queue = deque([(start, 0)])
    visited = set([start])
    dirty_cells = sum(row.count(1) for row in grid)
    cleaned_cells = 0
    path = []

    while queue:
        (x, y), steps = queue.popleft()
        path.append((x, y))

        if grid[x][y] == 1:
            cleaned_cells += 1
            grid[x][y] = 0

        if cleaned_cells == dirty_cells:
            return steps, path

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, grid, visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    return -1, []

def find_start_position(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 'S':
                return i, j
    return None

def vacuum_cleaner_problem(grid):
    start = find_start_position(grid)
    if start is None:
        raise ValueError("Start position 'S' not found in the grid.")
    
    steps, path = bfs(grid, start)

    if steps != -1:
        print(f"Total steps to clean all dirty cells: {steps}")
        print("Path taken:")
        for step in path:
            print(step)
    else:
        print("No solution found to clean all dirty cells.")

if __name__ == "__main__":
    grid = [
        [0, 1, 0, 1],
        [0, 'S', 0, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 0]
    ]
    vacuum_cleaner_problem(grid)
