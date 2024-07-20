from collections import deque


def bfs(graph, start):
    # Create a queue for BFS and add the starting node
    queue = deque([start])
    # Keep track of visited nodes
    visited = set()
    visited.add(start)

    while queue:
        # Remove the first node from the queue
        node = queue.popleft()
        print(node, end=" ")  # Process the node (in this case, just print it)

        # Add all unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)