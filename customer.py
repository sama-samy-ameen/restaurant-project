class MenuItems:
    def init(self, item_name, item_id, price, availability=True ):
        self.item_name=item_name
        self.item_id=item_id
        self.price=price
        self.availability=availability

class Order:
    def init(self, table_number, order_id):
        self.table_number=table_number
        self.order_id=order_id
        self.items=[]
        self.status="Pending"
        self.total_price=0

#Global shared menu for testing/demonstration.

global_menu=[
    MenuItems("Pizza", 1, 250),
    MenuItems("Pasta", 2, 210),
    MenuItems("Burger", 3, 185),
    MenuItems("Juice", 4, 40),
    MenuItems("Soda", 5, 60),
    MenuItems("Water", 6, 25)]

global_orders=[]
total_revenue=0

class Customer:
    #customer authorities:"make an order from the menu, buy it, do reviews"
    def __init__(self):
        print('         welcome to our restaurant!          \n Choose what you’d like from our menu to place your order')
        print(global_menu)

print(global_menu)