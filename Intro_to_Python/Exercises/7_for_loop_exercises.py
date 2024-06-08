# Exercise 1: Create a range from 4 and print each value
for i in range(4):
    print(i)  # Output: 0, 1, 2, 3

# Exercise 2: Create a range from 2 to 5 and print each value
for j in range(2, 5):
    print(j)  # Output: 2, 3, 4

# Exercise 3: Create a range from 3 to 12 with a step of 3 and print each value
for k in range(3, 12, 3):
    print(k)  # Output: 3, 6, 9

# Exercise 4: Create an inconsistent range from 12 to 3 and print each value
for l in range(12, 3):
    print(l)  # No output, as the loop range is inconsistent

# Exercise 5: Create a range from 12 to 3 with a step of -2 and print each value
for m in range(12, 3, -2):
    print(m)  # Output: 12, 10, 8, 6, 4

# Exercise 6: Calculate the sum of positive numbers in a list
def sum_of_positives(lst):
    s = 0
    for e in lst:
        if e > 0:
            s += e
    return s

# Main program
my_list = [2, -4, 6, 0, -5, 1]
for e in my_list:
    print(e + 1)

total = sum_of_positives(my_list)
print(total)  # Output: 9
