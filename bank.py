
class Account:
    def __init__(self,name,number,balance,bankname) :
        self.name=name
        self.number=number
        self.balance=balance
        self.bankname=bankname


    def deposit(self,amount):
        self.deposit=(input("You have deposited"))
        self.balance+=amount
        return f"Hello your current balance is {self.balance} "

    def  withdraw(self,amount) :
        self.deposit=(input("You have withdrawn"))
        self.balance-=amount 
        return f"Hello your current balance is {self.balance}"