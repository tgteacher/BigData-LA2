import sys
sys.path.insert(0, './answers')
from answer import global_average

def test_global_average():
    a = global_average("./data/sample_movielens_ratings.txt", 123)
    assert(abs(a-1.77491694352)<0.01)
