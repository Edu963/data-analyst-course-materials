'''
Exercise 2: Implement Inheritance

1. Create a base class Employee with attributes name and salary.
2. Create a derived class Manager that inherits from Employee and adds an additional attribute department.
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department 

    def get_details(self):
        return f"Manager {self.name}, Department: {self.department}, Salary: {self.salary}"

# Create an instance of Manager
manager = Manager("Alice", 90000, "HR")
print(manager.get_details()) 
