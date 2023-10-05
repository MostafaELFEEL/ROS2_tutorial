"""

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases=0
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, product):
        self.cart.remove(product)

    def calculate_cart_total(self):
        total = 0
        for product in self.cart:
            total += product.price
        if len(self.cart)>=5:
            return total*0.9
        else:
            return total
    



class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == "__main__":

        # Specify the file name (you can change this to your desired file name)
    file_name = "data_base.txt"

    # Specify the file path (optional, if you want to save it to a specific location)


    customer = Customer("Ahmed", "ahmedemad242@gmail.com")
    product1 = Product("Keyboard", 100)
    product2 = Product("Mouse", 50)
    customer.add_product(product1)
    customer.add_product(product2)
    customer.add_product(product1)
    customer.add_product(product2)
    #customer.add_product(product1)
    #customer.add_product(product2)



    print(customer.calculate_cart_total())

"""



class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []
        self.purchase_count = 0  # New attribute for tracking purchase count

    def name_val(self):
        if len(self.name) >= 2:
            return True
        else:
            return False
        

    def email_val(self):
        self.email = self.email.split("@")
        self.flag1=0
        self.flag2=0
        if self.email[1] == "gmail.com":
            self.flag1=1
        if self.email[0].isalnum():
            self.flag2=1

        if self.flag1==1 and self.flag2==1:
            return True
        else:
            return False
        
            
        


    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, product):
        self.cart.remove(product)

    def calculate_cart_total(self):
        cart_size_discount = 0
        loyalty_discount = 0
        
        if len(self.cart) > 5:
            cart_size_discount = 0.1  # 10% discount for cart size > 5
        
        if self.purchase_count > 10:
            loyalty_discount = 0.05  # 5% loyalty discount
        
        total = 0
        for product in self.cart:
            total += product.price
        
        # Calculate total discount, considering both cart size and loyalty discounts
        total_discount = cart_size_discount + loyalty_discount
        
        return total - (total * total_discount)

    def make_purchase(self):
        self.purchase_count += 1  # Increment purchase count on each purchase
        self.cart.clear()

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

if __name__ == "__main__":
    customer = Customer("Ahmed", "ahmedemad242@gmail.com")
    product1 = Product("Keyboard", 100)
    product2 = Product("Mouse", 50)
    customer.add_product(product1)
    customer.add_product(product2)
    
    # Simulate multiple purchases to qualify for the loyalty discount
    for _ in range(11):
        customer.make_purchase()

    customer.add_product(product1)
    customer.add_product(product2)

    print(customer.calculate_cart_total())
