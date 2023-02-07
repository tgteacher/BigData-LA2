import os

from answers.answer import global_average_recommender


def test_global_average_recommender():
    a = global_average_recommender(
        os.path.join(".", "data", "sample_movielens_ratings.txt"), 123
    )
    assert abs(a - 1.16693421444) < 0.01
