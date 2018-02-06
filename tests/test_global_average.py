import subprocess, os

def test_global_average():
    command="python ./answers/global_average.py 123"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(abs(float(process.stdout.read().decode("utf-8"))-1.77491694352)<0.01)
