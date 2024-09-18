class Car():
    def __init__(self,color, year, model):
        self.color = color
        self.model = model
        self.year = year
    def drive(self):
        print(f"The {self.model} is driving")
    def stop(self):
        print(f"The {self.model} has stopped")
    def carinfo(self):
        print(f"Car Info, {self.year} {self.model} {self.color}")
car1 = Car("black","2024","Honda")
car1.carinfo()
car1.drive()
car1.stop()


