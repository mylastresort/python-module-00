from time import sleep
from sys import stdout
from datetime import datetime as dt


def ft_progress(lst):
    for i in lst:
        yield i


def get_percentage(i, m): return int(i * 100 / m)


def symbolic_scale(scale): return ''.join(
    '=' if i != scale else '>' for i in range(1, scale))


def get_estimated_time(
    duration, limit, i): return duration * (limit / (i or 1) - 1)


def formated_bar(est, per, scl, i, limit,
                 dur): return '\rETA: {:.2f}s [{:3}%] [{:10}] {}/{} | elapsed time {:.2f}'.format(est, per, scl, i, limit, dur)


if __name__ == '__main__':
    limit = 3333
    listy = range(0, limit + 1)
    time = dt.now()
    for i in ft_progress(listy):
        per = get_percentage(i, limit)
        duration = (dt.now() - time).total_seconds()
        est = get_estimated_time(duration, limit, i)
        stdout.write(formated_bar(est, per, symbolic_scale(
            int(per / 10)), i, limit, duration))
        sleep(0.005)
