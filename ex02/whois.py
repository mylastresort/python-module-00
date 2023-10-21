import sys


def whois(num: int):
    return "I'm Zero." if num == 0 else "I'm Even." if num % 2 == 0 else "I'm Odd."


if __name__ == '__main__':
    sys.tracebacklimit = 0
    args = sys.argv[1:]
    assert args, 'Please provide one argument'
    assert len(args) == 1, 'More than one argument were provided'
    arg = args[0]
    assert type(int(arg)) is int, 'Argument is not an integer'
    print(whois(int(arg)))
