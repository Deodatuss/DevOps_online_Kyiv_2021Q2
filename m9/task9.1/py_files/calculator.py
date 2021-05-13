def calc(number1, number2, operation):
    class CustomError(Exception):
        pass

    if not(type(number1) is int or type(number1) is float):
        raise CustomError("Input error: invalid data type for first number, has to be int or float")
    elif not(type(number2) is int or type(number2) is float):
        return CustomError("Input error: invalid data type for second number, has to be int or float")

    if operation == '+':
        return number1+number2
    elif operation == '-':
        return number1-number2
    elif operation == '*':
        return number1*number2
    elif operation == '/':
        return number1/number2
    elif operation == '^':
        return number1**number2
    else:
        raise CustomError("Input error: invalid operation")
