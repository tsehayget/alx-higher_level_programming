#!/usr/bin/python3
from calculator_1 import add, mul, sub, div
from sys import argv

if __name__ == '__main__':
    argc = (len(argv) - 1)
    operators = ['+', '-', '*', '/']
    functions = [add, sub, mul, div]

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

        a = int(argv[1])
        b = int(argv[3])

        for symbols in range(len(operators)):
            if argv[2] == operators[symbols]:
                calc = functions[symbols](a, b)
                sign = operators[symbols]
                break

        if argv[2] != operators[symbols]:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

            print("{:d} {} {:d} = {:d}".format(a, sign, b, calc))
            exit(0)
