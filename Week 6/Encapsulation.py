class Person():
    def __init__(self):
        self.A = "James"
        self.__B = "James Bond"
    def Printname(self):
        print(self.A)
        print(self.__B)
p= Person()

p.A
p.__B
p.Printname()


