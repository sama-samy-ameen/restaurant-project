#Standard shared classes.
class MenuItems:
    def __init__(self, item_name, item_id, price, availability=True ):
        self.item_name=item_name
        self.item_id=item_id
        self.price=price
        self.availability=availability

class Order:
    def __init__(self, table_number, order_id):
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

#---Test---
if __name__=="__main__":
    item1=global_menu[0]
    print(f"Item created: {item1.item_name}, Price: {item1.price} EGP")
    test_order=Order(5, 102)
    print(f"Order status: {test_order.status} for Table number: {test_order.table_number}")