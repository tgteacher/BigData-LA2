import subprocess

def test_means_and_interaction_undisclosed():
    command="python ./answers/means_and_interaction.py 1234 19"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/means_and_interaction_undisclosed.txt","r").read())
