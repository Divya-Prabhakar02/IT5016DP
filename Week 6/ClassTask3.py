class Car():
    def __init__(self,color, model , year):
        self.color = color
        self.model = model
        self.year = year
    def car1(self):
        print(self.color(), self.model(), self.year())
    def car2(self):
        print(self.color(), self.model(), self.year())
    def car3(self):
        print(self.color(),self.model(), self.year())
    
car1 = ("black","2024","Honda")
car2 = ("red","2021","swift")
car3 = ("grey", "2020", "Aqua")

print(car1)
print(car2)
print(car3)



