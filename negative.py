def make_negative(number):
    number = str(number)
    if number[0] == "-" or (number == "0"):
        return int(number)
    else:
        number2 = int(number) * -1
    return number2

print(make_negative(0))