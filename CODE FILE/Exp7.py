# Game tree based on the given diagram
tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [3, 5],
    "E": [2, 9],
    "F": [12, 5],
    "G": [23, 23]
}

# Store the evaluated value of each node
values = {}


def minimax(node, is_maximizing):
    # If the node is a terminal node, return its utility
    if isinstance(node, int):
        return node

    # Evaluate all children recursively
    child_values = []

    for child in tree[node]:
        value = minimax(child, not is_maximizing)
        child_values.append(value)

    # MAX chooses the largest value
    if is_maximizing:
        best_value = max(child_values)
    else:
        # MIN chooses the smallest value
        best_value = min(child_values)

    values[node] = best_value
    return best_value


# Start from root node A (MAX)
best_value = minimax("A", True)

print("Minimax Evaluation:")
for node in ["D", "E", "F", "G", "B", "C", "A"]:
    print(node, "=", values[node])

print("\nBest move for AI:", tree["A"][
    0 if values["B"] >= values["C"] else 1
])
print("Best achievable utility:", best_value)