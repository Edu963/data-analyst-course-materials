
# Exercise 1: Check if a number is positive, negative, or zero
# Write a program that reads a number and prints whether it is positive, negative, or zero

number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Exercise 2: Leap Year Checker
# Write a program to check if a year is a leap year.
# A year is a leap year if it is divisible by 4 but not by 100, except if it is also divisible by 400

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Exercise 3: BMI Calculator
# Write a program that calculates the Body Mass Index (BMI) and prints the BMI category:
# Underweight, Normal weight, Overweight, Obese

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obese")

# Exercise 4: Number Comparison
# Write a program that compares three numbers and prints the largest one

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a > b and a > c:
    print("The largest number is", a)
elif b > a and b > c:
    print("The largest number is", b)
else:
    print("The largest number is", c)

# Exercise 5: Grading System
# Write a program that takes a score (0-100) as input and prints the corresponding grade:
# A (90-100), B (80-89), C (70-79), D (60-69), F (0-59)

score = int(input("Enter your score (0-100): "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
