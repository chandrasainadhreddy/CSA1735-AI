import heapq

class Node:
    def __init__(self, position: tuple, parent: 'Node' = None):
        self.position = position
        self.parent = parent
        self.g = 0  
        self.h = 0  
        self.f = 0  

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __hash__(self):
        return hash(self.position)

def astar(maze, start, end):
    start_node = Node(start)
    end_node = Node(end)

    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node)

        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1] 

        neighbors = get_neighbors(maze, current_node)

        for neighbor in neighbors:
            if neighbor in closed_list:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, end_node.position)
            neighbor.f = neighbor.g + neighbor.h

            if add_to_open(open_list, neighbor):
                heapq.heappush(open_list, neighbor)

    return None  

def get_neighbors(maze, node):
    neighbors = []
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  

    for direction in directions:
        neighbor_pos = (node.position[0] + direction[0], node.position[1] + direction[1])

        if 0 <= neighbor_pos[0] < len(maze) and 0 <= neighbor_pos[1] < len(maze[0]):
            if maze[neighbor_pos[0]][neighbor_pos[1]] != 1:  
                neighbors.append(Node(neighbor_pos, node))

    return neighbors

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  

def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node and neighbor.g > node.g:
            return False
    return True
if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 0]
    ]

    start = (0, 0)
    end = (5, 5)

    path = astar(maze, start, end)
    print(f"Path: {path}")
