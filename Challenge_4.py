

class Account:
    def __init__(self,title=None,Balance=0):
        self.title = title
        self.Balance = Balance
    
    def displaytitle(self,title):
        print(self.title)

    def displayBalance(self,Balance):
        print(self.Balance)

class SavingsAccount(Account):
    def __init__(self,title=None,Balance=0,interestRate=0):
        super().__init__(title,Balance)
        self.interestRate = interestRate

    def displaysavings(self,interestRate):
        print(self.interestRate)

#initialized title and balance to None and 0sam

account_obj = Account(None,0)
account_obj.displaytitle(None)
account_obj.displayBalance(0)

#taking input from user
title = input("Enter the title: ")
Balance = int(input("Enter the balance: "))
interestRate = int(input("Enter the rate of interest: "))

#using constructor of Account class
#account_obj = Account(title,Balance)
#account_obj.displaytitle(title)
#account_obj.displayBalance(Balance)

#using constructor SavingsAccount class
savings_obj = SavingsAccount(title,Balance,interestRate)
savings_obj.displaytitle(title)
savings_obj.displayBalance(Balance)
savings_obj.displaysavings(interestRate)
