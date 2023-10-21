import string
import sys


def text_analyzer(arg=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if arg is None:
        arg = input('What is the text to analyze?\n>> ')
    elif type(arg) is not str:
        print('AssertionError: argument is not a string', file=sys.stderr)
        return
    print("The text contains {} character(s):\n\
- %d upper letter(s)\n\
- %d lower letter(s)\n\
- %d punctuation mark(s)\n\
- %d space(s)" % (
        len(arg),
        sum([c.isupper() for c in arg]),
        sum([c.islower() for c in arg]),
        sum([c in string.punctuation for c in arg]),
        sum([c.isspace() for c in arg])))


if __name__ == "__main__":
    sys.tracebacklimit = 0
    args = sys.argv[1:]
    assert len(args) == 1, 'Wrong number of arguments'
    text_analyzer(args[0])
