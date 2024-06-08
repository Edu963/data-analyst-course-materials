# Example 1: Variable Assignment and Types
n = 33
a = 42 + 25
ch = "hello"
euro = 6.55957
is_equal = (4 == 2 + 2)

print("Integer:", n)
print("Sum:", a)
print("String:", ch)
print("Float:", euro)
print("Boolean:", is_equal)

# Example 2: Input and Output
name = input("Enter your name: ")
print("Hello, " + name + "!")

age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Example 3: Arithmetic Operations
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulo:", x % y)
print("Exponentiation:", x ** y)

# Example 4: String Operations
greeting = "Hello"
name = "World"
full_greeting = greeting + " " + name
print(full_greeting)

# Example 5: Comparison and Logical Operations
a = 5
b = 10
print("a == b:", a == b)
print("a != b:", a != b)
print("a < b:", a < b)
print("a > b:", a > b)
print("a <= b:", a <= b)
print("a >= b:", a >= b)
print("Logical AND:", a < b and b == 10)
print("Logical OR:", a > b or b == 10)
print("Logical NOT:", not(a > b))

# Example 6: Dynamic Typing
x = 5
print("Type of x:", type(x))
x = "hello"
print("Type of x:", type(x))
x = 3.14
print("Type of x:", type(x))
