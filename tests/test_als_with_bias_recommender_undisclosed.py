import sys
sys.path.insert(0, './answers')
from answer import als_with_bias_recommender

def test_als_with_bias_recommender_undisclosed():
    a = als_with_bias_recommender("./data/sample_movielens_ratings.txt", 1234)
    assert(abs(a-1.07)<0.03)
