import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import basic_als_recommender

def test_basic_als():
    a = basic_als_recommender(os.path.join('.', 'data', 'sample_movielens_ratings.txt'), 123)
    try:
        assert(abs(a-1.62)<0.03)
    except:
        assert(abs(a-1.56)<0.03)
