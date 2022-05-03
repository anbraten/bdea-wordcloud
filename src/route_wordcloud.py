import os
import flask
import os.path
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

    # create empty svg file to prevent parallel execution
    f = open(svgFile, "w")
    f.write("")
    f.close()

    cmd = 'make tfidf WORDCLOUD_TXT_FILE='+filename
    print(cmd)
    os.system(cmd)

    print("worcloud done")

    return flask.send_file(svgFile)

def cumulative_wordcloud():
    svgFile = os.path.join(basePath, 'wordclouds', "cumulative.svg")

    if os.path.exists(svgFile):
        return flask.send_file(svgFile)

    print("cumulative worcloud generation started ...")

    # create empty svg file to prevent parallel execution
    f = open(svgFile, "w")
    f.write("")
    f.close()
    
    cmd = 'make tfidf-cumulative'
    os.system(cmd)

    print("cumulative worcloud done")

    return flask.send_file(svgFile)