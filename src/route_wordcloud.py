import os
import flask
import os.path
import subprocess
from werkzeug.utils import secure_filename

basePath = os.path.join(os.getcwd(), 'data')

def wordcloud(filename: str):
    filename = secure_filename(filename)
    svgFile = os.path.join(basePath, 'wordclouds', filename.replace('.txt', '.svg'))
    textFile = os.path.join(basePath, 'uploads', filename)

    if not os.path.exists(textFile):
        return flask.Response(404)

    if os.path.exists(svgFile):
        return flask.send_file(svgFile)

    print("worcloud generation started ...")

    cmd = 'WORDCLOUD_TXT_FILE='+filename+' make tfidf'
    stream = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    output = stream.stdout.decode('utf-8')

    print("worcloud done")

    return flask.send_file(svgFile)

def cumulative_wordcloud():
    return flask.Response(500)