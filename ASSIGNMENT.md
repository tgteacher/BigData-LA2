# Assignment instructions

## 1. Recommender systems

### Preliminaries

With this assignment you will get a practical hands-on of recommender
systems in Spark. To begin, make sure you understand the example
at http://spark.apache.org/docs/latest/ml-collaborative-filtering.html
and that you can run it successfully. 

Important preliminary notes:

* The requested tasks, described below, are all evaluated with a test
  run with [pytest](http://pytest.org). Your assignment will be graded
  directly from the result of those tests, see details
  [here](./README.md). You may want to get familiar with pytest before
  you start.
  
* The tests contain examples of expected outputs that you may want to
  check in case the instruction below are unclear. Every detail in
  your answer counts! In particular, you should pay attention to the
  exact syntax of the expected output: add quotes around your answer
  and the tests won't pass!

* Your answers to the tasks below *must* be located in directory `answers`. 

### Dataset

We will use the MovieLens dataset sample provided with Spark and
available in directory `data`.

### Basic ALS recommender

#### Task

Write a script that prints the RMSE of recommendations obtained
through ALS collaborative filtering, similarly to the example at
http://spark.apache.org/docs/latest/ml-collaborative-filtering.html
The training ratio must be 80% and the test ratio must be 20%. The
random seed used to sample the training and test sets (passed to
`DataFrame.randomSplit`) must be an argument of the script. The seed
must also be used to initialize the ALS optimizer (use
*ALS.setSeed()*). The following parameters must be used in the ALS
optimizer:
- maxIter: 5
- rank: 70
- regParam: 0.01
- coldStartStrategy: 'drop'


#### Required syntax

`basic_als_recommender.py <seed>`

#### Test

`tests/test_basic_als.py`

### Global average rating

#### Task

Write a script that prints the global average rating for all users and
all movies in the training set. Training and test
sets should be determined as before.

#### Required syntax

`global_average.py`

#### Test

`tests/test_global_average.py`

### Global-average-based recommender

#### Task

Write a script that prints the RMSE of recommendations obtained
through global average, that is, the predicted rating for each
user-movie pair must be the global average computed in the previous
task. Training and test
sets should be determined as before. You can add a column to an existing DataFrame with function *.withColumn(...)*.

#### Required syntax

`global_average_recommender.py <seed>`

#### Test

`tests/test_global_average_recommender.py`

*Note:* compare the RMSEs obtained using the global-average
 recommender and the ALS one. Our basic ALS recommender does not
 perform well compared to the naive global-average
 approach. Although ALS parameters might be optimized (for instance,
 try increasing the number of max iterations or tuning the
 regularization parameter), this is fundamentally due to the fact that
 our current ALS method ignore user and item biases. In
 the remainder we will improve the basic ALS method by taking user and
 item biases into account.

### User mean, item mean and user-item interaction

#### Task

Write a script that prints the *n* first elements of a DataFrame
containing, for each (userId, movieId, rating) triple, the
corresponding user mean (computed on the training set), item mean
(computed on the training set) and user-item interaction *i* defined
as *i=rating-(user_mean+item_mean-global_mean)*. *n* must be passed on
the command line. The DataFrame must contain the following columns:

- userId # as in the input file
- movieId #  as in the input file
- rating # as in the input file
- user-mean # computed on the training set
- item-mean # computed on the training set 
- user-item-interaction # i = rating - (user_mean+item_mean-global_mean)

 Training and test
sets should be determined as before.

#### Required syntax

`means_and_interaction.py <seed> <n>`

#### Test

`tests/test_means_and_interaction.py`

*Note*: you should reuse this DataFrame in the next task.

### ALS with biases

#### Task

Write a script that prints the RMSE of recommendations obtained by
predicting the user-item interaction *i* using ALS. Your ALS model
should make predictions for *i* and the RMSE should be computed on the
final ratings, computed as i+user_mean+item_mean-m (m is the global rating). Training and test
sets should be determined as before. Your ALS model should use the
same parameters as before and be initialized with the random seed
passed on the command line.

#### Required syntax

`als_with_bias_recommender.py <seed>`

#### Test

`tests/test_als_with_bias_recommender.py`

*Note:* compare the RMSE obtained here with the one obtained with the
 basic ALS model. 

