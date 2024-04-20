# Lab13.py
# Author: Justin Hoang

# This Lab will expand upon the code for Lab12.py. If you did not complete Lab12.py, you should do so before attempting this Lab.

# Copy the code from Lab12.py into this file 1-13. I'll add some comments to help you out.


### INSERT CODE FROM LAB12.PY HERE 1-13###
from tabulate import tabulate
# Lab 12 will show basic understanding of Object Oriented Programming in Python.


# 1. Create a class called Product. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# price -> this should be a float
# product_id (this should be a unique number)
class Product:
    def __init__(self, name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id


# 2. Create a method called __str__ that returns a string with the following format:
# Product: <name>, Price: <price>, ID: <product_id>
# Hint: use f-strings to format the string.
def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, ID: {self.product_id}"
        

# Great now that we have a Product lets create a Customer class.
# 3. Create a class called Customer. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# customer_id (this should be a unique number)
# cart -> this should be a list that contains Product objects.
# also create a __str__ method that returns a string with the following format:
# Customer: <name>, ID: <customer_id>
# Hint: use f-strings to format the string.

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.cart = []

# 4. Create a method called add_to_cart that takes in a Product object and adds it to the cart list. print out the product that was added and the customer's name.

def add_to_cart(self, product):
        self.cart.append(product)
        print(f"Added {product.name} to {self.name}'s cart.")

# 5. Create a method called remove_from_cart that takes in a Product object and removes it from the cart list.

def remove_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)
            print(f"Removed {product.name} from {self.name}'s cart.")
        else:
            print(f"{product.name} is not in {self.name}'s cart.")

# 6. Create a method called checkout calculates the total price of all the products in the cart and prints out the total. After printing out the total, empty the cart.
# Hint: you will need to loop through the cart and add up the prices.

def checkout(self):
        total_price = sum(product.price for product in self.cart)
        print(f"Total price for {self.name}'s cart: ${total_price}")
        self.cart = []
# 7. Create a method called display_products that prints out all the products in the cart list.(use the __str__ method from the Product class)
def display_products(self):
        print("\nProducts in", self.name + "'s cart:")
        for product in self.cart:
            print(product)

# 8. **Extra** Create a method called display_products_pretty that prints out all the products in the cart list. (use the tabulate library)
# Make a nice table table using the tabulate library.
def display_products_pretty(self):
        table_data = [[product.name, product.price, product.product_id] for product in self.cart]
        print("\nProducts in", self.name + "'s cart:")
        print(tabulate(table_data, headers=['Name', 'Price', 'ID'], tablefmt='grid'))


# 9. Create a class called Store. The class should have the following attributes in the __init__ method:
# products -> this should be a list that contains Product objects.
# customers -> this should be a list that contains Customer objects.
class Store:
    def __init__(self):
        self.products = []
        self.customers = []
# 10. Create a method called add_product that takes in a Product object and adds it to the products list.

def add_product(self, product):
        self.products.append(product)
# 11. Create a method called add_customer that takes in a Customer object and adds it to the customers list.
def add_customer(self, customer):
        self.customers.append(customer)
# 12. Create a method called display_products that prints out all the products in the products list.
def display_products(self):
        print("\nCurrent products in the store:")
        for product in self.products:
            print(product)
# 13. Create a method called display_customers that prints out all the customers in the customers list.
def display_customers(self):
        print("\nCurrent customers in the store:")
        for customer in self.customers:
            print(customer)
# Typically we would create another file and import the classes we created. For this lab, we will just create the objects in this file to show how its possible.

# 14. Create a store object called store.
store = Store()
# 15. Create a product object called product1 with the following attributes:
# name: "iPhone 12"
# price: 799.99
# product_id: 1
product1 = Product("iPhone 12", 799.99, 1)


# 16. Create a product object called product2 with the following attributes:
# name: "iPhone 12 Pro"
# price: 999.99
# product_id: 2
product2 = Product("iPhone 12 Pro", 999.99, 2)

# 17. Create a product object called product3 with the following attributes:
# name: "iPhone 12 Pro Max"
# price: 1099.99
# product_id: 3
product3 = Product("iPhone 12 Pro Max", 1099.99, 3)

# 18. Create a customer object called customer1 with the following attributes:
# name: "John"
# customer_id: 1
customer1 = Customer("John", 1)
# 19. Create a customer object called customer2 with the following attributes:
# name: "Jane"
# customer_id: 2
customer2 = Customer("Jane", 2)

# 20. Add product1 to the store using the add_product method.
store.add_product(product1)
# 21. Add product2 to the store using the add_product method.
store.add_product(product2) 
# 22. Add product3 to the store using the add_product method.
store.add_product(product3)
# 23. Add customer1 to the store using the add_customer method.
store.add_customer(customer1)
# 24. Add customer2 to the store using the add_customer method.
store.add_customer(customer2)

# 25. Add product1 to customer1's cart using the add_to_cart method.
customer1.add_to_cart(product1)

# 26. Add product2 to customer1's cart using the add_to_cart method.
customer1.add_to_cart(product2)

