parents = [
    ("Ravi", "Arun"),
    ("Ravi", "Meena"),
    ("Arun", "Kiran"),
    ("Meena", "Priya"),
    ("Suresh", "Ravi")
]
def is_parent(parent, child):
    return (parent, child) in parents
def get_children(parent):
    return [child for p, child in parents if p == parent]
def get_parents(child):
    return [parent for parent, c in parents if c == child]
def get_grandparents(person):
    grandparents = []
    for parent in get_parents(person):
        grandparents.extend(get_parents(parent))
    return grandparents
# Display family relationships
person = "Kiran"
print("Family Tree Relationships")
print("-------------------------")
print("Parents of", person, ":", get_parents(person))
print("Children of Ravi:", get_children("Ravi"))
print("Grandparents of", person, ":", get_grandparents(person))
print("\nIs Ravi a parent of Arun?", is_parent("Ravi", "Arun"))
print("Is Suresh a grandparent of Kiran?",
      "Suresh" in get_grandparents("Kiran"))
