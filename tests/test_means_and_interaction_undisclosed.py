import sys
sys.path.insert(0, './answers')
from answer import means_and_interaction
from pyspark.sql import Row

def test_means_and_interaction_undisclosed():
    res = [Row(userId=0, movieId=3, rating=1.0, user_mean=1.4857142857142858,   item_mean=1.3076923076923077, user_item_interaction=-0.007981492192018269), \
            Row(userId=0, movieId=5, rating=2.0, user_mean=1.4857142857142858,  item_mean=1.5555555555555556, user_item_interaction=0.7441552599447339), \
            Row(userId=0, movieId=9, rating=4.0, user_mean=1.4857142857142858,  item_mean=1.5384615384615385, user_item_interaction=2.761249277038751), \
            Row(userId=0, movieId=11, rating=1.0, user_mean=1.4857142857142858, item_mean=1.4444444444444444, user_item_interaction=-0.14473362894415542), \
            Row(userId=0, movieId=12, rating=2.0, user_mean=1.4857142857142858, item_mean=1.6666666666666667, user_item_interaction=0.6330441488336223), \
            Row(userId=0, movieId=15, rating=1.0, user_mean=1.4857142857142858, item_mean=1.1764705882352942, user_item_interaction=0.12324022726499484), \
            Row(userId=0, movieId=21, rating=1.0, user_mean=1.4857142857142858, item_mean=1.4666666666666666, user_item_interaction=-0.16695585116637757), \
            Row(userId=0, movieId=26, rating=3.0, user_mean=1.4857142857142858, item_mean=1.1666666666666667, user_item_interaction=2.1330441488336223), \
            Row(userId=0, movieId=27, rating=1.0, user_mean=1.4857142857142858, item_mean=1.9230769230769231, user_item_interaction=-0.6233661075766341), \
            Row(userId=0, movieId=31, rating=1.0, user_mean=1.4857142857142858, item_mean=1.8333333333333333, user_item_interaction=-0.5336225178330438), \
            Row(userId=0, movieId=34, rating=1.0, user_mean=1.4857142857142858, item_mean=1.5555555555555556, user_item_interaction=-0.25584474005526614), \
            Row(userId=0, movieId=37, rating=1.0, user_mean=1.4857142857142858, item_mean=1.2,                user_item_interaction=0.09971081550028904), \
            Row(userId=0, movieId=41, rating=2.0, user_mean=1.4857142857142858, item_mean=1.8888888888888888, user_item_interaction=0.4108219266114004), \
            Row(userId=0, movieId=44, rating=1.0, user_mean=1.4857142857142858, item_mean=1.2307692307692308, user_item_interaction=0.06894158473105838), \
            Row(userId=0, movieId=47, rating=1.0, user_mean=1.4857142857142858, item_mean=1.6666666666666667, user_item_interaction=-0.36695585116637774), \
            Row(userId=0, movieId=48, rating=1.0, user_mean=1.4857142857142858, item_mean=1.7333333333333334, user_item_interaction=-0.4336225178330442), \
            Row(userId=0, movieId=50, rating=1.0, user_mean=1.4857142857142858, item_mean=1.7857142857142858, user_item_interaction=-0.48600347021399637), \
            Row(userId=0, movieId=51, rating=1.0, user_mean=1.4857142857142858, item_mean=2.066666666666667,  user_item_interaction=-0.7669558511663777), \
            Row(userId=0, movieId=54, rating=1.0, user_mean=1.4857142857142858, item_mean=1.6,                user_item_interaction=-0.30028918449971087)]
    a = means_and_interaction("./data/sample_movielens_ratings.txt", 1234, 19)
    assert(len(a) == len(res))
    for i in range(len(res)):
        res_row = res[i]
        a_row = a[i]
        assert(res_row["userId"] == a_row["userId"])
        assert(res_row["movieId"] == a_row["movieId"])
        assert(res_row["rating"] == a_row["rating"])
        assert(abs(res_row["user_mean"] - a_row["user_mean"]) < 0.03)
        assert(abs(res_row["item_mean"] - a_row["item_mean"]) < 0.03)
        assert(abs(res_row["user_item_interaction"] - a_row["user_item_interaction"]) < 0.03)
