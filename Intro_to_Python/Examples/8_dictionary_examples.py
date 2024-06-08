# Example 1: Creating a dictionary
notes = { 'quentin': 15.5, 'nathan': 12.0 }
print(notes)

# Example 2: Accessing values by key
print(notes['quentin'])  # Output: 15.5

# Example 3: Adding new entries
D = {}
D['a'] = 1
print(D)  # Output: {'a': 1}

D['a'] = 3
print(D)  # Output: {'a': 3}

# Example 4: Removing entries
D = {'a': 1, 'b': 2, 'c': 3}
del D['a']
print(D)  # Output: {'b': 2, 'c': 3}

# Example 5: Checking for existence of a key
prices = {'asus': 450, 'alienware': 1200, 'lenovo': 680}
print('asus' in prices)  # Output: True
print('toshiba' in prices)  # Output: False

# Example 6: Handling missing keys
letters = {'a': 103, 'b': 8, 'e': 150}

if 'u' in letters:
    letters['u'] = letters['u'] + 1
else:
    letters['u'] = 1

print(letters)

# Example 7: Traversing a dictionary
birthdays = {'ingrid': [12, 6, 1995], 'marc': [27, 8, 1996], 'brice': [11, 10, 1995]}

for name in birthdays:
    date = birthdays[name]
    print(name, 'will celebrate their birthday on', date[0], '/', date[1], '/2017')

# Example 8: Copying dictionaries
D = {1: 10, 2: 20, 3: 30}
E = dict(D)
E[5] = 50
print(E)  # Output: {1: 10, 2: 20, 3: 30, 5: 50}
print(D)  # Output: {1: 10, 2: 20, 3: 30}
