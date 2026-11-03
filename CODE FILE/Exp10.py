clauses = [
    {"EnjoysLearning"},                  # C1
    {"HasFreeTime"},                     # C2
    {"NotEnjoysLearning", "Happy"},      # C3
    {"NotHasFreeTime", "Happy"}          # C4
]
goal = "Happy"
print("Resolution Refutation\n")
print("--- Knowledge Base (CNF) ---")
for i, clause in enumerate(clauses, start=1):
    print(f"C{i}: {' OR '.join(sorted(clause))}")
# Negate the goal and add it to the knowledge base
negated_goal = "Not" + goal
clauses.append({negated_goal})

print(f"\nNegated goal added: {negated_goal}")
# Resolve complementary literals
derived = set()
empty_clause_found = False
print("\n--- Resolution Steps ---")
changed = True
while changed and not empty_clause_found:
    changed = False
    current_clauses = list(clauses)
    for i in range(len(current_clauses)):
        for j in range(i + 1, len(current_clauses)):
            c1 = current_clauses[i]
            c2 = current_clauses[j]
            for literal in c1:
                if literal.startswith("Not"):
                    complement = literal[3:]
                else:
                    complement = "Not" + literal
                if complement in c2:
                    resolvent = (c1 - {literal}) | (c2 - {complement})
                    print(
                        f"Resolve {sorted(c1)} and {sorted(c2)} "
                        f"on {literal} -> {sorted(resolvent)}"
                    )
                    if not resolvent:
                        empty_clause_found = True
                        break
                    frozen_resolvent = frozenset(resolvent)
                    if (frozen_resolvent not in
                            {frozenset(c) for c in clauses} and
                        frozen_resolvent not in derived):
                        derived.add(frozen_resolvent)
                        changed = True
            if empty_clause_found:
                break
        if empty_clause_found:
            break
    for clause in derived:
        new_clause = set(clause)
        if new_clause not in clauses:
            clauses.append(new_clause)
    derived.clear()
print("\n--- Final Result ---")
if empty_clause_found:
    print("Empty clause derived: Yes")
    print("Contradiction found.")
    print("Therefore, the goal 'Happy' is proved.")
else:
    print("Empty clause derived: No")
    print("The goal could not be proved by this resolution run.")




