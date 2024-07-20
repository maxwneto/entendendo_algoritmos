from chapt_06_breadth_first_search.breadth_first_search import bfs

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS starting from node A:")
bfs(graph, 'A')