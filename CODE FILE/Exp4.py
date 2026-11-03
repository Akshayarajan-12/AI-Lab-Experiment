import heapq
# Weighted graph from the experiment image
graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 3), ('B', 2), ('D', 6), ('E', 4)],
    'D': [('B', 5), ('C', 6), ('E', 1), ('F', 2)],
    'E': [('C', 4), ('D', 1), ('F', 3)],
    'F': [('D', 2), ('E', 3)]
}
# Estimated cost from each node to goal F
h = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 3,
    'F': 0
}
def astar(start, goal):
    # Priority queue entries: (f, node, g, path)
    open_list = [(h[start], start, 0, [start])]
    best_g = {start: 0}
    expanded = []
    print("A* Search: Intelligent Route Planning")
    print(f"Start: {start} | Goal: {goal}\n")
    while open_list:
        f, node, g, path = heapq.heappop(open_list)

        # Ignore outdated entries
        if g != best_g.get(node):
            continue
        expanded.append(node)
        print(f"Step {len(expanded)}: Expand {node}")
        print(f"  g(n)={g}, h(n)={h[node]}, f(n)={f}")
        if node == goal:
            print("  Goal reached!")
            break
        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + h[neighbor]
            if new_g < best_g.get(neighbor, float('inf')):
                best_g[neighbor] = new_g
                new_path = path + [neighbor]
                heapq.heappush(
                    open_list,
                    (new_f, neighbor, new_g, new_path)
                )
                print(
                    f"  {node}->{neighbor}: "
                    f"g={new_g}, h={h[neighbor]}, f={new_f} "
                    f"| Updated"
                )
            else:
                print(f"  {node}->{neighbor}: No better cost")
        pending = sorted(
            (item[1], item[2], item[0])
            for item in open_list
            if item[2] == best_g.get(item[1])
        )
        print("  OPEN (node, g, f):", pending, "\n")
    if node == goal:
        print("--- Final Result ---")
        print("Optimal path    :", " -> ".join(path))
        print("Total path cost :", g)
        print("Nodes expanded  :", len(expanded))
        print("Expansion order :", " -> ".join(expanded))
    else:
        print("No route found.")
astar('A', 'F')

