import os
import flask
import os.path
from werkzeug.utils import secure_filename
import threading
from typing import Dict

base_path = os.path.join(os.getcwd(), 'data')
locks: Dict[str, threading.Lock] = dict()
cumulative_wordcloud_lock = threading.Lock()

def wordcloud(filename: str):
    filename = secure_filename(filename)
    svg_file = os.path.join(base_path, 'wordclouds', filename.replace('.txt', '.svg'))
    text_file = os.path.join(base_path, 'uploads', filename)

    if not os.path.exists(text_file):
        return flask.Response(404)

    if os.path.exists(svg_file):
        return flask.send_file(svg_file)

    if filename in locks and locks[filename].locked():
        print("wait for lock to be released / image to be generated")
        locks[filename].acquire(blocking=True, timeout=-1)
        locks[filename].release() # directly release again as we only wanted to wait here
        return flask.send_file(svg_file)

    # lock image generation from being executed multiple times
    locks[filename] = threading.Lock()
    locks[filename].acquire()

    print("worcloud generation started ...")

    cmd = 'make tfidf WORDCLOUD_TXT_FILE='+filename
    print(cmd)
    os.system(cmd)

    locks[filename].release()

    print("worcloud done")

    return flask.send_file(svg_file)

def cumulative_wordcloud():
    svg_file = os.path.join(base_path, 'wordclouds', "cumulative.svg")

    if os.path.exists(svg_file):
        return flask.send_file(svg_file)

    if cumulative_wordcloud_lock.locked():
        print("wait for lock to be released / image to be generated")
        cumulative_wordcloud_lock.acquire(blocking=True, timeout=-1)
        cumulative_wordcloud_lock.release() # directly release again as we only wanted to wait here
        return flask.send_file(svg_file)

    cumulative_wordcloud_lock.acquire()

    print("cumulative worcloud generation started ...")

    # create empty svg file to prevent parallel execution
    f = open(svg_file, "w")
    f.write("")
    f.close()
    
    cmd = 'make tfidf-cumulative'
    os.system(cmd)

    cumulative_wordcloud_lock.release()

    print("cumulative worcloud done")

    return flask.send_file(svg_file)