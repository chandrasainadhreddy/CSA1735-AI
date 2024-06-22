from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = None

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if (3 - self.missionaries) < (3 - self.cannibals) and (3 - self.missionaries) > 0:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def get_children(self):
        children = []
        if self.boat == 1:
            new_states = [
                State(self.missionaries - 2, self.cannibals, 0),
                State(self.missionaries - 1, self.cannibals - 1, 0),
                State(self.missionaries, self.cannibals - 2, 0),
                State(self.missionaries - 1, self.cannibals, 0),
                State(self.missionaries, self.cannibals - 1, 0)
            ]
        else:
            new_states = [
                State(self.missionaries + 2, self.cannibals, 1),
                State(self.missionaries + 1, self.cannibals + 1, 1),
                State(self.missionaries, self.cannibals + 2, 1),
                State(self.missionaries + 1, self.cannibals, 1),
                State(self.missionaries, self.cannibals + 1, 1)
            ]
        for state in new_states:
            if state.is_valid():
                state.parent = self
                children.append(state)
        return children

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def bfs():
    initial_state = State(3, 3, 1)
    if initial_state.is_goal():
        return initial_state
    frontier = deque([initial_state])
    explored = set()
    while frontier:
        state = frontier.popleft()
        if state.is_goal():
            return state
        explored.add(state)
        children = state.get_children()
        for child in children:
            if child not in explored and child not in frontier:
                frontier.append(child)
    return None

def print_solution(solution):
    path = []
    state = solution
    while state:
        path.append(state)
        state = state.parent
    path.reverse()
    for step in path:
        print(f"({step.missionaries}, {step.cannibals}, {step.boat})")

if __name__ == "__main__":
    solution = bfs()
    if solution:
        print("Solution found!")
        print_solution(solution)
    else:
        print("No solution found.")
