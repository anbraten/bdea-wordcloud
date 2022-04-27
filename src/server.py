import os
from flask import Flask, render_template

import route_wordcloud
import route_wordcount
import route_upload
import config

app = Flask(__name__)

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

@app.route('/')
def index():
    files = os.listdir(config.get()['UPLOAD_PATH'])
    return render_template('index.html', files=files)

app.add_url_rule('/api/uploads', view_func=route_upload.upload, methods=['POST'])
app.add_url_rule('/api/uploads/<filename>', view_func=route_upload.uploaded_files)
app.add_url_rule('/api/wordcloud/<filename>', view_func=route_wordcloud.wordcloud)
app.add_url_rule('/api/wordcount/trigger', view_func=route_wordcount.trigger_wordcount)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)