# Game tree based on the given diagram
tree = {
    "A": ["B", "C", "D"],
    "B": ["E", "F", "G"],
    "C": ["H", "I", "J"],
    "D": ["K", "L", "M"],
    "E": [3, 5],
    "F": [6, 9],
    "G": [1, 2],
    "H": [4, 6],
    "I": [7, 8],
    "J": [9, 10],
    "K": [1, 3],
    "L": [12, 14],
    "M": [15, 18]
}

# Count evaluated terminal nodes and pruned branches
nodes_evaluated = 0
branches_pruned = 0


def alpha_beta(node, alpha, beta, is_max):
    global nodes_evaluated, branches_pruned

    # Terminal node: return its utility value
    if isinstance(node, int):
        nodes_evaluated += 1
        return node

    if is_max:
        best_value = float("-inf")

        for i, child in enumerate(tree[node]):
            value = alpha_beta(child, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            # Prune remaining branches if alpha >= beta
            if alpha >= beta:
                branches_pruned += len(tree[node]) - i - 1
                break

        return best_value

    else:
        best_value = float("inf")

        for i, child in enumerate(tree[node]):
            value = alpha_beta(child, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)

            # Prune remaining branches if beta <= alpha
            if beta <= alpha:
                branches_pruned += len(tree[node]) - i - 1
                break

        return best_value


# Evaluate each candidate move from the root
move_values = {}

for move in tree["A"]:
    move_values[move] = alpha_beta(
        move, float("-inf"), float("inf"), False
    )

# Select the best move for MAX
best_move = max(move_values, key=move_values.get)
best_value = move_values[best_move]

print("Move evaluations:")
for move, value in move_values.items():
    print(move, "=", value)

print("\nBest move for AI:", best_move)
print("Best utility value:", best_value)
print("Terminal nodes evaluated:", nodes_evaluated)
print("Branches pruned:", branches_pruned)