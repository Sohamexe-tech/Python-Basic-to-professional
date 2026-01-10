class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def increasePrice(self, amt):
        if amt > 0:
            self.price += amt
        else:
            print("Invalid amount")

    def decreasePrice(self, amt):
        if amt > 0 and amt <= self.price:
            self.price -= amt
        else:
            print("Invalid amount")

    def show(self):
        print("\nProduct ID :", self.id)
        print("Name       :", self.name)
        print("Price      :", self.price)


pid = input("Enter Product ID: ")
name = input("Enter Product Name: ")
price = float(input("Enter Price: "))

p = Product(pid, name, price)

while True:
    print("\n1. Increase Price")
    print("2. Decrease Price")
    print("3. Show Product")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        amt = float(input("Enter amount to increase: "))
        p.increasePrice(amt)

    elif ch == 2:
        amt = float(input("Enter amount to decrease: "))
        p.decreasePrice(amt)

    elif ch == 3:
        p.show()

    elif ch == 4:
        break

    else:
        print("Invalid choice")
