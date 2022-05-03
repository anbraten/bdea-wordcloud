import subprocess
import flask

def trigger_wordcount():
    print("trigger wordcount")

    cmd = 'make df'

    stream = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    output = stream.stdout.decode('utf-8')

    print("wordcount done")

    cmd = 'make clean'

    stream = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    output2 = stream.stdout.decode('utf-8')

    return flask.Response(output+output2, mimetype='txt')
