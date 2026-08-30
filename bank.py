
import json
import random

with open("info.json", "r") as file:
    info = json.load(file)

class BankAccount:
    def __init__(self):
        self.check_natid = None  #natid=national_id
        self.national_id = None
        
       #  check=True
        # while check:
         #     try:
          #      if x>0 and x<=2:
           #         check=False
            #  except:
              #     print('Enter a valid input')
        
       #  match x:
        #      case 1:
                          
         #       self.new_account()
          #    case 2:
           #     self.access_account()

    def _save_info(self):
        with open("info.json", "w") as file:
            json.dump(info, file, indent=4)

    def loginFrom_card(self):
        while True:
                try:
                    self.check_natid = input('Enter your national id:').strip()
                    if self.check_natid.isdigit() and len(self.check_natid) == 14:
                             break
                except :
                         print('Enter a valid input')
         
        while True:
                     try:
                         check_pass = int(input('\nEnter your password:'))
                         break
                     except :
                         print('Enter a valid input')
         
        if self.check_natid in info:
                     if info[self.check_natid]["password"] == check_pass:
                         self.national_id = self.check_natid
                         print(f"\nWelcome {info[self.check_natid]['name']}!")
                         return True
                     else:
                        print('national id and password don\'t match')
                        return False
        else:
                    print('User not found')
                    return False
                         
         

    def access_account(self):
        while True:
            try:
                self.check_natid = input('Enter your national id:').strip()
                if self.check_natid.isdigit() and len(self.check_natid) == 14:
                    break
                print('Enter a valid input')
            except :
                print('Enter a valid input')

        while True:
            try:
                check_pass = int(input('\nEnter your password:'))
                break
            except :
                print('Enter a valid input')

        if self.check_natid in info:
            if info[self.check_natid]["password"] == check_pass:
                self.national_id = self.check_natid
                print(f"\nWelcome {info[self.check_natid]['name']}!")
                while True:
                    try:
                        select = int(input(f"\n welcome {info[self.check_natid]['name']} , choose what you would like to do:\n1.withdraw\n2.deposit\n3.check your balance\n4.change password\n5.forget password\n6.create credit card\n--->  "))
                        if 1 <= select <= 5:
                            break
                        else:
                            print('Choose one of the given options')
                    except :
                        print('Choose one of the given options')

                match select:
                    case 1:
                          self.withdraw()
                    case 2:
                          self.deposit()
                    case 3:
                          print(info[self.check_natid]['balance'])
                    case 4:
                          self.change_pass()
                    case 5:
                          self.forgot_pass()
                    case 6:
                          self.create_card()
            else:
                 print('national id and password don\'t match')
        else:
             print('User not found')
                

    def create_card(self):
        user_id = self.national_id 
        if user_id is None:
            print('Please log in before creating a card.')
            return

        elif info[user_id]['credit_card']!= None:
            print(f'You already have a credit card: {info[user_id]["credit_card"]}')
            return

        
        else:
            self.card = random.randint(1000, 9000)
            info[self.check_natid]['credit_card'] = self.card
            self._save_info()
            print(f'Credit card created successfully. Your card number is: {self.card}')






    def new_account(self):
        try:    
                self.card=None
                print('Bank System:')
                self.name=input('Enter your name: ')
                self.name.lower()
                #user name validation:
                while not self.name.isalpha() :
                    print('\nPlease enter your name correctly')
                    self.name=input('Enter your name: ')
                    self.name.lower()
                self.balance=0

                check=True
                while check:
                    try:
                        print('\nYour national_id must be 14 digits')
                        self.national_id=(input('\nEnter your national id'))
                        if len(self.national_id) == 14 and self.national_id.isdigit() and int(self.national_id) >0:
                            check=False
                        else:
                            print("Invalid National ID")
                        
                    except:
                            print('\nEnter a valid number!')
                 
                check=True
                    
                while check:
                        try:
                            self._passw=int(input('\nEnter your password  \'it must be numbers\': '))
                            check=False
                        except:
                            print('\nEnter a valid password')
                check=True
                while check:
                    try:
                        confirm_pass=int(input('\nConfirm your password: '))
                        check=False
                    except:
                        print('\nEnter a valid input')

                while confirm_pass != self._passw:
                        print('it doesn\'t match your main password')
                        self._passw=int(input('\nEnter your password: '))
                        confirm_pass=int(input('\nConfirm your password: '))

                self.check_natid = self.national_id
                info[self.check_natid]={'name':self.name, 'password':self._passw ,'balance':self.balance,'credit_card':self.card}
                print('\nAccount created successfully!')
                self._save_info()
        except:
                print('\nAn error occurred, please try again')

    
            
    def withdraw(self):
        check=True
        while check:
            try:
                checkPass=int(input('\nEnter your password: '))
                check=False
            except:
                print('\nEnter a valid number!')
        if checkPass==info[self.check_natid]['password']:
            c=True
            while c:
                try:
                    self.withAmount=int(input('\nEnter the amount you want to withdraw: '))
                    if self.withAmount > 0:
                         c=False
                    elif self.withAmount==0:
                         print('\nIt is impossible to withdraw no value!')
                    else:
                         print('\nCan\'t withdraw a negative value')
                except:
                     print('\nPlease enter a valid number!!!')
            if info[self.check_natid]['balance']>=self.withAmount:
                info[self.check_natid]['balance']-=self.withAmount
                self._save_info()

                print('\nProcess is done successfully')
            else:
                 print('\nInsufficient money in your balance')

        else:
            print('\nIncorrect password')

    def deposit(self):
            check=True
            while check:
                try:
                    self.depAmount=int(input('\nEnter the amount you want to deposit: '))
                    if self.depAmount > 0:
                        check=False
                    elif self.depAmount==0:
                         print('\nYou cannot deposit 0 amount!')
                    else:
                         print('\nYou cannot deposit a negative amount!')
                except:
                    print('\nEnter a valid number!')
            
            info[self.check_natid]['balance'] +=self.depAmount
            self._save_info()
            print('\nAmount added to your balance successfully')

    def forgot_pass(self):
        check=True
        while check:
            try:
                check_id=int(input('\nEnter your national id: '))
                check_id.strip()
                if len(check_id) == 14 and check_id.isdigit() and int(check_id) >0:
                     check=False
            except:
                 print('\nEnter a valid input!!!')


        check=True
        while check:
            try:
                check_name=input('\nEnter your name: ')
                check=False
                    
            except:
                print('\nEnter a valid name')

        #id and name condition:
        if check_id==info[self.check_natid]  and  check_name.lower()==info[self.check_natid]['name']:
            info[self.check_natid]['password']=int(input('\nEnter your new password: '))
            self._save_info()
            print('\nPassword changed successfully')
        else:
            print('\nID doesn\'t match with the username')

    def change_pass(self):
            check=True
            while check:
                try:
                    checkPass=int(input('\nEnter your password: '))
                    check=False
                except:
                     print('\nEnter a valid number')

            if checkPass== info[self.check_natid]['password']:
                info[self.check_natid]['password']=int(input('\nEnter your new password: '))
                self._save_info()
                print('\nPassword changed successfully')
            else:
                 print('\nIncorrect password')

    def pay_credit(self,amount):

        if info[self.check_natid]['credit_card']== None:
             print('This account user does not have a credit card!')
             return

        check=True
        while check:
            try:
                        check_card=int(input('Enter your card number: '))
                        if check_card >=1000 and check_card<=9000:
                            check=False
            except:
                        print('Enter a valid number')
                    
                     
        if  check_card==info[self.check_natid]['credit_card']:
                            if amount <= info[self.check_natid]['balance']:
                                info[self.check_natid]['balance']-=amount
                                self._save_info()
                                print('Process is done successfully')
                                return True
                            else:
                                print('insufficient balance')
                                return False
        else:
                            print('incorrect card number')
                            return False



if __name__ == "__main__":
    acc = BankAccount()
    acc.access_account()
    acc.deposit()
    acc.create_card()
    acc.pay_credit(50)

         

