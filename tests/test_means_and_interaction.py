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
    res2 = [Row(userId=0, movieId=2, rating=3.0, user_mean=1.5142857142857142, item_mean=2.2666666666666666, user_item_interaction=0.996545519971213), \
     Row(userId=0, movieId=3, rating=1.0, user_mean=1.5142857142857142, item_mean=1.25, user_item_interaction=0.013212186637879375),\
     Row(userId=0, movieId=9, rating=4.0, user_mean=1.5142857142857142, item_mean=1.6363636363636365, user_item_interaction=2.626848550274243),\
     Row(userId=0, movieId=11, rating=1.0, user_mean=1.5142857142857142, item_mean=1.3, user_item_interaction=-0.03678781336212045),\
     Row(userId=0, movieId=12, rating=2.0, user_mean=1.5142857142857142, item_mean=1.4615384615384615, user_item_interaction=0.8016737250994177),\
     Row(userId=0, movieId=17, rating=1.0, user_mean=1.5142857142857142, item_mean=1.9166666666666667, user_item_interaction=-0.6534544800287876),\
     Row(userId=0, movieId=19, rating=1.0, user_mean=1.5142857142857142, item_mean=1.6923076923076923, user_item_interaction=-0.42909550566981314),\
     Row(userId=0, movieId=21, rating=1.0, user_mean=1.5142857142857142, item_mean=1.4666666666666666, user_item_interaction=-0.2034544800287874),\
     Row(userId=0, movieId=23, rating=1.0, user_mean=1.5142857142857142, item_mean=2.3636363636363638, user_item_interaction=-1.1004241769984846),\
     Row(userId=0, movieId=26, rating=3.0, user_mean=1.5142857142857142, item_mean=1.4166666666666667, user_item_interaction=1.8465455199712124),\
     Row(userId=0, movieId=29, rating=1.0, user_mean=1.5142857142857142, item_mean=2.1176470588235294, user_item_interaction=-0.8544348721856501),\
     Row(userId=0, movieId=30, rating=1.0, user_mean=1.5142857142857142, item_mean=2.6666666666666665, user_item_interaction=-1.4034544800287865),\
     Row(userId=0, movieId=31, rating=1.0, user_mean=1.5142857142857142, item_mean=1.6666666666666667, user_item_interaction=-0.4034544800287876),\
     Row(userId=0, movieId=34, rating=1.0, user_mean=1.5142857142857142, item_mean=1.7, user_item_interaction=-0.4367878133621208),\
     Row(userId=0, movieId=41, rating=2.0, user_mean=1.5142857142857142, item_mean=1.8888888888888888, user_item_interaction=0.37432329774899054),\
     Row(userId=0, movieId=44, rating=1.0, user_mean=1.5142857142857142, item_mean=1.2, user_item_interaction=0.0632121866378792),\
     Row(userId=0, movieId=45, rating=2.0, user_mean=1.5142857142857142, item_mean=1.3333333333333333, user_item_interaction=0.9298788533045463)]
    a = means_and_interaction("./data/sample_movielens_ratings.txt", 123, 17)
    try:
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
    except:
        assert(len(a) == len(res2))
        for i in range(len(res2)):
            res2_row = res2[i]
            a_row = a[i]
            assert(res2_row["userId"] == a_row["userId"])
            assert(res2_row["movieId"] == a_row["movieId"])
            assert(res2_row["rating"] == a_row["rating"])
            assert(abs(res2_row["user_mean"] - a_row["user_mean"]) < 0.03)
            assert(abs(res2_row["item_mean"] - a_row["item_mean"]) < 0.03)
            assert(abs(res2_row["user_item_interaction"] - a_row["user_item_interaction"]) < 0.03)