# 27. Add product3 to customer2's cart using the add_to_cart method.
customer2.add_to_cart(product3)
# 28. Display current products in customer1's cart using the display_products method.
customer1.display_products()
# 29. Display current products in customer2's cart using the display_products method.
customer2.display_products()
# 30. Checkout customer1's cart using the checkout method.
customer1.checkout()
# 31. Checkout customer2's cart using the checkout method.
customer2.checkout()
# 32. Display current products in customer1's cart using the display_products method. (should be empty)
customer1.display_products()
### END CODE FROM LAB12.PY ###

# START OF Lab 13 Questions
# 1. Create a method called add_product_to_customer_cart that takes in a Customer object and a Product object. The method should add the product to the customer's cart. The method should also print out the product that was added and the customer's name.
# Hint: You can use the add_to_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.
def add_product_to_customer_cart(customer, product):
    customer.add_to_cart(product)
    print(f"Added {product.name} to {customer.name}'s cart.")


# 2. Create a method called remove_product_from_customer_cart that takes in a Customer object and a Product object. The method should remove the product from the customer's cart. The method should also print out the product that was removed and the customer's name.
# Hint: You can use the remove_from_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.
def remove_product_from_customer_cart(customer, product):
    customer.remove_from_cart(product)
    print(f"Removed {product.name} from {customer.name}'s cart.")


# 3. Create a menu function that will display the following menu:
# 1. Add Product
# 2. Add Customer
# 3. Add Product to Customer's Cart
# 4. Remove Product from Customer's Cart
# 5. Display Products
# 6. Display Customers
# 7. Display Customer's Cart
# 8. Checkout
# 9. Exit
def menu():
    print("Menu:")
    print("1. Add Product")
    print("2. Add Customer")
    print("3. Add Product to Customer's Cart")
    print("4. Remove Product from Customer's Cart")
    print("5. Display Products")
    print("6. Display Customers")
    print("7. Display Customer's Cart")
    print("8. Checkout")
    print("9. Exit")
    choice = int(input("Enter your choice: "))
    return choice

# The menu function should return the user's choice as an integer.
# Hint: Print out the menu and then use the input() function to get the user's choice.

# 4. Create a main function that will call the menu function and then call the appropriate methods based on the user's choice. The main function should be in a while loop that will continue to call the menu function until the user enters 0 to exit the program.
# IMPORTANT: The main function should create a Store object and then call the appropriate methods on the Store object. Without the Store object, you will not be able to add products or customers.
# IE main function should look something like this:
# def main():
#     store = Store()
#     while True:
#         choice = menu()
#         if choice == 1:
#             # call add_product method
#         elif choice == 2:
#             # call add_customer method
#         elif choice == 3:
#             # call add_product_to_customer_cart method
# ETC...

# Hint 1: If you need informtation from the user about a product or customer, you can ask for it in the main function and then pass it to the appropriate method. Don't be afraid to use input() in the main function.
# Hint 2: Some of the methods take in a Product object or a Customer object. You will need to create a Product object or a Customer object before calling the method. You can create a Product object or a Customer object in the main function and then pass it to the appropriate method.
# Hint 3: You can use the display_products and display_customers methods to help you out.
# Hint 4: Some Methods take in parameters. You will need to pass in the correct parameters to the method. For example, the add_product method takes in a Product object. You will need to pass in a Product object to the method. You can pass in a Product as a parameter.
# IE. store.add_product(product) where product is a Product object.
# store.add_product(Product(name, price, product_id))
# You can either ask the user for the name, price, and product_id or you can hard code it in the main function.
def main():
    store = Store()
    while True:
        choice = menu()
        if choice == 1:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            product_id = int(input("Enter product ID: "))
            product = Product(name, price, product_id)
            store.add_product(product)
        elif choice == 2:
            name = input("Enter customer name: ")
            customer_id = int(input("Enter customer ID: "))
            customer = Customer(name, customer_id)
            store.add_customer(customer)
        elif choice == 3:
            customer_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product ID: "))
            customer = next((c for c in store.customers if c.customer_id == customer_id), None)
            product = next((p for p in store.products if p.product_id == product_id), None)
            if customer and product:
                add_product_to_customer_cart(customer, product)
            else:
                print("Customer or product not found.")
        elif choice == 4:
            customer_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product ID: "))
            customer = next((c for c in store.customers if c.customer_id == customer_id), None)
            product = next((p for p in store.products if p.product_id == product_id), None)
            if customer and product:
                remove_product_from_customer_cart(customer, product)
            else:
                print("Customer or product not found.")
        elif choice == 5:
            store.display_products()
        elif choice == 6:
            store.display_customers()
        elif choice == 7:
            customer_id = int(input("Enter customer ID: "))
            customer = next((c for c in store.customers if c.customer_id == customer_id), None)
            if customer:
                customer.display_products()
            else:
                print("Customer not found.")
        elif choice == 8:
            customer_id = int(input("Enter customer ID: "))
            customer = next((c for c in store.customers if c.customer_id == customer_id), None)
            if customer:
                customer.checkout()
            else:
                print("Customer not found.")
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

 # remove this line when you start working on the main function


if __name__ == "__main__":
    """
    Leave this code at the bottom of the file. It will call the main function when you run the file.
    """

    main()
