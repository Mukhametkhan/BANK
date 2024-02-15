class Customer():
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number


class Bank():
    def __init__(self):
        self.customers = dict()
        self.accounts = dict()

    def add_customer(self, first_name, last_name, passport_number):
        customer = Customer(first_name, last_name, passport_number)
        self.customers[customer.passport_number] = customer

    def get_customer(self, passport_number):
        if passport_number not in self.customers:
            raise KeyError("Customer not found")
        return self.customers[passport_number]

    def add_account(self, account, customer):
        self.accounts[customer] = account

    def get_customer_account(self, passport_number):
        customer = self.get_customer(passport_number)
        if customer not in self.accounts:
            raise KeyError("Account not found")
        return self.accounts[customer]

    def deposit(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.deposit(amount)

    def withdraw(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.withdraw(amount)


class BankAccount():
    def __init__(self, number, currency):
        self.number = number
        self.currency = currency
        self.amount = 0

    def deposit(self, sum):
        self.amount += sum

    def withdraw(self, sum):
        self.amount -= sum
