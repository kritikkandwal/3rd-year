# 📘 Dictionary All Functions and Operations

# Creating a dictionary
student = {
    "name": "Kritik",
    "age": 21,
    "branch": "CSE",
    "marks": 89
}

print("Original Dictionary:", student)

# ---------------------------------------------------------
print("\n========== 1. Accessing Values ==========")
print("Name:", student["name"])
print("Branch (using get):", student.get("branch"))
print("Unknown key (get):", student.get("grade", "Not Found"))

# ---------------------------------------------------------
print("\n========== 2. Adding & Updating ==========")
student["city"] = "Dehradun"              # Add new key
student.update({"marks": 92, "gender": "Male"})  # Update multiple
print("After update:", student)

# ---------------------------------------------------------
print("\n========== 3. Removing Elements ==========")
student.pop("city")        # Remove key
print("After pop:", student)
student.popitem()          # Remove last inserted key
print("After popitem:", student)
del student["age"]         # Delete specific key
print("After del:", student)

# ---------------------------------------------------------
print("\n========== 4. Dictionary Copy ==========")
copy_dict = student.copy()
print("Copied dict:", copy_dict)

# ---------------------------------------------------------
print("\n========== 5. Dictionary Keys, Values, Items ==========")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# ---------------------------------------------------------
print("\n========== 6. Looping Through Dictionary ==========")
for key in student:
    print(f"{key} → {student[key]}")

# ---------------------------------------------------------
print("\n========== 7. Nested Dictionary ==========")
students = {
    "stu1": {"name": "Kritik", "age": 21},
    "stu2": {"name": "Abhishek", "age": 22}
}
print("Nested dict:", students)
print("stu1 name:", students["stu1"]["name"])

# ---------------------------------------------------------
print("\n========== 8. Fromkeys & Setdefault ==========")
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("Fromkeys:", new_dict)
print("Setdefault (before):", student)
student.setdefault("country", "India")   # Adds only if not present
print("After setdefault:", student)

# ---------------------------------------------------------
print("\n========== 9. Clear Dictionary ==========")
temp = {"x": 1, "y": 2}
print("Before clear:", temp)
temp.clear()
print("After clear:", temp)
