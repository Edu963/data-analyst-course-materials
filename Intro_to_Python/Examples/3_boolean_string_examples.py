
# Example 1: String Definitions
print("Hello, World!")
print('Hello, World!')
print("""Hello, 
World!""")

# Example 2: String Operations
s = "hello"
print("Length of s:", len(s))
print("Concatenation:", "hello" + " world")
print("Repetition:", "hello " * 3)

# Example 3: Logical OR
a = 5
print((2 == 1 + 1) or (a >= 5))  # True
# print((3 == 1 + 1) or (b >= 5))  # Uncommenting this line will cause an error if b is not defined

# Example 4: Logical AND
print((2 > 8) and (a >= 5))  # False
# print((2 < 8) and (b >= 5))  # Uncommenting this line will cause an error if b is not defined

# Example 5: De Morgan's Laws
b = 3
print(not (a > 2 or b <= 4))  # False
print((a <= 2) and (b > 4))  # False

print(not (a > 2 and b <= 4))  # True
print((a <= 2) or (b > 4))  # True
