import sys
sys.path.insert(0, './answers')
from answer import means_and_interaction

def test_means_and_interaction():
    a = means_and_interaction("./data/sample_movielens_ratings.txt", 123, 17)
    assert(a==open("tests/means_and_interaction.txt","r").read())
