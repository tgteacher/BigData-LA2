import sys
sys.path.insert(0, './answers')
from answer import means_and_interaction
from pyspark.sql import Row

def test_means_and_interaction():
    res = [Row(userId=0,  movieId=2,  rating=3.0, user_mean=1.4615384615384615, item_mean=2.1875,             user_item_interaction=1.1258784819831331), \
            Row(userId=0, movieId=9,  rating=4.0, user_mean=1.4615384615384615, item_mean=1.5,                user_item_interaction=2.813378481983133), \
            Row(userId=0, movieId=11, rating=1.0, user_mean=1.4615384615384615, item_mean=1.4,                user_item_interaction=-0.08662151801686635), \
            Row(userId=0, movieId=12, rating=2.0, user_mean=1.4615384615384615, item_mean=1.7272727272727273, user_item_interaction=0.586105754710406), \
            Row(userId=0, movieId=19, rating=1.0, user_mean=1.4615384615384615, item_mean=1.6153846153846154, user_item_interaction=-0.30200613340148186), \
            Row(userId=0, movieId=21, rating=1.0, user_mean=1.4615384615384615, item_mean=1.3571428571428572, user_item_interaction=-0.043764375159723645), \
            Row(userId=0, movieId=23, rating=1.0, user_mean=1.4615384615384615, item_mean=2.6153846153846154, user_item_interaction=-1.3020061334014819), \
            Row(userId=0, movieId=26, rating=3.0, user_mean=1.4615384615384615, item_mean=1.4166666666666667, user_item_interaction=1.8967118153164666), \
            Row(userId=0, movieId=27, rating=1.0, user_mean=1.4615384615384615, item_mean=1.8571428571428572, user_item_interaction=-0.5437643751597236), \
            Row(userId=0, movieId=29, rating=1.0, user_mean=1.4615384615384615, item_mean=2.5294117647058822, user_item_interaction=-1.2160332827227491), \
            Row(userId=0, movieId=30, rating=1.0, user_mean=1.4615384615384615, item_mean=2.5833333333333335, user_item_interaction=-1.2699548513502), \
            Row(userId=0, movieId=31, rating=1.0, user_mean=1.4615384615384615, item_mean=1.5714285714285714, user_item_interaction=-0.25805008944543806), \
            Row(userId=0, movieId=37, rating=1.0, user_mean=1.4615384615384615, item_mean=1.5714285714285714, user_item_interaction=-0.25805008944543806), \
            Row(userId=0, movieId=41, rating=2.0, user_mean=1.4615384615384615, item_mean=1.6666666666666667, user_item_interaction=0.6467118153164666), \
            Row(userId=0, movieId=44, rating=1.0, user_mean=1.4615384615384615, item_mean=1.4,                user_item_interaction=-0.08662151801686635), \
            Row(userId=0, movieId=46, rating=1.0, user_mean=1.4615384615384615, item_mean=1.8888888888888888, user_item_interaction=-0.5755104069057553), \
            Row(userId=0, movieId=47, rating=1.0, user_mean=1.4615384615384615, item_mean=1.8,                user_item_interaction=-0.4866215180168667)]
    a = means_and_interaction("./data/sample_movielens_ratings.txt", 123, 17)
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
