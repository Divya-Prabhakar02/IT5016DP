class RequestSystem:
    unique_id_counter = 0  # Global unique ID counter

    def __init__(self):
        RequestSystem.unique_id_counter += 1
        self.request_id = RequestSystem.unique_id_counter
        self.name = ""
        self.age = 0
        self.email = ""
        self.items = []
        self.total_amount = 0
        self.status = "pending"

    def user_info(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.email = input("Enter your email: ")

    def request_details(self):
        while True:
            item = input("Enter the item name (or 'done' to finish): ").strip()
            if item.lower() == 'done':
                break
            price = float(input(f"Enter the price of {item}: "))
            self.items.append((item, price))
            self.total_amount += price
        print(f"Total amount requested: {self.total_amount:.2f}")

    def request_approval(self):
        if self.total_amount < 150:
            self.status = "approved"
        else:
            self.status = "pending"
        print(f"Request status: {self.status}")

    def respond_request(self, manager_response):
        if manager_response.lower() == 'approved':
            self.status = "approved"
        elif manager_response.lower() == 'not approved':
            self.status = "not approved"
        print(f"Manager's response: {self.status}")

    def display_request(self):
        print("\nRequest Summary:")
        print(f"Request ID: {self.request_id}")
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")
        print(f"Items requested:")
        for item, price in self.items:
            print(f" - {item}: ${price:.2f}")
        print(f"Total Amount: ${self.total_amount:.2f}")
        print(f"Request Status: {self.status}")

    @classmethod
    def request_stats(cls, requests):
        total_requests = len(requests)
        approved_requests = sum(1 for req in requests if req.status == "approved")
        print(f"\nTotal number of requests: {total_requests}")
        print(f"Total number of approved requests: {approved_requests}")


# Example usage:

# Creating a new request
request1 = RequestSystem()
request1.user_info()
request1.request_details()
request1.request_approval()

# Manager responds to the request
request1.respond_request("approved")

# Display the request details
request1.display_request()

# To display statistics for multiple requests, create more requests
request2 = RequestSystem()
request2.user_info()
request2.request_details()
request2.request_approval()

# Add all requests to a list
requests = [request1, request2]

# Display statistics
RequestSystem.request_stats(requests)

