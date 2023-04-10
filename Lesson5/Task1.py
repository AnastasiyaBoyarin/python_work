class CustomError(Exception):
    pass


def sum_func(a, b):
    """
    Addition of two numbers
    :param a: the first number
    :param b: the second number
    :return: Sum of two numbers
    """
    return a + b


def sub_func(a, b):
    """
    Substruction of two numbers
    :param a: the first number
    :param b: the second number
    :return: Substruction of two numbers
    """
    return a - b


def mult_func(a, b):
    """
    Multiplication of two numbers
    :param a: the first number
    :param b: the second number
    :return:  Multiplication of two numbers
    """
    return a * b


def div_func(a, b):
    """
    Division of two numbers
    :param a: the first number
    :param b: the second number
    :return: Division of two numbers
    """
    return a / b


def operation_recursion(argument):
    """

    :param argument: operation
    :return: function. it's recursion
    """
    print("Enter operation: +, -, *, / or 0 to exit program:")
    operation = input()
    result = None

    if operation == "0":
        return
    else:
        try:
            if (operation == '+') or (operation == '-') or (operation == '*') \
                    or (operation == '/'):
                first_number = int(input("Enter the first number:"))
                second_number = int(input("Enter the second number:"))

                if operation == '+':
                    result = sum_func(first_number, second_number)
                elif operation == '-':
                    result = sub_func(first_number, second_number)
                elif operation == '*':
                    result = mult_func(first_number, second_number)
                else:
                    result = div_func(first_number, second_number)

                print(f"Your result is: {result}")
            else:
                raise CustomError
        except CustomError:
            print("You entered invalid symbol. Enter +,-,*,/ or 0.")
        except ValueError:
            print("You entered string value. Enter number.")
        except ZeroDivisionError:
            print("You can not divide by zero. Enter new second number.")

    return operation_recursion(operation)


operation_recursion("")
