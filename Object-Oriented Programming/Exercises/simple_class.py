#Exercise 1: Create a Simple Class and Object

#Create a Book class with attributes like title, author, and pages.
#Instantiate the Book class and print the book details.

class Book:
    def __init__ (self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    
# Create an instance of Book
book = Book("1984", "George Orwell", 328)

print(book.get_info())