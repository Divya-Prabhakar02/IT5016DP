'''class Book():
    def __init__(self,title,author,publication_year):
        self.title = title
        self.author = author
        self.publicationyear = publication_year
        self.availability = True
    def display(self):
        print(f"Details\n Title: {self.title} \n Author: {self.author} \n Publication Year = {self.publicationyear} \n" 'Available' if self.availability else "Rented")
class Patron():
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.bbooks = []
    def borrowed(self,title):
        if title not in self.bbooks:
            self.bbooks.append(title)
            print(f"You have borrowed {title}")
        else:
            print(f"{title} is not available")
    def rented(self,title):
        if title  in self.bbooks:
            self.bbooks.remove(title)
            print(f"This {title} is rented.")
        else:
            print(f"This {title} is available.")
    def listbook(self):
        if self.bbooks:
            print(f"{self.bbooks}")   
        else:
            print("No book is borrowed.")
class Library():
    def __init__(self):
       self.books = []
       self.patronbooks = []
    def add(self,title):
        if title not in self.books:
            self.books.append(title)
            print(f"{title} is added")
        else:
            print(f"No Books is Added.")
    def newpatron(self,pname):
        if pname not in self.patronbooks:
            self.patronbooks.append(pname)
            print(f"{pname} has be added.")
        else:
            print("Nothing New.")
    def display(self,pname):
        if self.patronbooks:
            print(f"Registered patron: {pname}")
        else:
            print("Nothing is registered")
    def remove(self,pname):
        if pname in self.patronbooks:
            self.patronbooks.remove(pname)
            print(f"{pname} has been removed.")
        else:
            print("Nothing is changed.")



def main():
    library = Library()
    
    while True:
        print("\nLibrary Menu")
        print("1. Add book")
        print("2. Register patron")
        print("3. Borrow book")
        print("4. Return book")
        print("5. List borrowed books")
        print("6. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publication_year = input("Enter publication year: ")
            book = Book(title, author, publication_year)
            library.add()
        
        elif choice == '2':
            name = input("Enter patron name: ")
            id = input("Enter patron ID: ")
            patron = Patron(name, id)
            library.display(patron)
        
        elif choice == '3':
            name = input("Enter patron name: ")
            title = input("Enter book title: ")
           
            if patron  and book:
                patron.borrowed(book)
            else:
                print(" book not found.")
        elif choice == '5':
            name = input("Enter patron name: ")
            patron.listbook()
            if patron:
                patron.list_borrowed_books()
            else:
                print("Patron not found.")
        
        elif choice == '6':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main() '''       
'''elif choice == '4':
            name = input("Enter patron name: ")
            title = input("Enter book title: ")
            patron = library.find_patron(name)
            book = library.find_book(title)
            if patron and book:
                patron.return_book(book)
            else:
                print("Patron or book not found.")
'''

















