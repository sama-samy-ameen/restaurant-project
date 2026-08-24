
#import MainFile.py
#from financial.py import generate_bill()
#making table_number=None and order_id=100
class MenuItems:
    def __init__(self, item_name, item_id, price, availability=True ):
        self.item_name=item_name
        self.item_id=item_id
        self.price=price
        self.availability=availability
        

class Order:
    def __init__(self, table_number=None, order_id=100):
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

class customer(Order):
    def __init__(self):
        #displaying the menu
        print(' welcome to our restaurant,\n','choose the items you want from our menu:')
        for i in global_menu:
            print( '    ','(',i.item_id,')',i.item_name,':',i.price,'EGP')
        super().__init__()


    def order(self):
        try:  # a general exception handling so that the program doesn't crash
            try: #taking the the overall amount of items , then taking each one in detail

                self.amount=int(input('How many items do you want? '))
                self.order={}
                # amount condition
                while self.amount<=0 or self.amount>len(global_menu):
                    self.amount=int(input('How many items do you want? '))
                    
            except:
                print('please enter a valid number of items')
            #taking the order in detail and placing it in a dictionary
            for i in range(self.amount):
                try:
                    item=input("what will you order? :")  
                    #item conditions
                    valid=False
                    while not valid:
                        for i in global_menu:
                            if item.capitalize()==i.item_name:
                                valid=True
                                break
                            
                        if valid==False:
                            print('this item is currently unavailable or maybe you just wrote it incorrectly')
                            item=input("what will you order? :") 
                            

                    

                except:
                    print('invalid input')
                    break
                
                try:
                    quant=int(input(f'How much {item} do you want ? '))
                except:
                    print('please enter a valid quantity')
                self.order[item]=int(quant)

            # confirming the order 
            confirmation=input(f'Are you sure you want to place this order {self.order} ? :')
            if 'yes' in confirmation.lower():
                
                try:  #more info of the customer order
                    self.table_number=int(input('Enter your table number: '))
                    self.order_id+=1  #so that the next order's id becomes different
                    self.new_order = Order(self.table_number, self.order_id)
                    global_orders.append(self.new_order)
                except:
                    print('please enter a valid table number')
                
                #connecting  customer's order with the global Order list, so that the manager and the chef can access them
                for key, quantity in self.order.items():
                    for i in global_menu:
                        if key.capitalize() == i.item_name:
                            for x in range(quantity):
                                self.new_order.items.append(i)
                            
                print('your order has been confirmed successfully!')



            elif 'no' in confirmation.lower():
                print('please place your order again')
        
        except:
            print('sorry, an error occurred , please resubmit your order ')



    def generate_bill(self, order, discount=0):
        """
        Calculate bill after discount.
        """

        subtotal = 0

        # Calculate the order subtotal.
        for item in order.items:
            subtotal += item.price

        # Validate the discount.
        if discount < 0:
            discount = 0

        if discount > subtotal:
            discount = subtotal

        order.total_price = subtotal - discount

        return order.total_price
    

    #taking the final value of the bill from the manager class after applying discounts 'if available'
    def show_bill(self):
        print('\n','        Bill    ','\n')
        print('items*quantity:','    ','price')
        for key,value in self.order.items():
            for item in global_menu:
                if key.capitalize() == item.item_name:
                    print(key,'(',value,')','           ',value*item.price)
        print('\nTotal: ',self.generate_bill(self.new_order))


    

    
    
    
    
    #def order_status(self):
        #pass
    #def add item(self)
    #def history(self):
        #pass
    #def review(self):
       # pass #if low send to the manager
c1=customer()
c1.order()
c1.show_bill()
