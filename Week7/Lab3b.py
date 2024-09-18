class RequestSystem:
    def __init__(self, total_amount):
        self.total_amount = total_amount
        self.items = [] # Dictionary to store item names and their prices

    def request_details(self):
        while True:
            item = input("Please enter the name of the item (enter 'done' to exit): ")
            if item.lower() == 'done':
                break

            try:
                price = float(input(f"Enter the price of '{item}': "))
                self.total_amount += price
                print(f" Total Amount is: {self.total_amount:.2f}")
            except ValueError:
                print("Invalid price. Please enter a valid number.")
info = RequestSystem(0)
info.request_details()
