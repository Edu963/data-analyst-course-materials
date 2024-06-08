# Exercise 1: Create a dictionary of student grades and print it
grades = {'alice': 14, 'bob': 18, 'charlie': 11}
print(grades)

# Exercise 2: Add a new student's grade to the dictionary
grades['david'] = 15
print(grades)

# Exercise 3: Remove a student from the dictionary
del grades['charlie']
print(grades)

# Exercise 4: Check if a student is in the dictionary
print('alice' in grades)  # Output: True
print('charlie' in grades)  # Output: False

# Exercise 5: Traverse the dictionary and print each student's grade
for student in grades:
    print(student, 'has a grade of', grades[student])

# Exercise 6: Copy the dictionary and modify the copy
grades_copy = dict(grades)
grades_copy['eve'] = 17
print(grades_copy)
print(grades)
