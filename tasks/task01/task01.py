import math

i = 1


def is_narcissistic(number: int):
    number_of_digits = int(math.log10(number) + 1)
    result = 0
    numbers_list = [int(x) for x in str(number)]

    for n in numbers_list:
        result += n ** number_of_digits

    if result == number:
        return True

    return False


while i <= 1000:
    if is_narcissistic(i):
        print(i)
    i += 1
