from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def __init__(self,balance = 0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited{amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

savings = SavingsAccount()
savings.deposit(1000)
savings.withdraw(200)
savings.withdraw(900)      #This will show insufficient funds because the balance is only 800 after the first withdrawal.  