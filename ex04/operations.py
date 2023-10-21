import sys


def operations(A: int, B: int):
    print('{:14}{}\n{:14}{}\n{:14}{}\n{:14}{}\n{:14}{}'.format(
        'Sum:', A + B,
        'Difference:', A - B,
        'Product:', A * B,
        'Quotient:', A / B if B else 'ERROR (division by zero)',
        'Remainder:', A % B if B else 'ERROR (modulo by zero)'))


if __name__ == '__main__':
    sys.tracebacklimit = 0
    args = sys.argv[1:]
    if not args:
        print('Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3')
    else:
        assert len(args) <= 2, 'too many arguments'
        assert len(args) == 2, 'wrong number of arguments'
        try:
            operations(int(args[0]), int(args[1]))
        except:
            print('AssertionError: only integers', file=sys.stderr)
