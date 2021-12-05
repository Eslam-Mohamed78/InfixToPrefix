from project import *

def prefixEval(prefixExpr):
    operandStack = Stack()
    tokenList = prefixExpr.split()
    tokenList.reverse()

    for token in tokenList:
        if token not in "^*/-+":
            operandStack.push(float(token))
        else:
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(float(result))
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "^" or op == "**":
        return op1 ** op2
    else:
        return op1 - op2


theInfixExpr = input('Please enter the infix expression without quotes: ')

thePrefixExpr = infixToprefix(theInfixExpr)

print('The Prefix Expression is', thePrefixExpr)

print('The result after Evaluating the prefix Expression is', prefixEval(thePrefixExpr))

# Infix expressions for testing
# 5 * 3 ** ( 4 - 2 )
# ( 1 + 2 ) * 3 - ( 4 - 5 ) * ( 6 + 7 )
