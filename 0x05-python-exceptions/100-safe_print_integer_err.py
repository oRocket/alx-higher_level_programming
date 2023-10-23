#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        if "{:d}".format(value):
            print("{:d}".format(value))
            return True
    except ValueError:
        sys.stderr.write("Exception: Unknown format code 'd' for object of type '{}'\n".format(type(value)))
    return False
