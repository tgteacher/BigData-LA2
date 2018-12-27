import sys
sys.path.insert(0, './answers')
from answer import basic_als_recommender

def test_basic_als_undisclosed():
    a = basic_als_recommender("./data/sample_movielens_ratings.txt", 1234)
    assert(abs(a-1.6)<0.05)
