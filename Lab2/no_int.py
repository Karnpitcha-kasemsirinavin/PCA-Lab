
def from_decimal(decimal_num, base):

    result = ""

    if decimal_num == 0:
        result = "0"

    else:

        while decimal_num > 0:
            remainder = decimal_num % base
            decimal_cal, unwanted = (str(decimal_num/base).split("."))

            decimal_num = 0
            decimal_cal = decimal_cal[::-1]

            for index in range(0, len(decimal_cal)):
                decimal_num += (ord(decimal_cal[index]) - 48) * (10 ** index)

            if remainder < 10:
                result = str(remainder) + result

            elif remainder >= 10:
                letter_value = chr(remainder + 55)
                result = letter_value + result

    print(f"result: {result}")


def to_decimal(base_num, base_sys):

    decimal_num = 0

    base_num = str(base_num)[::-1]

    if base_num.isnumeric():
        for number in range(0, len(base_num)):
            decimal_num = decimal_num + (ord(base_num[number])-48)*base_sys**number

    else:

        for number in range(0, len(base_num)):

            if base_num[number].isalpha():
                decimal_num = decimal_num + (ord(base_num[number]) - 55) * base_sys ** number

            else:
                decimal_num = decimal_num + (ord(base_num[number])-48) * base_sys ** number

    result = str(decimal_num)

    print(f"result: {result}")


def select_function():

    command, input_info = input("Enter command: ").split("(")
    input_info = input_info.replace(")", "").replace(" ", "")
    first_input, second_input = input_info.split(",")

    second_calculated = 0
    first_calculated = 0
    check_value = True
    second_input = second_input[::-1]

    for index in range(0, len(second_input)):
        second_calculated += (ord(second_input[index])-48)*(10**index)

    if "-" in first_input:
        print("Error :negative number")

    elif "-" in second_input:
        print("Error :negative base")

    elif second_calculated < 2:
        print("Error :base < 2")

    elif second_calculated > 36:
        print("Error :base > 36")

    else:

        try:
            first_input = first_input.strip('"')
            # first_input = first_input[1:(len(first_input) - 1)]
        except IndexError:
            pass

        if first_input.isnumeric():

            first_input = first_input[::-1]

            for index in range(0, len(first_input)):
                first_calculated += (ord(first_input[index])-48)*(10**index)

        else:
            first_calculated = first_input

        if command == 'from_decimal':
            from_decimal(first_calculated, second_calculated)

        elif command == 'to_decimal':

            first_input = first_input[1:(len(first_input)-1)]

            for index in range(0, len(first_input)):
                if first_input[index].isalpha():
                    if ord(first_input[index]) - 55 > second_calculated:
                        print(ord(first_input[index]) - 55)
                        check_value = False
                else:
                    if ord(first_input[index]) - 48 > second_calculated:
                        check_value = False

            if check_value is True:
                to_decimal(first_calculated, second_calculated)
            else:
                print("Error: incorrect number/base")


select_function()
