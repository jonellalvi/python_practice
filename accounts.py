class Customer():
    def __init__(self, ssn):
        self.ssn = ssn

class Transaction():
    def __init__(self, amount, payee, memo):
        self.amount = amount
        self.payee = payee
        self.memo = memo
    def display(self):
        print("\t", self.amount, self.payee, self.memo)

class Account():
    type_display_name = "ACCOUNT"
    def __init__(self, name, balance, customer):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        self.customer = customer

    def add_transaction(self, transaction):
        self.transaction_list.append(transaction)
        self.balance += transaction.amount

    def printLedger(self):
        print(self.type_display_name)
        print(self.name)
        for individual_transaction in self.transaction_list:
            individual_transaction.display()
        print(self.balance)

kevin = Customer("544332211")
print(kevin.ssn)
# print(kevin["ssn"])


account = Account("checking", 5000, kevin)
t1 = Transaction(3000, "Landlord", "December Rent")
account.add_transaction(t1)
t2 = Transaction(3, "Starbucks", "Coffee")
account.add_transaction(t2)
t3 = Transaction(1000, "Transfer", "From Savings")
account.add_transaction(t3)

account.printLedger()
savings_account = Account("savings", 9999, kevin)
savings_account.add_transaction(Transaction(-1000, "Transfer", "To Checking"))
savings_account.printLedger()
