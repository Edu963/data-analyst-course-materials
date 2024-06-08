
# Exercise 1: String Length
# Write a program that reads a string from the user and prints its length

user_string = input("Enter a string: ")
print("The length of the string is:", len(user_string))

# Exercise 2: String Concatenation
# Write a program that reads two strings from the user and prints their concatenation

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print("Concatenated string:", str1 + " " + str2)

# Exercise 3: String Repetition
# Write a program that reads a string and a number from the user, and prints the string repeated that many times

user_string = input("Enter a string: ")
repeat_count = int(input("Enter a number: "))
print("Repeated string:", user_string * repeat_count)

# Exercise 4: Logical OR
# Write a program that checks if either of two given conditions is true

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > 0 or b > 0:
    print("At least one of the numbers is positive")
else:
    print("Neither number is positive")

# Exercise 5: Logical AND
# Write a program that checks if both of two given conditions are true

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > 0 and b > 0:
    print("Both numbers are positive")
else:
    print("At least one of the numbers is not positive")

# Exercise 6: De Morgan's Laws
# Write a program to verify De Morgan's laws

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("not (a > 2 or b <= 4):", not (a > 2 or b <= 4))
print("(a <= 2) and (b > 4):", (a <= 2) and (b > 4))

print("not (a > 2 and b <= 4):", not (a > 2 and b <= 4))
print("(a <= 2) or (b > 4):", (a <= 2) or (b > 4))
