
# Exercise 1: Write a function to calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Factorial of", num, "is", factorial(num))

# Exercise 2: Write a function to calculate the area of a circle
def area_of_circle(radius):
    return 3.14159 * (radius ** 2)

if __name__ == "__main__":
    r = float(input("Enter the radius: "))
    print("Area of the circle is:", area_of_circle(r))

# Exercise 3: Write a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

# Exercise 4: Write a function to find the maximum of three numbers
def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == "__main__":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    print("The maximum value is:", maximum(a, b, c))

# Exercise 5: Write a function to generate the Fibonacci sequence up to n terms
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    num = int(input("Enter the number of terms: "))
    print("Fibonacci sequence:", fibonacci(num))
