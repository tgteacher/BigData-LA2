import subprocess, os

def test_global_average_undisclosed():
    command="python ./answers/global_average.py 1234"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(abs(float(process.stdout.read().decode("utf-8"))-1.78)<0.015)
