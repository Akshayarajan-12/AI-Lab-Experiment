from collections import deque
def water_jug_bfs():
    start = (0, 0)
    goal = 2
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    action = {start: "Initial state"}
    capacities = (4, 3)
    def get_next_states(a, b):
        states = []
        # Fill either jug
        states.append(((4, b), "Fill 4-litre jug"))
        states.append(((a, 3), "Fill 3-litre jug"))
        # Empty either jug
        states.append(((0, b), "Empty 4-litre jug"))
        states.append(((a, 0), "Empty 3-litre jug"))
        # Pour 4-litre jug into 3-litre jug
        transfer = min(a, capacities[1] - b)
        states.append(((a - transfer, b + transfer),
                       "Pour 4-litre jug into 3-litre jug"))
        # Pour 3-litre jug into 4-litre jug
        transfer = min(b, capacities[0] - a)
        states.append(((a + transfer, b - transfer),
                       "Pour 3-litre jug into 4-litre jug"))
        return states
    step = 0
    goal_state = None

    print("Water Jug Problem: State-Space Search")
    print("Start state:", start)
    print("Goal: Exactly 2 litres in the 4-litre jug\n")
    while queue:
        current = queue.popleft()
        step += 1
        a, b = current
        print(f"Step {step}: State = {current}")
        print("  Queue:", list(queue))
        if a == goal:
            goal_state = current
            print("  Goal reached!")
            break
        for next_state, operation in get_next_states(a, b):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                action[next_state] = operation
                queue.append(next_state)
                print(f"  Action: {operation}")
                print(f"  New state: {next_state}")
            else:
                print(f"  Skipped {next_state}: Already visited")
    print("\n--- Final Result ---")
    if goal_state is None:
        print("No solution found.")
        return

    path = []
    current = goal_state
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    for i, state in enumerate(path):
        print(f"Step {i}: {state} | {action[state]}")
    print("\nSolution path:", " -> ".join(map(str, path)))
    print("Operations required:", len(path) - 1)
    print("States discovered:", len(visited))
water_jug_bfs()

