from flask import Flask, redirect
from flask_cors import CORS

import route_wordcloud
import route_wordcount
import route_upload

app = Flask(__name__, static_folder='./templates', static_url_path='')

CORS(app)

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

@app.route('/')
def re():
    return redirect("/index.html", code=302)

app.add_url_rule('/api/uploads', view_func=route_upload.upload, methods=['POST'])
app.add_url_rule('/api/filenames', view_func=route_upload.get_all_uploaded_files)
app.add_url_rule('/api/wordcloud/<filename>', view_func=route_wordcloud.wordcloud)
app.add_url_rule('/api/cumulative-wordcloud', view_func=route_wordcloud.cumulative_wordcloud)
app.add_url_rule('/api/wordcount-trigger', view_func=route_wordcount.trigger_wordcount)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0')