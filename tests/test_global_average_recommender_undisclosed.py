import sys
sys.path.insert(0, './answers')
from answer import global_average_recommender

def test_global_average_recommender_undisclosed():
    a = global_average_recommender("./data/sample_movielens_ratings.txt", 1234)
    assert(abs(a-1.15)<0.02)
