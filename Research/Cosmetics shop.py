class CosmeticsShop:
    product_id_counter = 1000  # Global product ID counter

    def __init__(self):
        self.products = []  # List to store all products
        self.customers = []  # List to store all customers

    def add_product(self):
        """Add a new product to the shop."""
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter initial quantity: "))
        product = {
            "id": self.generate_product_id(),
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.products.append(product)
        print(f"Product '{name}' added with ID {product['id']}")

    def generate_product_id(self):
        """Generate a unique product ID and increment the global counter."""
        product_id = CosmeticsShop.product_id_counter + 1
        CosmeticsShop.product_id_counter += 1
        return product_id

    def add_customer(self):
        """Add a new customer to the shop."""
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        customer = {
            "name": name,
            "email": email
        }
        self.customers.append(customer)
        print(f"Customer '{name}' added")

    def display_products(self):
        """Print all products in the shop."""
        print("\n============================")
        print("        Products        ")
        print("============================")
        if not self.products:
            print("No products in the shop yet.")
        else:
            print("ID   Product Name   Price   Quantity")
            for product in self.products:
                print(f"{product['id']}   {product['name']}   ${product['price']:.2f}   {product['quantity']}")

    def display_customers(self):
        """Print all customers in the shop."""
        print("\n============================")
        print("        Customers        ")
        print("============================")
        if not self.customers:
            print("No customers in the shop yet.")
        else:
            print("Name           Email")
            for customer in self.customers:
                print(f"{customer['name']}   {customer['email']}")

    def make_purchase(self):
        """Make a purchase as a customer."""
        customer_name = input("Enter your name: ")
        customer_email = input("Enter your email: ")
        customer = next((c for c in self.customers if c["name"] == customer_name and c["email"] == customer_email), None)
        if customer:
            product_id = int(input("Enter the product ID: "))
            product = next((p for p in self.products if p["id"] == product_id), None)
            if product:
                quantity = int(input("Enter the quantity to purchase: "))
                if quantity <= product["quantity"]:
                    product["quantity"] -= quantity
                    print(f"Purchase successful! You bought {quantity} {product['name']}s.")
                else:
                    print("Not enough quantity in stock.")
            else:
                print("Product not found.")
        else:
            print("Customer not found.")

def main():
    shop = CosmeticsShop()

    while True:
        choice = input("\n1. Add Product\n2. Add Customer\n3. Display Products\n4. Display Customers\n5. Make Purchase\n6. Exit\nChoose an option: ")
        if choice == "1":
            shop.add_product()
        elif choice == "2":
            shop.add_customer()
        elif choice == "3":
            shop.display_products()
        elif choice == "4":
            shop.display_customers()
        elif choice == "5":
            shop.make_purchase()
        elif choice == "6":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()