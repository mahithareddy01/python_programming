class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
    def deposit(self,amount):   
        self.__balance+=amount
        return self.__balance
    def withdraw(self,amount):
        self.__balance-=amount
        return self.__balance
    def get_balance(self):
        print(f"Current balance is: {self.__balance}")
ba=BankAccount()
dep=int(input("Enter an amount to deposit: "))
wtdrw=int(input("Enter an amount to withdraw: "))
ba.deposit(dep)
ba.withdraw(wtdrw)
ba.get_balance()