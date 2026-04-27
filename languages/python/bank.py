class InsufficentFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class AccountLockedError(Exception):
    pass

class BankAccount():
    def __init__(self):
        self.balance = 0
        self.amount = 0
        self.locked = False

    def deposit(self,amount):
        self.amount = amount
        if self.amount < 0:
            raise InvalidAmountError("not valid input")
        if self.locked == True:
            raise AccountLockedError()

        else:
            self.amount = amount
            self.balance += self.amount
            print(f"{self.amount} deposited")


    def withdraw(self,amount):
        self.amount = amount
        if self.locked == True:
            raise  AccountLockedError()


        if amount <= self.balance:
            self.balance -= self.amount

            print(f"{self.balance} left in account")
            return
        else:
            raise InsufficentFundsError("not enough money in your account")


    def get_balance(self):
        if self.locked:
            raise AccountLockedError()
        print(f"{self.balance} is in your balance")

    def lock(self):
        self.locked = True



    def unlock(self):
       self.locked = False


bank = BankAccount() 
bank.deposit(100)
bank.withdraw(50)
bank.get_balance()
