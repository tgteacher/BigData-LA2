import subprocess, os

def test_als_with_bias_recommender():
    command="python ./answers/als_with_bias_recommender.py 123"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")=="1.05448692337"+os.linesep)
