class Account:
    def __init__(self,number,pin,name):
        self.number = number
        self.__pin = pin
        self.name = name
        self._balance = 0
        self.transactions = []
        self.overdraft_limit = 0
        self._frozen = True
        self._minimum_balance = 0
    
    def check_balance(self,pin):
        if pin == self.__pin:
            return self._balance
        else:
            return "Wrong pin"
        
    def deposit(self,amount,pin):
        if pin == self.__pin:
           self._balance += amount
           self.transactions.append(f"Deposit: {amount}")
           print(f"You have successfully deposited {amount}")
        else:
           return "The pin you have entered is incorrect. Enter your pin again"
    
    

    def withdraw(self,amount,pin):
        if pin != self.__pin:
            print("Invalid pin")
        if amount > self._balance:
            print("insufficient funds")
            self._balance -= amount
        else:
            print(f"You have withdrawn {amount} and your balance is {self._balance}")        
        
    def view_details(self,pin):
        if pin == self.__pin:
           print(f"Account number: {self.number}")
           print(f"Current balance: {self._balance}")
        else:
            print("The pin you have entered is incorrect. Enter your pin")
    
    def change_owner_details(self,pin,new_name, new_pin,new_number):
        if pin == self.__pin:
           self.name = new_name
           self.__pin = new_pin
           self.number = new_number
        print(f"Account name updated to: {self.name}, your new pin is {self.__pin} and the new account number is {self.number}")

    def generate_statements(self,pin):
        if pin == self.__pin:
           return "\n".join(self.transactions)
            
    def set_overdraft_limit(self, pin,new_limit):
        if pin == self.__pin:
            self.overdraft_limit = new_limit
            print(f"Overdraft limit is: {self.overdraft_limit}")
        else:
            print("You have entered a wrong pin")        

    def calculate_interest(self, pin,rate):
        if pin == self.__pin:
           interest = self._balance * rate/100
           self._balance+=interest
           print(f"Interest is {interest}")
           self.transactions.append(f"Interest: {interest}")
        else:
           print("You have entered a wrong pin")
        
    def freeze_account(self,pin):
        if pin == self.__pin:
           self._frozen = True
        else:
            print("You have entered the wrong pin")

    def unfreeze_account(self,pin):
        if pin == self.__pin:
            self._frozen = False
        else:
            print("You have entered the wrong pin")
    
    def set_minimum_balance(self,minimum_balance):
            self._minimum_balance = minimum_balance
            return self._minimum_balance

    def transfer_funds(self,pin,amount,recipient_account):
        if pin == self.__pin:
            if self._balance - amount >= self.overdraft_limit:
                self._balance -= amount
                recipient_account._balance += amount
                self.transactions.append(f"Transfer to {recipient_account}: {amount}")
                recipient_account.append(f"Transfer from {self.number}: {amount}")
            else:
                return "Insufficient funds"
        else:
            return "Wrong pin"
        
    def close_account(self,pin):
        if pin == self.__pin:
            if self._balance == 0:
                print("Account has been closed successfully")
            else:
                print("Confirm if you want to close your account")
        else:
            print("Wrong pin")

                       


    


    
