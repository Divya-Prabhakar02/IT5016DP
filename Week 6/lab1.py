class Car():
    def __init__(self,color, model , year):
        self.color = color
        self.model = model
        self.year = year
    def drive(self):
        print(f"{self.model} {self.year} is driving ")
    def stop(self):
        print(f"{self.model}{self.year} has stopped")
    def display_info(self):
        print(f"Car Info:{self.model}{self.year}{self.color}")
class ElectricCar(Car):
    def __init__(self, color, model, year, battery_capacity):
        super().__init__(color, model, year)
        self.battery_capacity = battery_capacity
        print(f"battery capacity  is  {self.battery_capacity}km/hr")

    def display_info(self):
        return super().display_info()
my_car = ElectricCar("Swift","Black",2021,450)
my_car.drive()
my_car.stop()
my_car.display_info()
