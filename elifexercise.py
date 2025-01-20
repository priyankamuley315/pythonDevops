def isValid(number):
    max = 16
    min = 13
    if len(number) > max :
        print("the number length is invalid")
    elif len(number) < min :
        print("the number length is invalid/short")
    else:
        print("the number length is valid")
        print("Number is", number)


    number_str = str(number)
    first_digit = number_str[0]
    print(first_digit)
        # print(number_str[1])
    if first_digit == "4" :
        print("The first card is valid enough")
    elif number_str[0] == "3" and number_str[1] == "1":
        print("The first card is valid")
    else:
        print("First card number is not validddd")
        quit()


isValid("312345678912345")

