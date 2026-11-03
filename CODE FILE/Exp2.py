graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': ['L'],
    'L':[]
}
def dfs(graph, start, goal):
    visited = set()
    path = []
    order = []
    def search(node):
        visited.add(node)
        order.append(node)
        path.append(node)
        print(f"Step {len(order)}: Node = {node}")
        print(f"  Current path: {' -> '.join(path)}")
        if node == goal:
            print("  Goal reached!")
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                print(f"  Exploring edge: {node} -> {neighbor}")

                if search(neighbor):
                    return True
            else:
                print(f"  Skipping {neighbor}: Already visited")
        path.pop()
        print(f"  Backtracking from {node}")
        return False
    print("DFS: AI Pipeline Reachability")
    print(f"Start: {start} | Goal: {goal}\n")
    found = search(start)
    print("\n--- Final Result ---")
    print("Traversal order:", " -> ".join(order))
    if found:
        print("Path found     :", " -> ".join(path))
        print("Path length    :", len(path) - 1, "edges")
    else:
        print("No path exists.")
        print("Path found     : None")
    print("Nodes explored :", len(order))
dfs(graph, 'A', 'H')








