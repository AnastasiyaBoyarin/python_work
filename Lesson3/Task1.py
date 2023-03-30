class CustomError(Exception):
    pass


def get_time_of_year_by_using_list(month):
    """

    :param month: number of month
    :return: time of year
    """

    list_of_time_year = ["Winter", "Spring", "Summer", "Autumn"]

    if month <= 2 or month == 12:
        return list_of_time_year[0]
    elif 2 < month <= 5:
        return list_of_time_year[1]
    elif 5 < month <= 8:
        return list_of_time_year[2]
    elif 8 < month <= 11:
        return list_of_time_year[3]


def get_time_of_year_by_using_dictionary(month):
    """

    :param month: number of month
    :return: time of year
    """
    dictionary_of_month = {"Winter": (12, 1, 2), "Spring": (3, 4, 5),
                           "Summer": (6, 7, 8), "Autumn": (9, 10, 11)}

    result = None

    for key in dictionary_of_month:
        number_month = dictionary_of_month[key]
        for element in number_month:
            if month == element:
                result = key
                break

    return result


try:
    number_of_month = int(input("Enter number of month from 1 to 12:"))
    if number_of_month < 0:
        raise CustomError
    else:
        number_year = get_time_of_year_by_using_list(number_of_month)
        print(f"Result by using list: {number_year}")

        number_year = get_time_of_year_by_using_dictionary(number_of_month)
        print(f"Result by using dictionary: {number_year}")

except CustomError:
    print("You entered not positive number")
except ValueError:
    print("You entered string value")
