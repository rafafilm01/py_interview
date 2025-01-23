# create a pet class 
class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

# methods for pet
    def make_sound(self):
        if self.species.lower() == "dog":
            return "Woof!"
        elif self.species.lower() == "cat":
            return "Meow!"
        elif self.species.lower() == "fish":
            return "Fish make no sound !"
        else:
            return "The animal makes a sound."
    
    def celebrate_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! You are now {self.age} years old!"
        
    def get_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nSpecies: {self.species}"
    
    
dog = Pet("brian", 3, "dog")

print(dog.get_info())
print(dog.make_sound())

# exercise 4 -- library book Book class to manage library books 
class Book:
    def __init__(self, title: str, author: str, isbn: int, is_checked_out: bool) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out
        
    #property decorator used to make sure correct attribute type is provided , need to have getter and setter in order to work . With this set up , the values provided when the class is initialzised will be checked at runtime 
    # @property
    # def is_checked_out(self) -> bool:
    #     return self.is_checked_out
    
    # @is_checked_out.setter
    # def is_checked_out(self, value):
    #     if not isinstance(value, bool): 
    #         raise TypeError("is_checked_out must type boolean")
        
    # methods for Book class 
    def check_out(self):    
        if self.is_checked_out:
            return ("the book has already been borrowed")
        else:
            self.is_checked_out = True
    
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return "the book has been returned"
        else:
            return "the book was in the library all along "
        
    
    def get_due_date(self):
        if self.is_checked_out:
            return "The book is due back next Monday"
        return "Book is not checked out"
    
    def display_book_info(self):
        return(f"book info : \n{self.title}\n{self.author}\n{self.isbn}\nCurrently on lease : {self.is_checked_out}")
        
        
# Create some sample books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 9780743273565, False)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 9780446310789, True)
book3 = Book("1984", "George Orwell", 9780451524935, False)

# Test the books
print(book1.display_book_info())
print("\n")
print(book2.display_book_info())
print("\n") 
print(book3.display_book_info())

print(book2.check_out())
print("------")
print(book2.display_book_info())
print(book2.return_book())
print(book2.display_book_info())