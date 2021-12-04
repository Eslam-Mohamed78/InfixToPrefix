from pythonds.basic.stack import Stack

def reversingList(x):
    y = x.split()
    y.reverse()
    for i in range(len(y)):
        if y[i] == '(':
            y[i] = ')'
        elif y[i] == ')':
            y[i] = '('
    return y

def infixToprefix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    prec["^"] = 4
    prec["**"] = 4
    opStack = Stack()
    prefixList = []
    tokenList = reversingList(infixexpr)

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                prefixList.append(topToken)
                topToken = opStack.pop()

        elif token == '^' or token == '**':
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                prefixList.append(opStack.pop())
            opStack.push(token)

        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] > prec[token]):
                  prefixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        prefixList.append(opStack.pop())

    prefixList.reverse()

    return " ".join(prefixList)

#  Testing the program
# print(infixToprefix("A + B * C + D"))
# print(infixToprefix("A * B + C * D"))
# print(infixToprefix("( A + B ) * ( C + D )"))  # error: remember spaces after and before '( )'
# print(infixToprefix("( A + B ) * C - ( D - E ) * ( F + G )"))
# print(infixToprefix("A + B * C ^ D / E - F"))
# print(infixToprefix("A * B + C / D"))
# print(infixToprefix("8 + 3 * 5 / ( 9 - 4 )"))
# print(infixToprefix("8 + 3 ^ 2 / ( 9 - 6 )"))