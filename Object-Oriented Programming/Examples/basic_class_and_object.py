class Animal:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def move(self):
        pass  # Placeholder method

# Creating an instance of Animal
animal = Animal(50, 150)
print(f"Weight: {animal.weight}, Height: {animal.height}")
