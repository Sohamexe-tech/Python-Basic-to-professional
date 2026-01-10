# wap to know the price of the product

class product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price

    def show(self):
        print("self = ",self)
        print("id= ",self.id)
        print("name= ",self.name)
        print("price=",self.price)

p=product (10,"Pepsi",20)
print("p= ",p)
p.show()

b=product (10,"biscuit",60)
print("b= ",b)
p.show()