class Employee():
    def __init__(self,salary=0):
        self.salary = salary
    def get_salary(self):
        return self.salary
class Manager(Employee):
    def get_salary(self):
        return super().get_salary()
money = Employee(30000)
print(money.get_salary())
money = Manager(50000)
print(money.get_salary())