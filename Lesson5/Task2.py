even_number = odd_number = 0


def number_recursion(number_arg):
    """

    :param number_arg: input number
    :return:
    """
    global even_number
    global odd_number
    if number_arg <= 0:
        return
    else:
        if number_arg % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
        number_arg = number_arg // 10
    number_recursion(number_arg)


try:
    number = int(input("Enter the number:"))
    number_recursion(number)
    print(f"Even count is {even_number}, Odd count is {odd_number}")
except ValueError:
    print("You entered string value. Enter number.")
