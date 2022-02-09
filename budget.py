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
            category.deposit(amount, 'Transfer from ' + self.name)
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

def create_spend_chart(categories):
    titleLine = 'Percentage spent by category'
    totalWithdrawalOfCategory = list()
    for i in categories:
        sum = 0
        for j in i.ledger:
            if j["amount"] < 0:
                sum += j["amount"]
        totalWithdrawalOfCategory.append(-sum)

    sumOfWithdrawal = 0
    for i in totalWithdrawalOfCategory:
        sumOfWithdrawal += i

    percentageOfCategory = list()
    for i in totalWithdrawalOfCategory:
        percentageOfCategory.append(i/sumOfWithdrawal*100//10*10)

    line100 = '100| '
    line90 = ' 90| '
    line80 = ' 80| '
    line70 = ' 70| '
    line60 = ' 60| '
    line50 = ' 50| '
    line40 = ' 40| '
    line30 = ' 30| '
    line20 = ' 20| '
    line10 = ' 10| '
    line00 = '  0| '
    lineDash = '    ----' + '---'*(len(categories)-1)

    for i in percentageOfCategory:
        if i >= 100:
            line100 += 'o  '
        if i >= 90:
            line90 += 'o  '
        if i >= 80:
            line80 += 'o  '
        if i >= 70:
            line70 += 'o  '
        if i >= 60:
            line60 += 'o  '
        if i >= 50:
            line50 += 'o  '
        if i >= 40:
            line40 += 'o  '
        if i >= 30:
            line30 += 'o  '
        if i >= 20:
            line20 += 'o  '
        if i >= 10:
            line10 += 'o  '
        if i >= 0:
            line00 += 'o  '

    categoriesName = list()
    for i in categories:
        categoriesName.append(i.name)
    # print(categoriesName)

    nameLenMax = 0
    for i in range(len(categories)):
        if len(categoriesName[i]) > nameLenMax:
            nameLenMax = len(categoriesName[i])

    categoriesNameModifyList = list()
    for i in categoriesName:
        if len(i) < nameLenMax:
            i = i + ' '*(nameLenMax - len(i))
            categoriesNameModifyList.append(i)
        else:
            categoriesNameModifyList.append(i)

    if len(categoriesNameModifyList) < 4:
        for i in range(4 - len(categoriesNameModifyList)):
            categoriesNameModifyList.append(' '*nameLenMax)
    print(categoriesNameModifyList)



    namePrint = ''
    for i in range(nameLenMax):
        namePrint += '     ' + categoriesNameModifyList[0][i] + '  ' + categoriesNameModifyList[1][i] + '  ' + categoriesNameModifyList[2][i] + '  ' + categoriesNameModifyList[3][i] + '\n'




    printResult = titleLine + '\n' + line100 + '\n' + line90 + '\n' + line80 + '\n'\
                + line70 + '\n' + line60 + '\n' + line50 + '\n' + line40 + '\n'\
                + line30 + '\n' + line20 + '\n' + line10 + '\n' + line00 + '\n' + lineDash + '\n' \
                + namePrint


    return printResult
