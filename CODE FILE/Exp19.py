move_count = 0
def tower_of_hanoi(n, source, auxiliary, destination):
    global move_count
    if n == 1:
        move_count += 1
        print(
            "Move disk 1 from",
            source,
            "to",
            destination
        )
        return
    tower_of_hanoi(
        n - 1,
        source,
        destination,
        auxiliary
    )
    move_count += 1
    print(
        "Move disk", n,
        "from", source,
        "to", destination
    )
    tower_of_hanoi(
        n - 1,
        auxiliary,
        source,
        destination
    )
n = 3
print("Towers of Hanoi")
print("----------------")
print("Number of disks:", n)
print("\nSequence of moves:")
tower_of_hanoi(n, 'A', 'B', 'C')
print("\nTotal Moves:", move_count)
print("Minimum Moves Required:", 2**n - 1)

