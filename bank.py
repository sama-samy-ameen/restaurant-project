class BankAccount:
        def __init__(self):
            try:
                print('welcome to our bank')
                self.name=input('Enter your name: ')
                self.balance=0
                self._national_id=int(input('Enter your national id: '))
                self._passw=int(input('Enter your password: '))
                confirm_pass=int(input('Confirm your password: '))
                while confirm_pass != self._passw:
                    print('it doesn\'t match your main password')
                    self._passw=int(input('Enter your password: '))
                    confirm_pass=int(input('Confirm your password: '))

                print('Account created successfully!')
            except:
                 print('an error occurred, please try again')
            
        def withdraw(self):
            checkPass=int(input('Enter your password: '))
            if checkPass==self.passw:
                withAmount=int(input('Enter the amount you want to withdraw: '))
                self.balance-=withAmount
                print('process is done successfully')
            else:
                 print('incorrect password')

        def deposit(self):
            depAmount=int(input('Enter the amount you want to deposit: '))
            self.balance +=depAmount
            print('amount added to your balance successfully')

        def forgot_pass(self):
            check_id=int(input('Enter your national id: '))
            check_name=input()
            if check_id==self._national_id  and  check_name.lower()==self.name.lower():
                 self._passw=int(input('Enter your new password: '))
                 print('password changed successfully')
            else:
                 print('id doesn\'t match with the username')
        def change_pass(self):
            checkPass=int(input('Enter your password: '))
            if checkPass==self.passw:
                self._passw=int(input('Enter your new password: '))
                print('password changed successfully')
            else:
                 print('incorrect password')
                 
            





