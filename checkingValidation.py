def checkingValidation(infix_Expr):
    countNumbers = 0
    countOperators = 0
    tokenList = infix_Expr.split()
    operatorList = ['+', '-', '*', '/', '^', '**']

    for token in tokenList:
        if token not in operatorList and token not in "()":
            countNumbers = countNumbers + 1
        elif token in operatorList:
            countOperators = countOperators + 1

    if countNumbers == countOperators + 1:
        return "Valid Expression"
    else:
        return "Not Valid Expression"


