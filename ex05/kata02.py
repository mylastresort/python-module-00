import sys


def formated_kata(kata): return '{:02}/{:02}/{:04} {:02}:{:02}'.format(
    kata[1], kata[2], kata[0], kata[3], kata[4])


if __name__ == '__main__':
    sys.tracebacklimit = 0
    kata = (2019, 9, 25, 3, 30)
    assert type(kata) is tuple and len(kata) == 5 and kata[0] <= 9999 and kata[1] <= 99 and kata[2] <= 99 and kata[
        3] <= 99 and kata[4] <= 99, 'kata must be a tuple of integers with this format: (YYYY, M, D, H, M)'
    print(formated_kata(kata))
