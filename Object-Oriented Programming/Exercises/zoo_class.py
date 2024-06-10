class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            print(f"Animal: {animal}")

zoo = Zoo()
zoo.add_animal("Lion")
zoo.add_animal("Elephant")
zoo.list_animals()