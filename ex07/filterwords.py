import string
import sys


def filterwords(text, count): return [word.strip(string.punctuation) for word in text.split()
                                      if sum([char not in string.punctuation for char in word]) > count]


if __name__ == '__main__':
    sys.tracebacklimit = 0
    args = sys.argv[1:]
    assert len(args) == 2, 'wrong number of arguments'
    try:
        print(filterwords(args[0], int(args[1])))
    except:
        print(
            'AssertionError: program accepts this formats <text> <number>', file=sys.stderr)
