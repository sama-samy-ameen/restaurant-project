
from MainFile import Order, global_menu, global_orders ,MenuItems
#for the show_bill function below:
from finance import FinancialManager
manager=FinancialManager() #you must leave this one
from bank import BankAccount
class Customer(Order):
    def __init__(self):
        
        #displaying the menu
        print(' Welcome to our restaurant,\n','choose the items you want from our menu and place your order:')
        for i in global_menu:
            print( '    ','(',i.item_id,')',i.item_name,':',i.price,'EGP')
        self.validation=None
        self.dept=None
        super().__init__(None,100) 
        self.order_meth()
        #table number and order id are set correctly later in the ordering process


    def order_meth(self):
        
        try:
            check=True
            while check:
              # a general exception handling so that the program doesn't crash
                try: #taking the the overall amount of items , then taking each one in detail
                    self.amount=int(input('\nHow many items do you want? '))
                    self.order={}
                    # amount condition
                    if self.amount>0 and self.amount<len(global_menu):
                        check=False
                except:
                    print('\nPlease enter a valid number of items')

            #taking the order in detail and placing it in a dictionary
            for i in range(self.amount):
                try:
                    item=input("\nWhat will you order? :")  
                    #item conditions
                    valid=True
                    while valid:
                        for i in global_menu:
                            if item.capitalize() ==i.item_name:
                                valid=False
                                break
                            
                        if valid==True:
                            print('\nThis item is currently unavailable or maybe you just wrote it incorrectly')
                            item=input("\nWhat will you order? :")          

                except:
                    print('\nInvalid input')
                
                check=True
                while check:
                    try:
                        quant=int(input(f'\nHow much {item} do you want ? '))
                        if quant>0 and quant <10 :
                            check=False
                    except:
                        print('\nPlease enter a valid quantity')
                #adding the order to a dictionary        
                self.order[item]=int(quant)
            self.confirm_order()
        except:
            print('\nAn error occurred')
            self.next_step()


    def confirm_order(self):       # confirming the order 
            confirmation=input(f'\nAre you sure you want to place this order {self.order} ? :')
            if 'yes' in confirmation.lower():
                
                try:  #more info of the customer order
                    check=True
                    while check:
                        try:
                            self.table_number=int(input('\nEnter your table number: '))
                            if self.table_number >0 and self.table_number<=20 :
                                check=False
                            else:
                                print('\nPlease enter a valid table number!')
                        except:
                            print('\nPlease enter a valid input')
                    self.order_id+=1  #so that the next order's id becomes different
                    self.new_order = Order(self.table_number, self.order_id)
                    global_orders.append(self.new_order)
                except:
                    print('\nPlease enter a valid table number')
                
                #connecting  customer's order with the global Order list, so that the manager and the chef can access them
                for key, quantity in self.order.items():
                    for i in global_menu:
                        if key.capitalize() == i.item_name:
                            for x in range(quantity):
                                self.new_order.items.append(i)
                            
                print('\nYour order has been confirmed successfully!')
                self.next_step()
                
        

            elif 'no' in confirmation.lower():
                print('\nPlease place your order again')
                self.order_meth() #retake the order
                
            else:
                print('\nUnidentified answer')
                self.confirm_order() # asking again 'confirmation'

    def add_to_order(self):
        print('\n','Choose the items you want from our menu to add them to your order:')
        for i in global_menu:
            print( '    ','(',i.item_id,')',i.item_name,':',i.price,'EGP')
        self.validation=None
        self.dept=None
        super().__init__(self.table_number,self.order_id) 
        self.order_meth()
      
    #this function shows the user a set of options to choose from and decide what to do next
    def next_step(self):
        check1=True
        while check1:
            try:
                option=int(input('\nChoose what you would like to do next\n1-it is suggested to create a bank account so you can try the pay bill feature\n2-show_bill\n3-pay_bill\n4-rate your experience\n5-Make a new order\n6-Add items to your order\n7-exit\n--> '))
                if option==1:
                    self.validation=True

                if option ==1 or option ==2 or option ==3 or option ==4 or option==5 or option==6 or option==7 :
                    check1=False
                else:
                    print('please enter one of the given options')
            except:
                print('please enter a valid input')



            match option:
                case 1:
                    account=BankAccount()
                    account.deposit()
                    self.account=account
                    self.next_step()
                case 2:
                    self.show_bill()
                    self.next_step()
                case 3: # you cant pay credit unless you have a bank account 
                    if self.validation==True :
                        self.pay_credit()
                        self.next_step()
                    elif self.validation==None:
                        print('\nSorry, you dont\'t have a bank account')
                        self.next_step()
                        
                   
                case 4:
                    self.review()
                    self.next_step()

                case 5:
                    self.Dept()
                case 6:
                    self.add_to_order()
                case 7:
                    print('Have a good day!')
                    break


    def Dept(self):
        try: 
        #the user can make a new order only if he payed for the previous order:
            if self.dept==None:
                print('sorry you can\'t make a new order unless you pay for your last order')
                self.show_bill()
                self.next_step()
            elif self.dept==True:
                print('\nChoose the items you want from our menu and place your order:')
                for i in global_menu:
                    print( '    ','(',i.item_id,')',i.item_name,':',i.price,'EGP')
                self.order_meth() 
        except:
            print('\nAn error occurred, please try again\n')





    
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
        check=True
        while check:   
            try:
                rev=int(input('On a scale of 1 to 5, how would you rate your experience at our restaurant? '))
                check = False

                if rev <0:
                    complaint=input('write your complaint: ')
                    print('\nWe\'re really sorry that you had a bad experience. We truly appreciate your feedback and will do our best to make sure it doesn\'t happen again')
                elif rev>5:
                     print('That means a lot to us! We’re delighted that you enjoyed your experience.')
                    

                match rev:

                    case 0|1|2|3 :
                        complaint=input('write your complaint: ')
                        print('\nWe\'re really sorry that you had a bad experience. We truly appreciate your feedback and will do our best to make sure it doesn\'t happen again')
                        
                    case 4 | 5:
                        print('Thank you for your positive feedback! We\'re glad you enjoyed your experience.')
                   
            except:
                print('Enter a valid input')

    #connected with the bank_account
    def pay_credit(self):
        try:    

            if self.account.balance < self.total_bill :
                print('you dont have enough money')
            else:
                self.dept=True
                self.account.withdraw()
        except:
            print('An error occurred ,please try again')
            self.next_step()

    





       

#testing
c1=Customer()





