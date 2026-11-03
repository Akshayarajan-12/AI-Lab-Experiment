
# Available colours (domains)
colours = ["Red", "Green", "Blue"]

# Variables: regions A, B, C, D, E, F
regions = ["A", "B", "C", "D", "E", "F"]

# Adjacency constraints from the given diagram
neighbours = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D", "F"],
    "F": ["D", "E"]
}

# Store the assigned colours
assignment = {}

# Count assignment attempts
attempts = 0


def is_safe(region, colour):
    # Check whether any already-coloured neighbour
    # has the same colour
    for neighbour in neighbours[region]:
        if assignment.get(neighbour) == colour:
            return False

    return True


def solve(index):
    global attempts

    # All regions have been coloured
    if index == len(regions):
        return True

    # Select the next region
    region = regions[index]

    # Try each available colour
    for colour in colours:
        attempts += 1

        if is_safe(region, colour):
            # Assign the colour
            assignment[region] = colour

            # Solve for the next region
            if solve(index + 1):
                return True

            # Backtrack: remove the colour assignment
            del assignment[region]

    return False


# Run the CSP solver
if solve(0):
    print("Valid Map Colouring:\n")

    for region in regions:
        print(region, ":", assignment[region])

    # Verify all adjacency constraints
    valid = True

    for region in regions:
        for neighbour in neighbours[region]:
            if assignment[region] == assignment[neighbour]:
                valid = False
                print("Conflict:", region, "and", neighbour)

    print("\nAll adjacency constraints satisfied:", valid)
    print("Total assignment attempts:", attempts)

else:
    print("No valid colouring exists.")