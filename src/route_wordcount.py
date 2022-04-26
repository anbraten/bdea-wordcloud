import subprocess
import flask

def trigger_wordcount():
    print("trigger wordcount")

    cmd = 'make wordcount'
    stream = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    output = stream.stdout.decode('utf-8')

    print("wordcount done")

    return flask.Response(output, mimetype='txt')
