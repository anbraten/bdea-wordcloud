import os
from flask import Flask, render_template, redirect
from flask_cors import CORS

import route_wordcloud
import route_wordcount
import route_upload
import config


app = Flask(__name__, static_folder='./templates', static_url_path='')

CORS(app)

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

@app.route('/')
def re():
    return redirect("/index.html", code=302)

app.add_url_rule('/api/uploads', view_func=route_upload.upload, methods=['POST'])
app.add_url_rule('/api/get/all_filenames', view_func=route_upload.get_all_uploaded_files)
app.add_url_rule('/api/uploads/<filename>', view_func=route_upload.uploaded_files)
app.add_url_rule('/api/wordcloud/<filename>', view_func=route_wordcloud.wordcloud)
app.add_url_rule('/api/cumulative-wordcloud', view_func=route_wordcloud.cumulative_wordcloud)
app.add_url_rule('/api/wordcount/trigger', view_func=route_wordcount.trigger_wordcount)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)