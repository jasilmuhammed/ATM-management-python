class atm:
    bank_name="hdfc bank"

    def __init__(self,account_no,account_holder,balance=1000):
        self.account_no=account_no
        self.account_holder=account_holder
        self.balance=balance
    def balance_enquiry(self):
        print("current balance:",self.balance)
    def deposit(self,amount):
        self.balance= self.balance+amount
        print("amount deposited:",amount)
        print("current balance:",self.balance)
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance=self.balance-amount
            print("amount withdraw:",amount)
            print("current balance:",self.balance)
        else:
            print("insufficient balance")
atm1=atm(12345,"jasil")
atm1.balance_enquiry()
atm1.deposit(4000)
atm1.withdraw(10000)
