# LA2: Recommendation Systems with Apache Spark

## Important note

This assignment must be submitted individually. You are encouraged to 
discuss and exchange solutions during the lab sessions or on Slack, but 
you are *not allowed* to share code electronically. Plagiarism, 
unauthorized collaboration and other offenses under Concordia's 
[Academic Code of 
Conduct](http://www.concordia.ca/students/academic-integrity/offences.html) 
will be firmly handled. 

## Preliminary comments

To submit this assignment, you will have to be familiar with Git and
GitHub. If you have never used these technologies, it is recommended to 
go through the following tutorials:
* [Git](https://rogerdudler.github.io/git-guide)
* [GitHub](https://guides.github.com/)

In particular, you will have to be able to:
1. *Clone* a Git repository from GitHub: find the URL of a GitHub repository
and clone it using `git clone <repo_url>`.
2. *Commit* modifications to a local clone of a Git repository: `git add <file>` and `git commit -m "message"`.
3. *Push* modifications from your local clone to the origin repository on GitHub: `git push`.

## Assignment submission

You have to submit your assignment through GitHub classroom, using the following procedure:

1. Accept the assignment at <https://classroom.github.com/a/0vc-fWFA>. This will create your own copy
   of the assignment repository, located at http://github.com/tgteacher/bigdata-la2-your_github_username.
2. Clone your copy of the assignment repository on your computer, and 
implement the functions in `answers/answer.py`, following the instructions in the 
documentation strings. A skeleton of your answer file already exists in file `answers/answer.py`
  with the required syntax for each function.
3. Commit your solution to your local copy of the assignment repository.
4. Push your solution to your GitHub copy of the assignment repository.

You can repeat steps 3 and 4 as many times as you wish. Your assignment 
will be graded based on a snapshot of your repository taken on the 
submission deadline.

## Evaluation

### Grading

#### General Rule

Your assignment will be automatically graded through software tests. 

The tests are already available in directory `tests`. You
may want to run them as you implement your solution, to check that your
code passes them. To do so, you will have to install `pytest` and simply
run `pytest tests` in the base directory of the assignment. Alternatively, you
can install [`act`](https://github.com/nektos/act) to run the GitHub action locally.

Your grade will be determined from the number of passing tests as 
returned by pytest. All tests will contribute equally to the final 
grade. For instance, if 20 tests are evaluated, and your solution passes 18 tests, then your grade 
will be 90%.

This grading scheme is meant to be transparent and objective. However,
it is also radical and you should be very meticulous with your coding: 
make a single syntax error in your answer file, such as a spurious 
tabulation character, and all the tests will fail! To avoid that kind 
of surprises, you are strongly encouraged to check the output of the 
tests on GitHub actions regularly.

#### Exceptions

The rules below aim at discouraging cheating. They might sound a bit harsh,
but in general be cool: if you don't aim at cheating, you probably won't :)

1. You are not allowed to modify the tests to make them pass. Every deliberate
  attempt to modify the tests will result in a grade of 0.
2. You must use the libraries mentioned in the instructions to 
  implement the assignment. Any attempt to implement the solution with a different
  library, for instance Dask when Spark was expected, will result in a grade of 0.
3. You are not allowed to make the tests pass using a hard-coded solution. Your solution
  must, in principle, apply to other similar datasets. Any hard-coded solution will receive 
  the grade of 0.
4. Any deliberate attempt to trick the grading system by making the tests pass
   without providing a correct, non-hardcoded, solution will receive the grade of 0.

 
### Test environment and live feedback
Your code will be tested with Python 3.10. It is your responsibility to
ensure that the tests will pass in this environment. Live feedback on your
assignment is provided through GitHub actions. **Your grade will be
determined from the result of the tests executed in GitHub actions**.
It is strongly suggested that you run the disclosed tests before 
submitting your assignment, using `pytest` or `act` as explained previously.

**Your grade will be determined 
from the result of the
tests executed in Github Actions**.
