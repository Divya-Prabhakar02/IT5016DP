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
info = Patron("Shiv",2024)
info.rented("KOI HOR")
info.borrowed("Luna")
info.listbook()
        



