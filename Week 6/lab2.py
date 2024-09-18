class Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance
    def deposit(self,amount):
        if amount >0:
            self._balance += amount 
            print(f"{amount} Deposited")
        else:
            print("The amount is positive")
    def withdraw(self,amount):
        if 0< amount <= self._balance:
            self._balance -= amount
            print(f"{amount} Withdraw")
        else:
             print("Amount is Negative")
           
    def get_balance(self):
            return self._balance

account = Account("Divya",500)
print(account.owner)
account.deposit(50)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())


        