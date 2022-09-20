'''
Aim of this file: Demonstrate examples of encapsulation
'''

class Product:
    def __init__(self):
        self.__maxprice = 900
    
    def set_price(self, price):
        self.__maxprice = price
    
    def show_price(self):
        print(self.__maxprice)
    

class PublicProduct:
    def __init__(self, price=900):
        self.maxprice = price
    
    def show_price(self):
        print(self.maxprice)


sample_private_product = Product()
sample_private_product.show_price()

sample_private_product.__maxprice = 1000
sample_private_product.show_price()

sample_public_product = PublicProduct()
sample_public_product.show_price()

sample_public_product.maxprice = 1000
sample_public_product.show_price()
