import subprocess, os

def test_als_with_bias_recommender_undisclosed():
    command="python ./answers/als_with_bias_recommender.py 1234"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(abs(float(process.stdout.read().decode("utf-8"))-1.07)<0.03)
