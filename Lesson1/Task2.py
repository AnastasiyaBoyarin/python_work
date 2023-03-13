print("Enter time in seconds:")
seconds = int(input())

if seconds >= 0:
    hours = str(seconds // 3600)
    minutes = str(seconds // 60)

    print("Time in format h:m:s ")
    print("{} hours {} minutes {} seconds".format(hours, minutes, seconds))
else:
    print("You entered negative number. Could you please try again.")
