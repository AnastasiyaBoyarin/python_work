def reverse_recursion(number_arg, inc):
    global count_digit
    count = len(str(inc))
    if number_arg == 0:
        if count == count_digit - 1:
            return "0" + str(inc)
        else:
            return inc
    else:
        return reverse_recursion(number_arg // 10, inc * 10 + number_arg % 10)


try:
    number = int(input("Enter the number:"))
    count_digit = len(str(number))
    reversed_number = reverse_recursion(number, 0)
    print(f"Reverse of {number} is {reversed_number}")
except ValueError:
    print("You entered string value. Enter number.")
