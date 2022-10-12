class Account:
    def __init__(self,title=None,Balance=0):
        self.title = title
        self.Balance = Balance
    
    def deposit(self,deposit_amount):
        self.Balance = self.Balance + deposit_amount
        return self.Balance

    def withdrawal(self,wamount):
        self.Balance = self.Balance - wamount
        return self.Balance

    def getBalance(self):
        print(self.Balance)

class SavingsAccount(Account):
    def __init__(self,title=None,Balance=0,interestRate=0):
        super().__init__(title,Balance)
        self.interestRate = interestRate

    def interestAmount(self):
        self.iamount = (self.interestRate * self.Balance)/100
        return self.iamount

title = input("Enter the title: ")
Balance = int(input("Enter the current Balance: "))
interestRate = int(input("Enter the rate of interest: "))


account_obj = Account(title,Balance)
saving_obj = SavingsAccount(title,Balance,interestRate)

choice = int(input("Enter the choice: 1. Balance enquiry 2. Deposit amount 3. Withdraw amount 4.Interset amount\n"))
if choice == 1:
    saving_obj.getBalance()
elif choice == 2:
    deposit_amount = int(input("Enter the amount to be deposited: "))
    final_amount = saving_obj.deposit(deposit_amount)
    print("Total Balance now is: ",final_amount)
elif choice == 3:
    withdrawal_amount = int(input("Enter the amount to be withdrawn: "))
    final_amount = saving_obj.withdrawal(withdrawal_amount)
    print("Total Blance after withdrawal is: ",final_amount)
elif choice == 4:
    int_amount = saving_obj.interestAmount()
    print("Interset amount of the current balance is: ",int_amount)
else:
    print("Enter valid choice")
