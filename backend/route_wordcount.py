import subprocess
import flask
import threading

lock = threading.Lock()

def trigger_wordcount():
    lock.acquire()
    print("trigger wordcount")

    cmd = 'make df'

    stream = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    output = stream.stdout.decode('utf-8')

    print("wordcount done")

    cmd = 'make clean'

    stream = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    output2 = stream.stdout.decode('utf-8')

    lock.release()

    return flask.Response(output+output2, mimetype='txt')
