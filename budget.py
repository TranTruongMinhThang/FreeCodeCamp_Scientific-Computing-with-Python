class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount: float, description=None):
        amount = amount
        if description is None:
            description = ''
        else:
            description = description
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description=None):
        if self.check_funds(amount):
            if description is None:
                description = ''
            else:
                description = description
            self.ledger.append({"amount": - amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        currentBalance = 0.0
        for i in self.ledger:
            currentBalance += i["amount"]
        return currentBalance

    def transfer(self, amount: float, category):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Received from ' + self.name)
            return True
        else:
            return False

    def check_funds(self, amount: float):
        if self.get_balance() - amount < 0:
            return False
        else:
            return True

    def __str__(self):
        titleLine = '*' * (round((30 - len(self.name)) / 2)) + self.name + '*' * (
                    30 - len(self.name) - (round((30 - len(self.name)) / 2))) + '\n'

        bodyLine = ''
        for i in self.ledger:
            bodyLine += i["description"][0:23] + ' ' * \
                        (30 - len(i["description"][0:23]) - len(str(f"{i['amount']:.02f}")[0:7])) + \
                        str(f"{i['amount']:.02f}")[0:7] + '\n'

        totalLine = 'Total: ' + str(self.get_balance())

        return titleLine + bodyLine + totalLine

# def create_spend_chart(categories):
