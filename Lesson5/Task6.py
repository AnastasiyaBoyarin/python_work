import random

attempt = 0


def find_random_number_recursion(num):
    global attempt

    potential_number = int(input("Enter potential number:"))

    if attempt == 10:
        return
    else:
        attempt += 1
        if potential_number == num:
            print("You are right!")
            return
    find_random_number_recursion(num)


random_number = random.randint(0, 100)
print(random_number)
find_random_number_recursion(random_number)

