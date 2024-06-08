
# Example 1: Simple if statement
number = int(input("Enter a number: "))
if number > 0:
    print(number, "is positive")

# Example 2: If...Else statement
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Example 3: If...Elif...Else statement
score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Example 4: Nested If statements
age = int(input("Enter your age: "))
if age >= 18:
    if age >= 65:
        print("You are a senior citizen")
    else:
        print("You are an adult")
else:
    print("You are a minor")
