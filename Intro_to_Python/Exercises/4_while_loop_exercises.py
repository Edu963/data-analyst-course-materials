
# Exercise 1: Sum of First n Numbers
# Write a program that calculates the sum of the first n natural numbers
n = int(input("Enter a positive integer n: "))
total_sum = 0
i = 1

while i <= n:
    total_sum += i
    i += 1

print("The sum of the first", n, "numbers is:", total_sum)

# Exercise 2: Factorial Calculation
# Write a program that calculates the factorial of a number
n = int(input("Enter a positive integer n: "))
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print("The factorial of", n, "is:", factorial)

# Exercise 3: User Input Until Non-Zero
# Write a program that keeps asking the user for a number until they enter a non-zero value
number = 0

while number == 0:
    number = int(input("Enter a non-zero number: "))
    if number == 0:
        print("Zero is not allowed. Try again.")

print("You entered:", number)

# Exercise 4: Counting Digits
# Write a program that counts the number of digits in a positive integer
number = int(input("Enter a positive integer: "))
count = 0

while number > 0:
    number //= 10
    count += 1

print("The number of digits is:", count)

# Exercise 5: Multiplication Table
# Write a program that prints the multiplication table for a given number up to 10
number = int(input("Enter a number to get its multiplication table: "))
i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1

# Exercise 6: Guessing Game
# Write a program that implements a simple guessing game
import random
target = random.randint(1, 100)
guess = None

while guess != target:
    guess = int(input("Guess the number (between 1 and 100): "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")

print("Congratulations! You guessed the correct number:", target)
