import sys
sys.path.insert(0, './answers')
from answer import means_and_interaction

def test_means_and_interaction_undisclosed():
    a = means_and_interaction("./data/sample_movielens_ratings.txt", 1234, 19)
    assert(a==open("tests/means_and_interaction_undisclosed.txt","r").read())
