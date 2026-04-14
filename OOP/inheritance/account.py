class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited{amount}. New balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest of {interest}. New balance: {self.balance}")

class TransactionalAccount(Account):
    def __init__(self, owner, balance, transaction_fee, overdraft_limit):
        self.transaction_fee = transaction_fee
        self.overdraft_limit = overdraft_limit


    def withdraw(self, amount):
        total_amount = amount + self.transaction_fee
        if self.balance - total_amount < self.overdraft_limit:
            print("Transaction exceeds overdraft limit. Withdrawal denied.")
        elif total_amount > self.balance:
            print("Insufficient funds for this transsaction.")
        else:
            self.balance -= total_amount
            print(f"Withdrew {amount} with a fee of {self.transaction_fee}. New balance: {self.balance}")

savings = SavingsAccount("Alice", 5000, 0.05)
savings.deposit(4000)
savings.apply_interest()
balance = savings.balance

transact =  TransactionalAccount(savings.owner, 8000, 30, 200)
transact.withdraw(3000)
transact.withdraw(5000)
transact.withdraw(1160)