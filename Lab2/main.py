"""Converting decimal number into the input base system"""


def from_decimal(decimal_num, base_sys):

    result = ''

    while int(decimal_num) > 0:
        remainder = int(decimal_num) % base_sys
        decimal_num, unwanted = (str(int(decimal_num)/base_sys)).split(".")

        if remainder < 10:
            result = str(remainder) + result

        elif remainder >= 10:
            letter = chr(remainder+55)
            result = letter + result

    if result == '':
        result = '0'

    print(result)


"""Converting input base number into decimal number"""


def to_decimal(base_num, base_sys):

    decimal_num = 0
    check_value = True

    base_num = str(base_num)[::-1]

    if base_num.isnumeric():

        for number in range(0, len(base_num)):
            if int(base_num[number]) >= base_sys:
                check_value = False
            else:
                decimal_num = decimal_num + int(base_num[number])*base_sys**number

    else:

        for number in range(0, len(base_num)):

            if base_num[number].isalpha():
                transform_number = ord(base_num[number]) - 55
                if transform_number >= base_sys:
                    check_value = False
                else:
                    decimal_num = decimal_num + transform_number * base_sys ** number

            else:
                if int(base_num[number]) >= base_sys:
                    check_value = False
                else:
                    decimal_num = decimal_num + int(base_num[number]) * base_sys ** number

    if check_value is False:
        print("Error: incorrect number/base")

    else:
        result = str(decimal_num)
        print(result)


"""Selecting function
convert from decimal number to number in the input base system: from_decimal(decimal number, base system)
convert to decimal: to_decimal(number, base system)"""


def select_function():

    command, input_num = input("Enter command: ").split("(")
    input_num = input_num.strip(")")
    first_input, second_input = input_num.split(",")
    base_sys = int(second_input)

    if "-" in first_input:
        print("Error :negative number")

    elif base_sys < 0:
        print("Error :negative base")

    elif base_sys > 36:
        print("Error :base > 36")

    elif base_sys < 2:
        print("Error :base < 2")

    else:

        if command == 'from_decimal':
            from_decimal(first_input, base_sys)

        elif command == 'to_decimal':
            first_input = first_input[1:len(first_input)-1]
            to_decimal(first_input, base_sys)


select_function()
