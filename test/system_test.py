import timeit

def func(i):
    return i * 2

def test_performance():
    assert 1 > timeit.timeit("[func(x) for x in range(20)]", number=5,
                              setup="from __main__ import func")

test_performance()