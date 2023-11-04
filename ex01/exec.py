import sys


def rev_alpha(args: list[str]):
    return ' '.join(word[::-1].swapcase() for word in ' '.join(args).split()[::-1])


if __name__ == '__main__':
    sys.tracebacklimit = 0
    args = sys.argv[1:]
    assert args, 'An argument was expected'
    print(rev_alpha(args))
