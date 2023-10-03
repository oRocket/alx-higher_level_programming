#!/usr/bin/python3
def print_last_digit(num):  # num = number
    if num >= 0:
        l_digit = num % 10  # l_digit = last digit
    else:
        l_digit = num % -10
        l_digit *= -1

    print("{:d}".format(l_digit), end='')
    return (l_digit)
