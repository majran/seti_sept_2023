MAX_BASE = 16


# binary_decimal = (
#     {"decimal": 100, "binary": [1, 1, 0, 0, 1, 0, 0]},
#     {"decimal": 2, "binary": [1, 0]},
#     {"decimal": 0, "binary": [0]},
#     {"decimal": 1, "binary": [1]},
#     {"decimal": 64, "binary": [1, 0, 0, 0, 0, 0, 0]},
# )

def decimal_to_binary(decimal_number):
    """Returns the array of digits in binary representation of a decimal number"""
    return decimal_to_base(decimal_number, 2)


def binary_to_decimal(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    return base_to_decimal(binary_digits, 2)


def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    if decimal_number == 0:
        return [0]
    binary = []
    while decimal_number > 0:
        div_result = decimal_number // destination_base
        remainder = decimal_number % destination_base
        binary.append(remainder)
        decimal_number = div_result
    return binary[::-1]


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    source = digits[::-1]
    result = 0
    for index, digit in enumerate(source):
        result += digit * original_base ** index
    return result


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""

    if not (2 <= base <= 16) or not digits:
        raise ValueError

    map = {
        10: 'A',
        11: 'B',
        12: "C",
        13: 'D',
        14: 'E',
        15: 'F'

    }
    for index, number in enumerate(digits):
        if  not (0 <= number <= 15):
            raise ValueError

        if number > 9:
            digits[index] = map[number]

    return "".join([str(d) for d in digits])


#
# any_to_any_base = (
#     {"digits": [1, 0, 0], "source": 10, "target": 2, "result": [1, 1, 0, 0, 1, 0, 0]},
#     {"digits": [5, 1, 5], "source": 8, "target": 16, "result": [1, 4, 13]},
#     {"digits": [1, 4, 13], "source": 16, "target": 8, "result": [5, 1, 5]},
# )
def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    decimal = base_to_decimal(original_digits, original_base)
    return decimal_to_base(decimal, destination_base)


if __name__ == '__main__':
    number = input("daj number: ")
    print(decimal_to_binary(int(number)))

