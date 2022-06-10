
class Account:
    def __init__(self,name, account_number):
        self.name=name
        self.number=account_number
        self.balance = 0
        self.deposits=[]
        self.withdrawal=[]
        

    def deposit(self,amount):
        
       

        if amount<=0:
            return f"Deposit should be more than zero"
        else:
            self.balance += amount
            self.deposits.append(amount)
            return f"You have deposited {amount} your new balance is {self.balance}" ,self.deposits
            
    def withdraw(self,amount):
        self.withdrawal -=amount
        self.deposits.append(amount)

        if amount>self.balance:
            return f"Your balance is {self.balance},you cannot withdraw the {amount}"
        elif amount <=0:
            return f"Amount {amount} must be greater than zero" 

        else:
            self.balance-=amount
            self.withdrawal.append(amount)
            return f"You have withdrawn {amount} your balance is {self.balance}" ,self.withdrawal 

    def deposit_statement(self):
        print(*self.deposits,sep="\n")    