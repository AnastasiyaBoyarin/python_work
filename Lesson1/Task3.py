print("Enter positive number n:")
n = int(input())

if n > 0:
    nn = str(n) * 2
    nnn = str(n) * 3
    sum_number = n + int(nn) + int(nnn)
    print(f"n + nn + nnn = {sum_number}")
else:
    print("You entered negative number. Could you please repeat again.")
