import sys
sys.path.insert(0, './answers')
from answer import als_with_bias_recommender

def test_als_with_bias_recommender():
    a = als_with_bias_recommender("./data/sample_movielens_ratings.txt", 123)
    assert(abs(a-1.0409172341247102)<0.03)
