import budget


class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description = None):
        amount = amount
        if description is None:
            description = ''
        else:
            description = description
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = None):
        if budget.Category.check_funds(self,amount):
            if description is None:
                description = ''
            else:
                description = description
            self.ledger.append({"amount": - amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        currentBalance = 0
        for i in self.ledger:
            currentBalance += i["amount"]
        return currentBalance

    def transfer(self, amount, category):
        if budget.Category.check_funds(self,amount):
            budget.Category.withdraw(self,amount,'Transfer to [' + category + ']')
            return True
        else:
            return False

    def check_funds (self, amount):
        if budget.Category.get_balance(self) - amount < 0:
            return False
        else:
            return True

    def








# def create_spend_chart(categories):