import subprocess, os

def test_basic_als_undisclosed():
    command="python ./answers/basic_als_recommender.py 1234"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(abs(float(process.stdout.read().decode("utf-8"))-1.6)<0.05)
