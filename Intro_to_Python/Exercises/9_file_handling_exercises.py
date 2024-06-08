# Exercise 1: Write a program to read a file and print its content
def read_file(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    print(content)

# Exercise 2: Write a program to read lines from a file into a list
def read_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines

# Exercise 3: Write a program to write user input to a file
def write_user_input(file_name):
    user_input = input("Enter some text: ")
    with open(file_name, 'w') as f:
        f.write(user_input)

# Exercise 4: Write a program to append user input to a file
def append_user_input(file_name):
    user_input = input("Enter some text to append: ")
    with open(file_name, 'a') as f:
        f.write(user_input + '\n')

# Exercise 5: Write a program to calculate the sum of integers in a file
def sum_integers(file_name):
    sum = 0
    with open(file_name, 'r') as f:
        for number in f:
            sum += int(number)
    return sum

# Exercise 6: Write a program to save the first 10 powers of 3 in a file
def save_powers(file_name):
    with open(file_name, 'w') as f:
        for i in range(10):
            f.write(str(3 ** i) + '\n')
