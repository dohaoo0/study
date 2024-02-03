class Item():
    def __init__(self, name=None, price=None, quantity=None):
        self.name = name
        self.price = price
        self.quantity = quantity

    def input_infor_item(self):
        self.name = input("Enter its name: ")
        self.price = int(input("Enter its price: "))
        self.price = self.check_type(self.price, int)
        self.quantity = int(input("Enter its quantity: "))
        self.quantity = self.check_type(self.quantity, int)
    
    @staticmethod
    def check_type(values, _type):
        if type(values) is not _type:
            values = input("Enter again: ")
        return values
    
    def show_title(self):
        print("Name \t Price \t Quantity")
        
    def show_infor(self):
        print("{} \t {} \t {}".format(self.name, self.price, self.quantity))

item1 = Item()
item1.input_infor_item()
item1.show_title()
item1.show_infor()