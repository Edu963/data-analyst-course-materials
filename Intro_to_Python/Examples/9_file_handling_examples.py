# Example 1: Reading from a file
f = open('data.txt')
text = f.read()
print(text)
f.close()

# Example 2: Reading lines from a file
f = open('data.txt')
lines = f.readlines()
print(lines)
f.close()

# Example 3: Reading a file line by line
f = open('data.txt')
for line in f:
    print(line.strip())
f.close()

# Example 4: Writing to a file
f = open('output.txt', 'w')
f.write('Hello, World!\n')
f.write('This is a test.\n')
f.close()

# Example 5: Appending to a file
f = open('output.txt', 'a')
f.write('Appending this line.\n')
f.close()

# Example 6: Calculating the sum of integers in a file
f = open('numbers.txt')
sum = 0
for number in f:
    sum += int(number)
print(sum)
f.close()

# Example 7: Writing the first 10 powers of 2 to a file
f = open('powers.txt', 'w')
for i in range(10):
    f.write(str(2 ** i) + '\n')
f.close()
