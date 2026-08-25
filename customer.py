#for the pay_pill fucntion below:
from bank import BankAccount
account=BankAccount()
account.deposit()
#from MainFile import Order, global_menu, global_orders
#for the show_bill function below:
from financial import FinancialManager
manager=FinancialManager()


class customer(Order):
    def __init__(self):
        #displaying the menu
        print(' welcome to our restaurant,\n','choose the items you want from our menu:')
        for i in global_menu:
            print( '    ','(',i.item_id,')',i.item_name,':',i.price,'EGP')
        super().__init__(None,100)   
        #table number and order id are set correctly later in the ordering process


    def order(self):
        try:  # a general exception handling so that the program doesn't crash
            try: #taking the the overall amount of items , then taking each one in detail
                self.account=account
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
                    #connecting the customer's order with the Order class
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
            else:
                print('unidentified answer, resubmit your order')
        
        except:
            print('sorry, an error occurred , please resubmit your order ')



    
    #taking the final value of the bill from the manager class after applying discounts 'if available'
    # NOTE_THAT generate_bill function is taken from the financial manager class

    
    def show_bill(self):
        print('\n','        Bill    ','\n')
        print('items*quantity:','    ','price')
        for key,value in self.order.items():
            for item in global_menu:
                if key.capitalize() == item.item_name:
                    print(key,'(',value,')','           ',value*item.price)
        self.total_bill=manager.generate_bill(self.new_order) 
        #storing the total value in a variable will be useful for the pay_credit method
        print('\nTotal: ',self.total_bill)


    def review(self):
        rev=int(input('On a scale of 1 to 5, how would you rate your experience at our restaurant? '))
        match rev:
            case 1 |2|3 :
                complaint=input('write your complaint: ')
            case 4 | 5:
                print('Thank you for your positive feedback! We’re glad you enjoyed your experience.')
            case _:
                print('out of range :)')

    #connected with the bank_account
    def pay_credit(self):
        if account.balance < self.total_bill :
            print('you dont have enough money')
        else:
            account.withdraw()

    





       

#testing
c1=customer()
c1.order()
c1.show_bill()
c1.review()
c1.pay_credit()

