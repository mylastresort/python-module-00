import sys


def format_kata(kata): return "The %d numbers are: %s" % (
    len(kata), ', '.join(str(num) for num in kata))


if __name__ == '__main__':
    sys.tracebacklimit = 0
    kata = (19, 21, 42)
    assert type(
        kata) is tuple, 'the kata variable must be a tuple of integers only'
    assert all(type(item) is int for item in kata), 'Tuple items must be integers'
    print(format_kata(kata))
