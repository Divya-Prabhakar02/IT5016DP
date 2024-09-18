class Library():
    def __init__(self):
       self.books = []
    def add(self,title):
        if title not in self.books:
            self.books.append(title)
            print(f"{title} is added")
        else:
            print(f"No Books is Added.")
class Patron():
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.patronbooks = []
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
b1 = Library()
b1.add("luna")
p1 = Patron("SAM",101)
p1.newpatron("KIM")
p1.display("KIM")
p1.remove("KIM")



        



    

