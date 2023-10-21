import sys


def format_kata(kata: dict[str]):
    for key, val in kata.items():
        print("%s was created by %s" % (key, val))


if __name__ == '__main__':
    sys.tracebacklimit = 0
    kata = dict(Python='Guido van Rossum',
                Ruby='Yukihiro Matsumoto', PHP='Rasmus Lerdorf')
    assert type(kata) is dict, 'the kata variable must be a dict of strings'
    assert all([type(val) is str for val in kata.values()]
               ), 'Tuple items must be strings'
