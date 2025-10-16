# =========================================================
# ✅ PYTHON STRING FUNCTIONS - COMPLETE EXAMPLE SCRIPT
# =========================================================

text = " Hello World! Welcome to Python Programming. "
text2 = "python"
text3 = "12345"
text4 = "Hello123"
text5 = "HELLO WORLD"
text6 = "hello world"
text7 = "Hello World"

print("========== Original Strings ==========")
print("text  =", text)
print("text2 =", text2)
print("text3 =", text3)
print("text4 =", text4)
print("text5 =", text5)
print("text6 =", text6)
print("text7 =", text7)

# ---------------------------------------------------------
print("\n========== 1. Case Conversion Functions ==========")
print("text.lower()       =", text.lower())      # Convert to lowercase
print("text.upper()       =", text.upper())      # Convert to uppercase
print("text.title()       =", text.title())      # Capitalize each word
print("text.capitalize()  =", text.capitalize()) # Capitalize first word only
print("text.swapcase()    =", text.swapcase())   # Swap upper/lower case

# ---------------------------------------------------------
print("\n========== 2. Whitespace Handling ==========")
print("text.strip()       =", text.strip())      # Remove leading/trailing spaces
print("text.lstrip()      =", text.lstrip())     # Remove leading spaces
print("text.rstrip()      =", text.rstrip())     # Remove trailing spaces

# ---------------------------------------------------------
print("\n========== 3. Searching and Finding ==========")
print("text.find('World')     =", text.find("World"))     # Index of substring (or -1)
print("text.rfind('o')        =", text.rfind("o"))        # Last occurrence
print("text.index('Python')   =", text.index("Python"))   # Like find() but raises error if not found
print("text.count('o')        =", text.count("o"))        # Count occurrences

# ---------------------------------------------------------
print("\n========== 4. Checking String Type ==========")
print("text2.islower()    =", text2.islower())   # All lowercase
print("text5.isupper()    =", text5.isupper())   # All uppercase
print("text3.isdigit()    =", text3.isdigit())   # Only digits
print("text4.isalnum()    =", text4.isalnum())   # Only letters and digits
print("text2.isalpha()    =", text2.isalpha())   # Only letters
print("text6.isspace()    =", text6.isspace())   # Only spaces (False here)
print("'   '.isspace()    =", "   ".isspace())   # Only spaces (True)
print("text7.istitle()    =", text7.istitle())   # Each word capitalized

# ---------------------------------------------------------
print("\n========== 5. Replace and Join ==========")
print("text.replace('Python', 'Java') =", text.replace("Python", "Java"))
words = ["Hello", "World", "Python"]
print("'-'.join(words) =", "-".join(words))     # Join list with separator

# ---------------------------------------------------------
print("\n========== 6. Splitting Strings ==========")
print("text.split()       =", text.split())        # Split by whitespace
print("text.split('o')    =", text.split("o"))     # Split by a specific character
print("text.rsplit('o',2) =", text.rsplit("o", 2)) # Split from right
print("text.partition('World') =", text.partition("World")) # Split into 3 parts (before, match, after)
print("text.rpartition('World') =", text.rpartition("World"))

# ---------------------------------------------------------
print("\n========== 7. Alignment Functions ==========")
print("text2.center(20,'-') =", text2.center(20, '-'))  # Center align
print("text2.ljust(20,'*')  =", text2.ljust(20, '*'))   # Left align
print("text2.rjust(20,'*')  =", text2.rjust(20, '*'))   # Right align
print("text2.zfill(10)      =", text2.zfill(10))        # Pad with zeros

# ---------------------------------------------------------
print("\n========== 8. Startswith / Endswith ==========")
print("text.startswith(' Hello') =", text.startswith(" Hello"))
print("text.endswith('ing.')     =", text.endswith("ing."))

# ---------------------------------------------------------
print("\n========== 9. Encoding and Formatting ==========")
print("text.encode() =", text.encode())  # Encode string to bytes
print("text2.format() =", "{} is awesome!".format(text2.capitalize()))
print("f-string example =", f"{text2.upper()} IS FUN!")

# ---------------------------------------------------------
print("\n========== 10. Miscellaneous ==========")
print("min(text2) =", min(text2))  # Smallest char alphabetically
print("max(text2) =", max(text2))  # Largest char alphabetically
print("len(text)  =", len(text))   # Length of string
print("text.expandtabs(4) =", "Hello\tWorld".expandtabs(4))  # Convert tabs to spaces
print("text.casefold() =", text.casefold())  # Stronger lowercase (for comparison)
print("'---'.strip('-') =", "---Python---".strip('-'))  # Remove specific char
print("text.removeprefix(' Hello') =", text.removeprefix(" Hello"))  # ✅ Python 3.9+
print("text.removesuffix('ing. ') =", text.removesuffix("ing. "))    # ✅ Python 3.9+

print("\n✅ All major string functions demonstrated successfully!")
