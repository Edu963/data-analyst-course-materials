
# Example 1: Division with While Loop
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))

while b == 0:
    b = int(input("B is zero! Try again: "))

print("A / B =", a // b)

# Example 2: Avoiding Infinite Loop
n = 5
while n < 10:
    print("n is:", n)
    n += 1  # increment to avoid infinite loop
print("End")

# Example 3: Loop Counter
i = 0  # counter variable

while i < 10:
    print(2 ** i)  # 2 to the power of i
    i += 1  # increment the counter
print("End")

# Example 4: Accumulator
i = 1
total_sum = 0  # initially, the sum is 0

while i <= 10:
    total_sum += i  # add each value of i to the sum (accumulation)
    i += 1  # never forget to update the counter

print("The sum of the first 10 integers is:", total_sum)

# Example 5: Flag Variable
i = 0
all_odd = True

while i < 10:
    x = int(input("Enter an integer: "))
    all_odd = all_odd and (x % 2 != 0)
    i += 1

if all_odd:
    print("All entered numbers are odd")
else:
    print("At least one entered number was not odd")

# Example 6: Break Keyword
i = 1

while i < 100:
    if i % 2 == 0:
        print("*")
        break  # exit the loop
    i += 1

print("Incrementing i")
print("End")

# Example 7: Continue Keyword
i = 1

while i < 100:
    if i % 2 == 0:
        print("*")
        continue  # skip the rest of the loop
    i += 1

print("Incrementing i")
print("End")

# Example 8: Nested Loops
i = 1

while i <= 3:
    j = 1
    while j <= 2:
        print(i, ", ", j)
        j += 1
    i += 1
