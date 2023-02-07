import os

from answers.answer import global_average


def test_global_average():
    a = global_average(os.path.join(".", "data", "sample_movielens_ratings.txt"), 123)
    assert abs(a - 1.77491694352) < 0.01
