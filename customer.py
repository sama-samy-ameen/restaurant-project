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
# import MainFile.py
class customer(Order):
    def __init__(self):
        #choosing items and placing orders
        print(' welcome to our restaurant,\n','choose the items you want from our menu:')
        for i in global_menu:
            print( '    ','(',i.item_id,')',i.item_name,':',i.price,'EGP')
        super().__init__()
    def Order(self):
        try:

            try: 
                self.amount=int(input('How many items do you want? '))
                self.order={}
                if self.amount<=0 or self.amount>len(global_menu):
                    print('out of range, try again')
            except:
                print('please enter a valid number of items')
            for i in range(self.amount):
                item=input("what will you order?  ")
                #for i in global_menu:
                 #   if item.lower() not in self.item_name.lower():
                  #      print('please enter a valid option')
                   #     break

                   # self.amount=int(input('How many items do you want? '))
                    #for i in range(self.amount):
                     #   item=input('what will you order? ')
                      #  try:
                       #     quant=int(input(f'How much {item} do you want ? '))
                        #except:
                         #   print('please enter a valid input')
                try:
                    quant=int(input(f'How much {item} do you want ? '))
                except:
                    print('please enter a valid quantity')
                self.order[item]=int(quant)
            confirmation=input(f'Are you sure you want to place this order {self.order} ? :')
            if 'yes' in confirmation.lower():
                for key in self.order:
                    self.items.append(key)
                try:
                    self.table_number=int(input('Enter your table number: '))
                    self.order_id+=1
                except:
                    print('please enter a valid table number')
                    #break

                for key,value in self.order.items():
                        for item in global_menu:
                             if key.capitalize()==item.item_name:
                                self.total_price += (item.price *value)
                print('your order has been confirmed successfully!')


            elif 'no' in confirmation.lower():
                print('please place the order again')
        
        except:
            print('sorry, an error occurred , please resubmit your order ')
    
        



        

      #errors:  the total price part   , error handling 
        





        
    #def Budget(self):
        pass 
    #def order_status(self):
        pass
    #def add item(self)
    #def history(self):
        pass
    #def review(self):
       # pass #if low send to the manager
c1=customer()
c1.Order()
