def isValid(number):
    max = 16
    min = 13


    list_iterator = iter(number)
    count = 0
    while True:
        try:
            next(list_iterator)
            count +=1
        except StopIteration:
            break
    print(count)

    if count > max:
        print("card number is too long/invalid")
    elif count < min:
        print("card number is too short/invalid")
    else:
        print("card is valid!!")

isValid("12345678912345")