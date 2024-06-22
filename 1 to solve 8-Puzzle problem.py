import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.empty_tile = self.find_empty_tile()
        self.priority = self.moves + self.manhattan_distance()

    def find_empty_tile(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    target_x, target_y = divmod(self.board[i][j] - 1, 3)
                    distance += abs(target_x - i) + abs(target_y - j)
        return distance

    def is_goal(self):
        goal = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]]
        return self.board == goal

    def generate_successors(self):
        successors = []
        x, y = self.empty_tile
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                successors.append(PuzzleState(new_board, self.moves + 1, self))
        return successors

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board]) + f'\nMoves: {self.moves}\n'


def solve_puzzle(initial_board):
    initial_state = PuzzleState(initial_board)
    open_set = []
    heapq.heappush(open_set, initial_state)
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)
        
        if current_state.is_goal():
            return current_state

        closed_set.add(current_state)

        for successor in current_state.generate_successors():
            if successor not in closed_set and successor not in open_set:
                heapq.heappush(open_set, successor)

    return None


def print_solution(solution):
    path = []
    state = solution
    while state:
        path.append(state)
        state = state.previous
    path.reverse()

    for step in path:
        print(step)


if __name__ == "__main__":
    initial_board = [[1, 2, 3],
                     [4, 0, 6],
                     [7, 5, 8]]

    solution = solve_puzzle(initial_board)
    
    if solution:
        print_solution(solution)
    else:
        print("No solution found.")
