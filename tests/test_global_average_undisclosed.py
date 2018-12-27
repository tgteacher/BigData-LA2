import sys
sys.path.insert(0, './answers')
from answer import global_average

def test_global_average_undisclosed():
    a = global_average("./data/sample_movielens_ratings.txt", 1234)
    assert(abs(a-1.78)<0.015)
