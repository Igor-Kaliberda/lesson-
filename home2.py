class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, description={self.description}, dimensions={self.dimensions})"



class Customer:
    def __init__(self, last_name, first_name, middle_name, phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone = phone

    def __str__(self):
        return f"Customer(last_name={self.last_name}, first_name={self.first_name}, middle_name={self.middle_name}, phone={self.phone})"



class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def total_cost(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def __str__(self):
        items_str = "\n".join([f"{product} x {quantity}" for product, quantity in self.items])
        return f"Order for {self.customer}:\n{items_str}\nTotal cost: {self.total_cost()}"

product1 = Product("Apple", 1, "Fresh red apple", "10x10x10 cm")
product2 = Product("Banana", 0.5, "Ripe yellow banana", "15x3x3 cm")
customer1 = Customer("Shevchenko", "Taras", "Hryhorovych", "+380501234567")


order1 = Order(customer1)
order1.add_product(product1, 5)
order1.add_product(product2, 10)

print(order1)