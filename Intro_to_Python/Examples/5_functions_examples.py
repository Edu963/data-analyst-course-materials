
# Example 1: Drawing a Square
import turtle

def square(side_length):
    i = 1
    while i <= 4:
        turtle.forward(side_length)
        turtle.right(90)
        i += 1

if __name__ == "__main__":
    square(100)
    turtle.up()
    turtle.forward(130)
    turtle.down()
    square(50)

# Example 2: Calculating Distance
def distance(x1, y1, x2, y2):
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return d

if __name__ == "__main__":
    print(distance(1, 2, 1, 5))
    xA = 2
    yA = 3
    z = distance(xA, yA, 0, 0)
    print("Distance from (0,0) to A:", z)

# Example 3: Function without Arguments
import turtle

def standard_square():
    i = 1
    while i <= 4:
        turtle.forward(100)
        turtle.right(90)
        i += 1

def ask_name():
    name = input("What is your name?")
    return name

if __name__ == "__main__":
    name = ask_name()
    standard_square()

# Example 4: Side Effects vs. Return Values
def add(x, y):
    return x + y

def add_IO():
    x = float(input("x? "))
    y = float(input("y? "))
    print(x + y)

if __name__ == "__main__":
    result = add(5, 3)
    print(result)
    add_IO()

# Example 5: Using a Function inside Another Function
def move_without_drawing(distance):
    turtle.up()
    turtle.forward(distance)
    turtle.down()

def line_of_squares(num_squares, side_length):
    i = 0
    while i < num_squares:
        square(side_length)
        move_without_drawing(side_length + 10)
        i += 1

if __name__ == "__main__":
    line_of_squares(5, 50)
