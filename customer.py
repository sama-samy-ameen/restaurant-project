
from MainFile import Order, global_menu, global_orders ,MenuItems
#for the show_bill function below:
from financial import FinancialManager
manager=FinancialManager() #you must leave this one
from bank import BankAccount
import random
class Customer(Order):
    def __init__(self):
        
        #displaying the menu
        print(' Welcome to our restaurant,\n','choose the items you want from our menu and place your order:')
        for i in global_menu:
            print( '    ','(',i.item_id,')',i.item_name,':',i.price,'EGP')
        self.validation=None
        self.did_c_order=None
        self.dept=None
        self.order={}
        self.existing_table=False
        super().__init__(None,random.randint(0,7000)) 
        self.order_meth()
        #table number and order id are set correctly later in the ordering process


    def order_meth(self): #order method
        
        try:
            self.did_c_order=True
            check=True
            while check:
              # a general exception handling so that the program doesn't crash
                try: #taking the the overall amount of items , then taking each one in detail
                    self.food=int(input('\nEnter the id of the item you want: '))
                    valid=True
                    while valid:
                            for i in global_menu:
                                if self.food ==i.item_id:
                                    self.food_name=i.item_name
                                    valid=False
                                    break
                                                
    
                except:
                    print('\nPlease enter a valid id')
                

        
                check=True
                while check:
                    try:
                        quant=int(input(f'\nHow much {self.food_name} do you want ? '))
                        if quant>0 and quant <10 :
                            check=False
                    except:
                        print('\nPlease enter a valid quantity')
                #adding the order to a dictionary        
                self.order[self.food_name]=int(quant)

                check=True
                while check:
                    try:
                        choice=int(input('\NWould you like anything else, or would you like to confirm your order?\n1-add to the order\n2-confirm it'))
                        if choice ==1 or choice ==2:
                            check=False
                    except:
                        print('\nPlease enter a valid input')

                    match choice :
                        case 1 :
                            check=True
                            while check:
                            # a general exception handling so that the program doesn't crash
                                try: #taking the the overall amount of items , then taking each one in detail
                                    self.food=int(input('\nEnter the id of the item you want: '))
                                    valid=True
                                    while valid:
                                        for i in global_menu:
                                            if self.food ==i.item_id:
                                                self.food_name=i.item_name
                                                valid=False
                                                break
                                                                            
                                
                                except:
                                    print('\nPlease enter a valid id')
                                            
                            
                                    
                                check=True
                                while check:
                                    try:
                                        quant=int(input(f'\nHow much {self.food_name} do you want ? '))
                                        if quant>0 and quant <10 :
                                            check=False
                                    except:
                                            print('\nPlease enter a valid quantity')
                                            #adding the order to a dictionary        
                                            self.order[self.food_name]=int(quant)
                        case 2:
                                
                            self.confirm_order()
        except:
            print('\nAn error occurred')
            self.next_step()


    def confirm_order(self):
        
        print('Items:','    ','Quantity','\n')
        for key,value in self.order.items():
            for item in global_menu:
                if key.food_name() == item.item_name:
                    print(key,'           ',value)
       # confirming the order 

        check=True
        while check:
                try:
                    confirmation=int(input('\nAre you sure you want to place this order\n1-Yes\n2-No'))
                    if confirmation ==1 or confirmation ==2:
                        check=False
                except:
                    print('\nPlease insert one of the given options')

        match confirmation :
            case 1:    
                try:  #more info of the customer order
                            if self.existing_table==False:
                                check=True
                                while check:
                                    try:
                                        self.table_number=int(input('\nEnter your table number: '))
                                        if self.table_number >0 and self.table_number<=20:
                                            check=False
                                        else:
                                            print('\nPlease enter a valid table number!')
                                    except:
                                        print('\nPlease enter a valid input')

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
                                    
                if self.existing_table:
                            print('\nItems have been added to your order successfully!')
                else:
                            print('\nYour order has been confirmed successfully!')
                self.next_step()
                
            case 2:
                print('\nLet\'s redo the order')
                self.order={}
                self.order_meth()

                
            

    def add_to_order(self):
        if self.did_c_order ==True:

            print('\n','Choose the items you want from our menu to add them to your order:')
            for i in global_menu:
                print( '    ','(',i.item_id,')',i.item_name,':',i.price,'EGP')
            self.order_meth()
        elif self.did_c_order ==None:
            print('\nYou don\'t have an order so you can add items to it')
            print('\n','Choose the items you want from our menu to create your order:')
            for i in global_menu:
                print( '    ','(',i.item_id,')',i.item_name,':',i.price,'EGP')
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
                    self.existing_table=True
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
                self.validation=None
                self.dept=None
                self.order={}
                self.existing_table=False
                self.table_number=None
                self.order_id=random.randint(1,100000)
                self.order_meth() 
        except:
            print('\nAn error occurred, please try again\n')





    
    #taking the final value of the bill from the manager class after applying discounts 'if available'
    # NOTE_THAT generate_bill function is taken from the financial manager class

    
    def show_bill(self):
        print('\n','----------Bill----------')
        print('items*quantity:','    ','price','\n')
        for key,value in self.order.items():
            for item in global_menu:
                if key.capitalize() == item.item_name:
                    print(key,'(',value,')','           ',value*item.price)
        self.total_bill=manager.generate_bill(self.new_order) 
        #storing the total value in a variable will be useful for the pay_credit method
        print('\nTotal: ',self.total_bill)
        print('--------------------------')


    def review(self):
        check=True
        if self.did_c_order==True:

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

        elif self.did_c_order==None:
            print('You can\'t make a review unless you make an order first')

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
# the add to order doesnt add to the order dictionary so the bill doesnt contain the new items
# the way the order inputs are taken is awful




