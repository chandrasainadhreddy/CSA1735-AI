def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node, end=' ')  # Print the node as it's visited
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

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
    print("DFS Recursive Traversal Order:")
    dfs_recursive(graph, start_node)
    print()  # Newline for better readability
