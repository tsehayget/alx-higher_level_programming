#!/usr/bin/python3
def print_last_digit(number):
    t = int(repr(number)[-1])
    print("{}".format(t), end="")
    return t
