class BankAccountSysytem:
    def __init__(self,account_no,account_holder_name, balance):
        self.account_no = account_no
        self.account_holder_name = account_holder_name
        self.balance = balance
    def deposit(self,amount):
        self.balance+= amount
    def withdraw(self,amount):
        self.balance-=amount
    def check_balance(self):
        return self.balance
acc = BankAccountSysytem(2222,"Divya",500)
print(acc.account_holder_name)
acc.deposit(100)
acc.withdraw(50)
print(acc.check_balance())

