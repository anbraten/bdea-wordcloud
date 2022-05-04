import os
from flask import request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import mimetypes

import config

def upload():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in config.get()['UPLOAD_EXTENSIONS'] or mimetypes.guess_type(filename)[0] != 'text/plain':
            return "Invalid file format", 400
        uploaded_file.save(os.path.join(config.get()['UPLOAD_PATH'], filename))
    return 'success', 204

def get_all_uploaded_files():
    return jsonify([f for f in os.listdir(config.get()['UPLOAD_PATH']) if os.path.isfile(os.path.join(config.get()['UPLOAD_PATH'], f))])

def uploaded_files(filename):
    return send_from_directory(config.get()['UPLOAD_PATH'], filename)
