
from restaurant_common_data import Order,global_menu,global_orders
#for the show_bill function below:
from financial import FinancialManager
manager=FinancialManager() #you must leave this one
from bank import BankAccount,info  
import random


class Customer(Order):
    def __init__(self):
        
        #displaying the menu
        print(' Welcome to our restaurant,\n','choose the items you want from our menu and place your order:')
        for i in global_menu:
            print(f"({i.item_id:<1}){i.item_name:<10}:{i.price:>5} EGP")
        self.did_c_order=None    #checking if the customer made an order or not, because some features cannot be used unless an order is made, such as pay bill ! 
        self.dept=None  #paid the order?
        self.order={}
        self.existing_table=False  #so if the customer added an item , it doesn't ask him again for the table number
        super().__init__(None,random.randint(1,7000)) 
        self.order_method()
        #table number is set correctly later in the ordering process


    def order_method(self): 
        
        
    
            self.did_c_order=True
            check=True
            while check: #making the order with the id of the items
                try: 
                    self.food=int(input('\nEnter the id of the item you want: '))
                    if self.food >0 and self.food <= len(global_menu):
                        check1=True #connecting the item id with the item name 
                        while check1:
                            for i in global_menu:
                                if self.food ==i.item_id:
                                    if i.availability==True:
                                          check1=False
                                          check=False
                                          break
                                    else:
                                         print('This item is currently unavailable')
                                         check1=False
                                         break
                    else:
                         print('\nplease enter a valid id')
                except:
                    print('\nPlease enter a valid id')

            check=True #connecting the item id with the item name 
            while check:
                        for i in global_menu:
                            if self.food ==i.item_id:
                                self.food_name=i.item_name
                                check=False
     
            check=True
            while check:  #quantity
                    try:
                        quant=int(input(f'\nHow much {self.food_name} do you want ? '))
                        if quant>0 and quant <=20 : #cannot order more than 20 quantity from the item
                            check=False
                    except:
                        print('\nPlease enter a valid quantity')
                #adding the order to a dictionary 
            if self.food_name in self.order:
                 self.order[self.food_name]+=quant
            else:            
                self.order[self.food_name]=quant
            return self.confirm_1() #first step in confirmation process
            
        

    def confirm_1(self): #first stage of confirming order , the customer can choose whether to add items or move to the next step

        check=True
        while check:
            try:
                        choice=int(input('\nWould you like anything else, or would you like to confirm your order?\n1-add to the order\n2-confirm it\n---> '))
                        if choice ==1 or choice ==2:
                            check=False
                        else:
                             print('Enter one of the given choices')
            except:
                        print('\nChoose one of the given options')

        
        match choice :
                    
            case 1 :
                for i in global_menu:
                    print(f"({i.item_id:<1}){i.item_name:<10}:{i.price:>5} EGP")
                self.order_method()
            case 2:
                return self.confirm_order()
            case _:
                print('Please choose one of the given options')
        


    def confirm_order(self): # last stage of confirming order, the customer can choose whether to confirm it or reorder

        #displaying the items entered by the customer
        print('--------------------------')
        print(f"{'Items':<10} {'Quantity':>10}\n")
        for key,value in self.order.items():
                print(f"{key:<10} {value:>10}")
        print('--------------------------')
       # confirming the order 

        check=True
        while check:
                try:
                    confirmation=int(input('\nAre you sure you want to place this order\n1-Yes\n2-No\n---> '))
                    if confirmation ==1 or confirmation ==2:
                        check=False
                except:
                    print('\nPlease insert one of the given options')

        match confirmation :
            case 1:    
                 #more info of the customer order
                if self.existing_table==False:
                    check=True
                    while check:
                        try:
                            self.table_number=int(input('\nEnter your table number \'1-20\': '))
                            if self.table_number >0 and self.table_number<=20:
                                check=False
                            else:
                                print('\nPlease enter a valid table number!')
                        except:
                            print('\nPlease enter a valid table number')

                # connecting the new_order variable with the Order class and the global_orders list'which have all info of the order
                    self.new_order = Order(self.table_number, self.order_id)
                    global_orders.append(self.new_order)
                
                #connecting  customer's order with the global Order list, so that the manager and the chef can access them
                #this part is for appending the items *quantity times in the global list so that the generate bill function from the Financial manager can work correctly and calculate the price of the item*quantity
                for key, quantity in self.order.items(): 
                #order is the dictionary with the ordered items from the customer
                    for i in global_menu:
                        if key == i.item_name:
                            for x in range(quantity):
                                self.new_order.items.append(i)
                    
                                    
                if self.existing_table: #if existing table is not non that means that the user is adding items to their order
                            print('\nItems have been added to your order successfully!')
                else:
                            print('\nYour order has been confirmed successfully!')
            
                            
                manager.generate_bill(self.new_order)
                self.next_step()     
                
                
            case 2:
                print('\nLet\'s redo the order')
                for i in global_menu:
                     print(f"({i.item_id:<1}){i.item_name:<10}:{i.price:>5} EGP")
                self.order={} #so that it doesn't add the items with the old wrong order
                return self.order_method()

                
            

    def add_to_order(self):   #used to add items to the customer order

        if self.did_c_order ==True:
            if self.dept==None: #customer didn't pay , so items will be added to the previous order

                    print('\n','Choose the items you want from our menu to add them to your order:')
                    for i in global_menu:
                        print(f"({i.item_id:<1}){i.item_name:<10}:{i.price:>5} EGP")
                    #adding to the existing order
                    check=True
                    while check: #making the order with the id of the items
                        try: 
                            self.food=int(input('\nEnter the id of the item you want: '))
                            if self.food >0 and self.food <= len(global_menu):
                                check1=True #connecting the item id with the item name 
                                while check1:
                                    for i in global_menu:
                                        if self.food ==i.item_id:
                                            if i.availability==True:
                                                check1=False
                                                check=False
                                                break
                                            else:
                                                print('This item is currently unavailable')
                                                check1=False
                                                break
                            else:
                               print('\nplease enter a valid id')
                        except:
                            print('\nPlease enter a valid id')
                    
                    check=True #connecting the item id with the item name 
                    while check:
                        for i in global_menu:
                            if self.food ==i.item_id:
                                self.food_name=i.item_name
                                check=False
                         
                    check=True
                    while check:  #quantity
                        try:
                            quant=int(input(f'\nHow much {self.food_name} do you want ? '))
                            if quant>0 and quant <=20 : #cannot order more than 20 quantity from the item
                                check=False
                        except:
                            print('\nPlease enter a valid quantity')
                                    #adding the order to a dictionary        
                    
               
             
                    if self.food_name in self.order: 
                        self.order[self.food_name]+=quant
                                
                    else:
                         self.order[self.food_name]=quant
                                
                                
                    return self.confirm_1()
                            
                
 


            elif self.dept==True:  #customer already paid, so create a new order
                print('\nChoose the items you want from our menu and place your order:')
                for i in global_menu:
                    print(f"({i.item_id:<1}){i.item_name:<10}:{i.price:>5} EGP")
                self.dept=None
                self.order={}
                self.existing_table=False
                self.table_number=None
                self.order_id=random.randint(1,100000)
                self.order_method() 
                 
        elif self.did_c_order ==None: 
            print('\nYou don\'t have an order so you can add items to it')
            print('\n','Choose the items you want from our menu to create your order:')
            for i in global_menu:
                 print(f"({i.item_id:<1}){i.item_name:<10}:{i.price:>5} EGP")
            self.order_method()
      
    #this function shows the user a set of options to choose from and decide what to do next
    def next_step(self):
        check=True
        while check:
            try:
                option=int(input('\nChoose what you would like to do next\n1-show_bill\n2-pay_bill\n3-rate your experience\n4-Add items to your order\n5-exit\n--> '))
                
                if option>=1 and option<=5:
                    check=False
                else:
                    print('please enter one of the given options')
            except:
                print('please enter a valid input')



        match option:  #return is to handle the recursive function calling
                case 1:
                    self.show_bill()
                    return self.next_step()
                case 2:
                    
                        self.show_bill()
                        self.pay()
                        return self.next_step()
                case 3:
                    self.review()
                    return self.next_step()

                case 4:
                    self.existing_table=True
                    return self.add_to_order()
                case 5: 
                        if self.dept==True:
                            print('Have a good day!')
                            return
                        elif self.dept==None:
                             print('You didn\'t pay for the order')
                             self.pay()
                             return self.next_step()
                


   
    
    #taking the final value of the bill from the manager class after applying discounts 'if available'
    # NOTE_THAT generate_bill function is taken from the financial manager class

    
    def show_bill(self):
        if self.dept==None: #customer didn't pay
            print('\n','-----------------Bill-----------------') 
            print(f'your order id: {self.order_id}')
            print(f"{'items*quantity':<10}{'price':>20}\n") 
            for key,value in self.order.items(): 
                for item in global_menu: 
                    if key.lower() == item.item_name.lower(): 
                        print(f"{key:<10}({value:<2}){value*item.price:>20}")
                        break
            self.total_bill=manager.generate_bill(self.new_order) 
            #storing the total value in a variable will be useful for the pay method
            print('\nTotal: ',self.total_bill)
            print('---------------------------------------')
        elif self.dept==True: #they paid
             print('You already paid for your order')



    def review(self): # the customer cant choose to make a review unless he had already placed an order
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
    def pay(self): # paying_credit method becomes optional 
        if self.dept==True : #customer paid for the order
            print('You already paid for your order')
        elif self.dept==None: #customer didn't pay
            check=True
            while check:
                try:
                    choose=int(input('How would you like to pay\n1-credit\n2-cash\n---> '))
                    if choose==1 or choose==2:
                        check=False
                    else:
                         print('\nChoose one of the given options')
                except:
                    print('\nChoose one of the options')
            try:  
                match choose:
                    case 1:
                        account=BankAccount() 
                        self.account=account
                        if self.account.loginFrom_card():  #if the login occurred successfully it will return True
                            if self.account.pay_credit(self.total_bill):
                                  #if the pay_credit function occurred successfully it will return True
                                  self.dept=True 
                            else:
                                 print('Process failed')
                        else:
                             print('Login failed')
                            
                    
                    
                    case 2:
                        print('Payment received, thank you ')
                        self.dept=True
                    
            except Exception as e:
                print(e)
             





