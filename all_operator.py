# ==============================================
# ✅ PYTHON OPERATORS - COMPLETE EXAMPLE SCRIPT
# ==============================================

# Example variables
a = int(input("enter a no: "))
b = 3
x = True
y = False
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
string1 = "Hello"
string2 = "World"

print("========== 1. Arithmetic Operators ==========")
print("a + b =", a + b)    # Addition
print("a - b =", a - b)    # Subtraction
print("a * b =", a * b)    # Multiplication
print("a / b =", a / b)    # Division
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)    # Modulus
print("a ** b =", a ** b)  # Exponentiation

print("\n========== 2. Assignment Operators ==========")
c = a
print("c =", c)
c += b
print("c += b ->", c)
c -= b
print("c -= b ->", c)
c *= b
print("c *= b ->", c)
c /= b
print("c /= b ->", c)
c %= b
print("c %= b ->", c)
c **= b
print("c **= b ->", c)
c //= b
print("c //= b ->", c)

print("\n========== 3. Comparison Operators ==========")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n========== 4. Logical Operators ==========")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\n========== 5. Bitwise Operators ==========")
print("a & b (AND):", a & b)
print("a | b (OR):", a | b)
print("a ^ b (XOR):", a ^ b)
print("~a (NOT):", ~a)
print("a << 1 (Left Shift):", a << 1)
print("a >> 1 (Right Shift):", a >> 1)

print("\n========== 6. Identity Operators ==========")
print("a is b:", a is b)
print("a is not b:", a is not b)
print("list1 is list2:", list1 is list2)
print("list1 is not list2:", list1 is not list2)

print("\n========== 7. Membership Operators ==========")
print("2 in list1:", 2 in list1)
print("7 not in list1:", 7 not in list1)
print("'H' in string1:", 'H' in string1)
print("'W' not in string1:", 'W' not in string1)

print("\n✅ All operator types demonstrated successfully!")
