#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv)
    if nargs != 4
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
        op = sys.argv[2]
        if op != '+' and op != '-' and op != '*' and op != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            quit(1)
            from calculator_1 import add, sub, mul, div
            a = int(argv[1])
            b = int(argv[3]
                    [funcs = [add, sub, mul, div]
                    op = sys.argv[2]
                    print("{} {} {} = {}".format(a, op, b, funcs[i](a, b)))
