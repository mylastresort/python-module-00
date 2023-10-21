import sys


def formated_kata(kata): return 'module_{:02}, ex_{:02} : {:.2f}, {:.2e}, {:.2e}'.format(
    kata[0], kata[1], kata[2], kata[3], kata[4])


if __name__ == '__main__':
    sys.tracebacklimit = 0
    kata = (0, 4, 132.42222, 10000, 12345.67)
    assert type(kata) is tuple and len(kata) == 5 and kata[0] <= 99 and kata[1] <= 99 and type(kata[2]) is float and type(kata[3]) is int and type(kata[4]) is float, 'kata must be a tuple of integers with this format:\n\
            2 non-negative integer containing up to 2 digits\n\
            1 decimal\n\
            1 integer\n\
            1 decimal'
    print(formated_kata(kata))
