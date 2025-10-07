# ✅ Simple & Clear — All Tuple Operations

# Create tuple
tup = (10, 20, 30, 40, 50)
print("Original tuple:", tup)

# Access elements
print("First element:", tup[0])
print("Last element:", tup[-1])

# Slicing
print("First 3 elements:", tup[:3])
print("Every 2nd element:", tup[::2])

# Count & index
print("Count of 20:", tup.count(20))
print("Index of 30:", tup.index(30))

# Concatenation
tup2 = (60, 70)
new_tup = tup + tup2
print("After concatenation:", new_tup)

# Repetition
print("Repetition:", tup * 2)

# Check & length
print("Is 40 in tuple?", 40 in tup)
print("Length of tuple:", len(tup))

# Convert to list (to modify)
temp_list = list(tup)
temp_list.append(99)
tup = tuple(temp_list)
print("After converting to list & adding 99:", tup)

# Loop
print("Elements in tuple:")
for x in tup:
    print(x)
