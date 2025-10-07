# 📘 All Important Set Functions and Operations

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Original Sets:")
print("set1 =", set1)
print("set2 =", set2)

# ---------------------------------------------------------
print("\n========== 1. Basic Operations ==========")
set1.add(9)            # Add single element
print("After add:", set1)

set1.remove(2)         # Remove specific element (Error if not found)
print("After remove:", set1)

set1.discard(10)       # Remove element safely (no error if not found)
print("After discard:", set1)

popped = set1.pop()    # Removes a random element
print("After pop:", set1, "| Popped value:", popped)

set1.update([10, 11])  # Add multiple elements
print("After update:", set1)

# ---------------------------------------------------------
print("\n========== 2. Mathematical Operations ==========")
print("Union:", set1.union(set2))           # Combine both (no duplicates)
print("Intersection:", set1.intersection(set2))  # Common elements
print("Difference:", set1.difference(set2)) # Elements only in set1
print("Symmetric Difference:", set1.symmetric_difference(set2))  # Non-common elements

# ---------------------------------------------------------
print("\n========== 3. Set Relations ==========")
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print("a is subset of b:", a.issubset(b))
print("b is superset of a:", b.issuperset(a))
print("a and b disjoint?:", a.isdisjoint({6, 7}))

# ---------------------------------------------------------
print("\n========== 4. Copy & Clear ==========")
copy_set = set1.copy()
print("Copied set:", copy_set)

copy_set.clear()
print("After clear:", copy_set)
