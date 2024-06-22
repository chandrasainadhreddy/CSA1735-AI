from collections import deque

def bfs(graph, start):
    # Initialize the queue with the start node and the visited set
    queue = deque([start])
    visited = set([start])
    
    # List to keep track of the order of traversal
    order = []

    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        order.append(node)
        
        # Iterate over all the adjacent nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Mark the neighbor as visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

    return order

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start_node = 'A'
    traversal_order = bfs(graph, start_node)

    print("BFS Traversal Order:", traversal_order)
