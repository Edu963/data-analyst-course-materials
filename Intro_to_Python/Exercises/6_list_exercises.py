# Exercise 1: Create a list of the first 10 multiples of 3 and print it
multiples_of_3 = [3 * i for i in range(1, 11)]
print(multiples_of_3)

# Exercise 2: Write a function to find the maximum element in a list
def find_max(l):
    max_elem = l[0]
    for elem in l:
        if elem > max_elem:
            max_elem = elem
    return max_elem

my_list = [4, 2, 8, 6, 5, 7, 3]
print("The maximum element is:", find_max(my_list))

# Exercise 3: Write a function to reverse a list
def reverse_list(l):
    return l[::-1]

my_list = [1, 2, 3, 4, 5]
print("Reversed list:", reverse_list(my_list))

# Exercise 4: Write a function to remove duplicates from a list
def remove_duplicates(l):
    return list(set(l))

my_list = [1, 2, 3, 2, 4, 1, 5, 3]
print("List without duplicates:", remove_duplicates(my_list))

# Exercise 5: Write a function to merge two lists without duplicates
def merge_lists(l1, l2):
    return list(set(l1 + l2))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print("Merged list:", merge_lists(list1, list2))

# Exercise 6: Write a function to find the intersection of two lists
def intersection(l1, l2):
    return list(set(l1) & set(l2))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print("Intersection:", intersection(list1, list2))
