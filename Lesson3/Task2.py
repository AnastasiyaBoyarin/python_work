print("Structure <Rating>")
print("In order to finish cycle enter exit code -1")


def rating(arg_list):
    """

    :param arg_list: defined list
    :return:
    """
    print(arg_list)
    new_number = int(input("Enter new element of rating: "))
    while new_number != -1:
        for element in arg_list:
            if new_number > element:
                arg_list.insert((arg_list.index(element)), new_number)
                print(arg_list)
                break
            elif new_number <= min(arg_list):
                element = min(arg_list)
                arg_list.insert((arg_list.index(element) + 1),
                                new_number)
                print(arg_list)
                break
        new_number = int(input("Enter new element of rating: "))
    print(arg_list)


rating_list = [8, 7, 5, 5, 3, 3, 2]
rating(rating_list)
