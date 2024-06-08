# Example 1: Iterating over a list of numbers
for e in [1, 4, 5, 0, 9, 1]:
    print(e)

# Example 2: Iterating over a list of characters
for e in ["a", "e", "i", "o", "u", "y"]:
    print(e)

# Example 3: Iterating over a string
for e in "python":
    print(e)

# Example 4: Basic range example
for i in range(1, 6):
    print(i, end=",")  # Output: 1,2,3,4,5,

# Example 5: Range with different parameters
for i in range(4):
    print(i)  # Output: 0, 1, 2, 3

for j in range(2, 5):
    print(j)  # Output: 2, 3, 4

for k in range(3, 12, 3):
    print(k)  # Output: 3, 6, 9

for l in range(12, 3, -2):
    print(l)  # Output: 12, 10, 8, 6, 4

# Example 6: Inconsistent range
for k in range(200, 210, -2):
    print(k)  # This loop is ignored

for k in range(110, 100, -2):
    print(k)  # Output: 110, 108, 106, 104, 102

# Example 7: Loop variable modification inside the loop
for i in range(1, 5):
    print(i)
    i = i * 2  # This modification does not affect the loop's progression
