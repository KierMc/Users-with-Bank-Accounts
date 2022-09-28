
class BankAccount:
    
    accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print(" Insufficient funds: Charging a $5 Fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print("Balance: "+ str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= 1 + self.int_rate
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking_account = BankAccount(int_rate=0.02, balance=200)
        self.savings_account = BankAccount(int_rate=0.02, balance=100)
    
    def make_deposit(self, amount, account):
        if account=="checking":
            self.checking_account.deposit(amount)
        elif account=="savings":
            self.savings_account.deposit(amount)
        else:
            print("check spelling!")
    
    def make_withdrawal(self, amount, account):
        if account=="checking":
            self.checking_account.withdraw(amount)
        elif account=="savings":
            self.savings_account.withdraw(amount)
        else:
            print("check spelling!")

    def display_info(self):
        self.savings_account.display_account_info()
        self.checking_account.display_account_info()
    
    def yield_int(self):
        self.savings_account.yield_interest()
    
    def transfer_money(self, amount, other_user):
        self.checking_account.withdraw(amount)
        other_user.checking_account.deposit(amount)






user1 = User("Kiernan","Kier@gmail.com")
user2 = User("Thomas","Tomtom@yahoo.com")

user1.display_info()

# user1.transfer_money(50, user2)
# user1.display_info()
# user2.display_info()