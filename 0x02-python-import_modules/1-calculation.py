#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    result = a + b
    result_sub = a - b
    result_mul = a * b
    result_div = a / b
    print("{:d} + {:d} = {:d}".format(a, b, result))
    print("{:d} - {:d} = {:d}".format(a, b, result_sub))
    print("{:d} * {:d} = {:d}".format(a, b, result_mul))
    print("{:d} / {:d} = {:d}".format(a, b, result_div))
