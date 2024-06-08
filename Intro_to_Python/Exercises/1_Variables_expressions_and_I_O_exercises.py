# Exercise 1: Basic Variable Assignment
# Assign the value 10 to a variable named 'a'
# Print the value of 'a'

a = 10
print(a)

# Exercise 2: User Input
# Prompt the user to enter their favorite color
# Print a message saying "Your favorite color is [color]"

color = input("Enter your favorite color: ")
print("Your favorite color is", color)

# Exercise 3: Arithmetic Operations
# Given two variables x and y, calculate and print:
# 1. Their sum
# 2. Their difference
# 3. Their product
# 4. The result of x divided by y
# 5. The result of x to the power of y

x = 15
y = 4
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Division:", x / y)
print("Exponentiation:", x ** y)

# Exercise 4: String Concatenation
# Given two strings first_name and last_name,
# concatenate them to create a full_name
# Print the full_name

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# Exercise 5: Comparison Operations
# Write a program that compares two numbers a and b
# and prints whether a is greater than, less than, or equal to b

a = 20
b = 25
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# Exercise 6: Logical Operations
# Write a program that takes two boolean variables is_raining and is_sunny
# Print a message depending on their values:
# - If both are true, print "Rainbow"
# - If only is_raining is true, print "Take an umbrella"
# - If only is_sunny is true, print "Wear sunglasses"
# - If neither is true, print "Stay inside"

is_raining = True
is_sunny = False
if is_raining and is_sunny:
    print("Rainbow")
elif is_raining:
    print("Take an umbrella")
elif is_sunny:
    print("Wear sunglasses")
else:
    print("Stay inside")