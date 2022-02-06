import re


def arithmetic_arranger(listOfProblems, see=None):
    if len(listOfProblems) > 5:
        print('Error: Too many problems.')
        return

    listNum1 = list()
    listOperator = list()
    listNum2 = list()
    listResult = list()

    for i in listOfProblems:

        num1 = i.split()[0]
        if re.search('[a-z]',num1):
            print('Error: Numbers must only contain digits.')
            return
        else:
            listNum1.append(num1)

        operator = i.split()[1]
        listOperator.append(operator)

        num2 = i.split()[2]
        if re.search('[a-z]',num2):
            print('Error: Numbers must only contain digits.')
            return
        else:
            listNum2.append(num2)

        if operator == "+":
            result = int(num2) + int(num1)
            listResult.append(str(result))
        elif operator == "-":
            result = int(num1) - int(num2)
            listResult.append(str(result))
        else:
            print("Error: Operator must be '+' or '-'.")
            return

    # print(listNum1)
    if len(listNum1) > len(listOfProblems) or len(listNum2) > len(listOfProblems):
        print('Error: Numbers must only contain digits.')
        return

    for i in range(len(listNum1)):
        if len(listNum1[i]) > 4 or len(listNum2[i]) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return

    listDigits = list()
    for i in range(len(listNum1)):
        if len(listNum1[i]) > len(listNum2[i]):
            listDigits.append(len(listNum1[i]))
        else:
            listDigits.append(len(listNum2[i]))

    listDash = list()
    for i in listDigits:
        listDash.append('-'*(2+i))



    # print(listNum1)
    # print(listOperator)
    # print(listNum2)
    # print(listDash)
    # print(listResult)

    upperLine = ''
    for i in range(len(listNum1)):
        if i ==0:
            # upperLine += listNum1[i].rjust(6+listDigits[i]+2-len(listNum1[i]))
            upperLine += ' '*(listDigits[i] + 2 - len(listNum1[i]) ) + listNum1[i]

        else:
            upperLine += '    ' + ' '*(listDigits[i] + 2 - len(listNum1[i]) ) + listNum1[i]

    # print(upperLine)

    secondLine = ''
    for i in range(len(listNum2)):
        if i==0:
            secondLine += listOperator[i] + ' '*(listDigits[i]-len(listNum2[i]) + 1) +listNum2[i]
        else:
            secondLine += '    '+ listOperator[i] + ' '*(listDigits[i]-len(listNum2[i]) + 1) +listNum2[i]
    # print(secondLine)

    dashLine = ''
    for i in range(len(listDash)):
        if i==0:
            dashLine += listDash[i]
        else:
            dashLine += '    ' + listDash[i]
    # print(dashLine)

    resultLine = ''
    for i in range(len(listResult)):
        if i==0:
            resultLine += ' '*(listDigits[i]+2-len(listResult[i])) + listResult[i]
        else:
            resultLine += '    ' + ' '*(listDigits[i]+2-len(listResult[i])) + listResult[i]
    # print(resultLine)

    print(upperLine)
    print(secondLine)
    print(dashLine)

    if see == True:
        print(resultLine)
# def arithmetic_arranger(lst):
#     see = False
#     arithmetic_arranger(lst,see)




exp2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
exp1 = ["321 + 698", "3801 + 2", "45 + 43", "123 + 49",'1 + 2']
# arithmetic_arranger(exp2,True)
arithmetic_arranger(exp1)
