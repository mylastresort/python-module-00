import sys


def formated_kata(kata): return '{:->42}'.format(kata)


if __name__ == '__main__':
    sys.tracebacklimit = 0
    kata = "The right format"
    assert type(kata) is str and len(
        kata) <= 42, 'kata must be a string of less than 42 characters'
    print(formated_kata(kata), end='')
