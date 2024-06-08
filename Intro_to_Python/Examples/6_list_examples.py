# Example 1: Creating and Accessing Lists
Weekend = ["Saturday", "Sunday"]
print(Weekend[0])  # Output: 'Saturday'

# Example 2: Appending to a List
Multiple3 = [3, 6, 9]
Multiple3.append(21)
print(Multiple3)  # Output: [3, 6, 9, 21]

# Example 3: Inserting and Extending Lists
Multiple3.insert(3, 15)
print(Multiple3)  # Output: [3, 6, 9, 15, 21]
Multiple3.extend([24, 27])
print(Multiple3)  # Output: [3, 6, 9, 15, 21, 24, 27]

# Example 4: Popping and Removing Elements
a = Multiple3.pop(0)
print(a)  # Output: 3
print(Multiple3)  # Output: [6, 9, 15, 21, 24, 27]
Multiple3.remove(24)
print(Multiple3)  # Output: [6, 9, 15, 21, 27]

# Example 5: Checking Membership
def search(elem, l):
    if elem in l:
        return True
    else:
        return False

my_list = [2, 5, 8, 12, 17, 25]
found = search(12, my_list)
print(found)  # Output: True
found = search(6, my_list)
print(found)  # Output: False

# Example 6: Side Effects on Lists
def add_start_end(l, start_elem, end_elem):
    l.insert(0, start_elem)
    l.append(end_elem)

my_list = [2, 3, 4]
add_start_end(my_list, 1, 5)
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Example 7: Avoiding Undesired Side Effects
import random

def add_random(l):
    """Returns a list obtained from l by adding a random integer between 5 and 10."""
    x = random.randint(5, 10)
    new_list = list(l)  # copy the list
    new_list.append(x)
    return new_list

original_list = [1, 2, 3]
new_list = add_random(original_list)
print(original_list)  # Output: [1, 2, 3]
print(new_list)  # Output: [1, 2, 3, <random_number>]
