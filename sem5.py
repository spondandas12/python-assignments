class bankaccount:
    def __init__(self, acc_number, balance= 0):
        self.acc_number = acc_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited rs{amount}")
        else:
            print("Invalid deposit amount")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"withdraw rs{amount}")
        else:
            print("Insufficient balance or invalid amount")
    def check_balance(self):
        print(f"----------------------wc---------------------" f"\nCurrent Balance: {self.balance}" f"\n--------------ty--------------")

account = bankaccount(101, 5000)
account.deposit(2000)
account.withdraw (1500)
account.check_balance()       